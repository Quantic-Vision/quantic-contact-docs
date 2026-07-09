"""
Auditoría estructural del wiki: front matter, imágenes, nav, citas.

Ejecutar desde scraper/:
    .venv\\Scripts\\python audit_structure.py
"""

import re
import yaml
from pathlib import Path

DOCS_DIR = Path("../docs").resolve()
MKDOCS_YML = Path("../mkdocs.yml").resolve()
OUT_FILE = Path("../auditoria_estructural.md").resolve()

REQUIRED_FIELDS = ["title", "resumen", "seccion", "tipo", "nivel", "roles", "fuente", "obsoleto", "relacionados"]
VALID_TIPO = {"tutorial", "guia", "referencia", "concepto", "faq", "troubleshooting"}
VALID_NIVEL = {"basico", "intermedio", "avanzado"}
VALID_ROLES = {"administrador", "agente", "desarrollador"}
VALID_FUENTE = {"zh", "en", "zh+en"}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
IMG_MD_RE = re.compile(r'!\[[^\]]*\]\(([^)\s]+)\)')
LINK_MD_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)\s#]+)(?:#[^)]*)?\)')
SOURCES_BLOCK_RE = re.compile(r"^## Fuentes\s*\n((?:- `[^`]+`\s*\n?)+)", re.MULTILINE)
WILDCARD_SOURCE_RE = re.compile(r"`[^`]*\*[^`]*`")


def load_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def main():
    md_files = sorted(DOCS_DIR.rglob("*.md"))
    issues = []

    # --- 1. Front matter ---
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel = md.relative_to(DOCS_DIR.parent).as_posix()
        fm = load_frontmatter(text)
        if fm is None:
            issues.append(f"[FRONTMATTER] `{rel}` — no tiene front matter YAML válido")
            continue
        missing = [f for f in REQUIRED_FIELDS if f not in fm]
        if missing:
            issues.append(f"[FRONTMATTER] `{rel}` — faltan campos: {', '.join(missing)}")
        if fm.get("tipo") not in VALID_TIPO:
            issues.append(f"[FRONTMATTER] `{rel}` — tipo inválido: `{fm.get('tipo')}`")
        if fm.get("nivel") not in VALID_NIVEL:
            issues.append(f"[FRONTMATTER] `{rel}` — nivel inválido: `{fm.get('nivel')}`")
        if fm.get("fuente") not in VALID_FUENTE:
            issues.append(f"[FRONTMATTER] `{rel}` — fuente inválida: `{fm.get('fuente')}`")
        roles = fm.get("roles") or []
        bad_roles = [r for r in roles if r not in VALID_ROLES]
        if bad_roles:
            issues.append(f"[FRONTMATTER] `{rel}` — roles inválidos: {bad_roles}")
        if not fm.get("title"):
            issues.append(f"[FRONTMATTER] `{rel}` — title vacío")
        if not fm.get("resumen"):
            issues.append(f"[FRONTMATTER] `{rel}` — resumen vacío")

    # --- 2. Citas: wildcards y existencia de archivo (solo dentro del bloque ## Fuentes) ---
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel = md.relative_to(DOCS_DIR.parent).as_posix()
        for block_match in SOURCES_BLOCK_RE.finditer(text):
            for line in block_match.group(1).splitlines():
                path_m = re.match(r"- `([^`]+)`", line.strip())
                if not path_m:
                    continue
                src_path = path_m.group(1)
                if "*" in src_path:
                    issues.append(f"[CITAS] `{rel}` — cita con comodín: `{src_path}`")
                    continue
                full = DOCS_DIR.parent / src_path
                if not full.exists():
                    issues.append(f"[CITAS] `{rel}` — cita a archivo inexistente: `{src_path}`")

    # --- 3. Imágenes: existencia y huérfanas ---
    referenced_images = set()
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel = md.relative_to(DOCS_DIR.parent).as_posix()
        for img_m in IMG_MD_RE.finditer(text):
            img_path = img_m.group(1)
            if img_path.startswith("http"):
                continue
            resolved = (md.parent / img_path).resolve()
            referenced_images.add(resolved)
            if not resolved.exists():
                issues.append(f"[IMAGEN ROTA] `{rel}` — referencia a imagen inexistente: `{img_path}`")
            # Alt text check
            alt_m = re.search(r'!\[([^\]]*)\]', img_m.group(0))
            if alt_m and len(alt_m.group(1).strip()) < 5:
                issues.append(f"[IMAGEN] `{rel}` — alt text muy corto o vacío para `{img_path}`")

    all_image_files = set((DOCS_DIR / "assets" / "images").rglob("*"))
    all_image_files = {p.resolve() for p in all_image_files if p.is_file()}
    orphan_images = all_image_files - referenced_images
    for orphan in sorted(orphan_images):
        rel = orphan.relative_to(DOCS_DIR.parent).as_posix()
        issues.append(f"[IMAGEN HUÉRFANA] `{rel}` — no está referenciada en ningún .md")

    # --- 4. Nav vs archivos reales ---
    mkdocs_text = MKDOCS_YML.read_text(encoding="utf-8")
    nav_paths = set(re.findall(r'((?:[a-zA-Z0-9_\-]+/)?[a-zA-Z0-9_\-\.]+\.md)', mkdocs_text))
    all_md_rel = {p.relative_to(DOCS_DIR).as_posix() for p in md_files}
    nav_missing_files = nav_paths - all_md_rel
    for nm in sorted(nav_missing_files):
        issues.append(f"[NAV] mkdocs.yml referencia `{nm}` pero el archivo no existe")
    orphan_pages = all_md_rel - nav_paths
    for op in sorted(orphan_pages):
        issues.append(f"[NAV] `docs/{op}` no está en el nav de mkdocs.yml (revisar si es intencional, ej. páginas de FAQ)")

    # --- 5. relacionados: apuntan a páginas existentes ---
    slug_to_path = {p.stem: p for p in md_files}
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel = md.relative_to(DOCS_DIR.parent).as_posix()
        fm = load_frontmatter(text)
        if not fm:
            continue
        for r in (fm.get("relacionados") or []):
            if r not in slug_to_path:
                issues.append(f"[RELACIONADOS] `{rel}` — relacionado `{r}` no coincide con ningún archivo (por nombre base)")

    # --- Escribir reporte ---
    lines = ["# Auditoría estructural del wiki\n"]
    lines.append(f"Total de artículos analizados: **{len(md_files)}**\n")
    lines.append(f"Total de hallazgos: **{len(issues)}**\n")
    lines.append("---\n")
    by_cat = {}
    for i in issues:
        cat = i.split("]")[0][1:]
        by_cat.setdefault(cat, []).append(i)
    for cat, items in sorted(by_cat.items()):
        lines.append(f"## {cat} ({len(items)})\n")
        for it in items:
            lines.append(f"- {it}")
        lines.append("")

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Artículos analizados: {len(md_files)}")
    print(f"Hallazgos totales: {len(issues)}")
    for cat, items in sorted(by_cat.items()):
        print(f"  {cat}: {len(items)}")
    print(f"Detalle completo en {OUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
