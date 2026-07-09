"""
Inventario de imágenes disponibles por artículo del wiki en español.

- Lee cada docs/*.md, extrae su lista de "## Fuentes" (rutas raw/...).
- Para cada fuente, busca referencias de imagen {{...}} en el .txt original.
- Resuelve cada referencia a un archivo real en raw/{lang}/images/... y
  comprueba si ya se descargó.
- Agrupa por artículo y compara disponibilidad EN vs ZH.

Ejecutar desde scraper/:
    .venv\\Scripts\\python image_inventory.py
"""

import re
from pathlib import Path

DOCS_DIR = Path("../docs")
RAW_DIR = Path("../raw")
OUT_FILE = Path("../inventario_imagenes.md")

SOURCES_BLOCK_RE = re.compile(r"^## Fuentes\s*\n((?:- `[^`]+`\s*\n?)+)", re.MULTILINE)
BULLET_PATH_RE = re.compile(r"^- `([^`]+)`", re.MULTILINE)
TITLE_RE = re.compile(r'^title:\s*"?([^"\n]+)"?', re.MULTILINE)

IMG_PATTERN = re.compile(
    r'\{\{:?'
    r'([^}|?\s]+\.(?:png|jpg|jpeg|gif|svg|bmp|webp))'
    r'(?:\?[^|}]*)?'
    r'(?:\|[^}]*)?'
    r'\}\}',
    re.IGNORECASE,
)


def extract_sources(md_text: str) -> list[str]:
    paths = []
    for block_match in SOURCES_BLOCK_RE.finditer(md_text):
        block = block_match.group(1)
        paths.extend(BULLET_PATH_RE.findall(block))
    return paths


def extract_title(md_text: str) -> str:
    m = TITLE_RE.search(md_text)
    return m.group(1) if m else "(sin título)"


def namespace_of(media_id: str, fallback: str) -> str:
    return media_id.split(":")[0] if ":" in media_id else fallback


def media_id_to_path(media_id: str, namespace: str) -> Path:
    parts = media_id.split(":")
    if parts[0] == namespace:
        parts = parts[1:]
    rel = Path(*parts) if len(parts) > 1 else Path(parts[0])
    return RAW_DIR / namespace / "images" / rel


def lang_of_source(src_path: str) -> str:
    # raw/en/... or raw/zh/...
    parts = src_path.split("/")
    return parts[1] if len(parts) > 1 else "?"


def images_for_source(src_path: str) -> list[tuple[str, Path, bool]]:
    """Retorna [(media_id, ruta_resuelta, existe)] para un archivo fuente."""
    full = RAW_DIR.parent / src_path
    if not full.exists():
        return []
    lang = lang_of_source(src_path)
    content = full.read_text(encoding="utf-8", errors="ignore")
    refs = IMG_PATTERN.findall(content)
    seen = set()
    out = []
    for ref in refs:
        media_id = ref.lstrip(":")
        if media_id in seen:
            continue
        seen.add(media_id)
        ns = namespace_of(media_id, lang)
        resolved = media_id_to_path(media_id, ns)
        out.append((media_id, resolved, resolved.exists()))
    return out


def main():
    md_files = sorted(DOCS_DIR.rglob("*.md"))

    total_articles = 0
    articles_with_images_available = 0
    articles_already_illustrated = 0
    total_images_available = 0

    lines = []
    lines.append("# Inventario de imágenes disponibles por artículo\n")
    lines.append(
        "Compara, para cada artículo de `docs/`, cuántas imágenes están "
        "disponibles (ya descargadas en `raw/{en,zh}/images/`) a partir de "
        "sus fuentes citadas, separado por idioma.\n"
    )
    lines.append(
        "**Hallazgo validado visualmente:** las capturas de pantalla del "
        "namespace ZH muestran la interfaz de AsterCC completamente en "
        "chino, ilegible para el lector de este wiki en español. Las "
        "capturas del namespace EN muestran la interfaz en inglés, "
        "legible y consistente con los nombres de campo que ya se "
        "tradujeron al redactar cada artículo. Por eso la recomendación "
        "prioriza **EN** aunque ZH tenga más imágenes disponibles; ZH solo "
        "se recomienda como respaldo cuando no hay ninguna captura EN.\n"
    )
    lines.append("---\n")

    rows = []

    for md_path in md_files:
        rel_md = md_path.relative_to(DOCS_DIR.parent)
        text = md_path.read_text(encoding="utf-8", errors="ignore")
        sources = extract_sources(text)
        if not sources:
            continue

        # ¿ya tiene imágenes insertadas? (busca ![...](../assets/images o assets/images)
        already_has_images = bool(re.search(r'!\[[^\]]*\]\([^)]*assets/images', text))

        en_imgs = []
        zh_imgs = []
        for src in sources:
            lang = lang_of_source(src)
            imgs = images_for_source(src)
            for media_id, resolved, exists in imgs:
                entry = (src, media_id, resolved, exists)
                if lang == "en":
                    en_imgs.append(entry)
                elif lang == "zh":
                    zh_imgs.append(entry)

        total_articles += 1
        if already_has_images:
            articles_already_illustrated += 1

        en_available = [e for e in en_imgs if e[3]]
        zh_available = [e for e in zh_imgs if e[3]]

        if en_available or zh_available:
            articles_with_images_available += 1
        total_images_available += len(en_available) + len(zh_available)

        rows.append({
            "path": str(rel_md).replace("\\", "/"),
            "title": extract_title(text),
            "already": already_has_images,
            "en_total": len(en_imgs),
            "en_available": len(en_available),
            "zh_total": len(zh_imgs),
            "zh_available": len(zh_available),
            "en_imgs": en_available,
            "zh_imgs": zh_available,
        })

    lines.append("## Resumen global\n")
    lines.append(f"- Artículos con fuentes citadas: **{total_articles}**")
    lines.append(f"- Artículos que ya tienen alguna imagen insertada: **{articles_already_illustrated}**")
    lines.append(f"- Artículos con al menos 1 imagen disponible para insertar: **{articles_with_images_available}**")
    lines.append(f"- Total de imágenes disponibles (descargadas, EN+ZH, sin insertar aún ni contar las ya usadas): **{total_images_available}**\n")
    lines.append("---\n")

    lines.append("## Detalle por artículo\n")
    lines.append("| Artículo | Ya ilustrado | Imgs EN disp. | Imgs ZH disp. | Recomendación |")
    lines.append("|---|---|---|---|---|")

    for r in sorted(rows, key=lambda x: -( x["en_available"] + x["zh_available"])):
        if r["en_available"] == 0 and r["zh_available"] == 0:
            continue
        # Criterio validado visualmente: las capturas ZH muestran la UI en
        # chino (ilegible para el lector) y las EN muestran la UI en inglés
        # (legible, mapea directo a los nombres de campo ya traducidos).
        # Se prefiere EN siempre que haya disponibilidad; ZH solo como
        # respaldo cuando no hay ninguna captura EN para ese artículo.
        if r["en_available"] > 0:
            rec = "EN (UI en inglés, legible)"
        else:
            rec = "ZH (única disponible — UI en chino, revisar antes de usar)"
        already = "Sí" if r["already"] else "No"
        lines.append(
            f"| `{r['path']}` | {already} | {r['en_available']} | {r['zh_available']} | {rec} |"
        )

    lines.append("\n---\n")
    lines.append("## Artículos SIN ninguna imagen disponible\n")
    for r in rows:
        if r["en_available"] == 0 and r["zh_available"] == 0:
            lines.append(f"- `{r['path']}`")

    lines.append("\n---\n")
    lines.append("## Detalle de rutas de imagen por artículo (con imágenes disponibles)\n")
    for r in rows:
        if r["en_available"] == 0 and r["zh_available"] == 0:
            continue
        lines.append(f"### {r['path']}\n")
        if r["zh_imgs"]:
            lines.append("**ZH:**")
            for src, media_id, resolved, exists in r["zh_imgs"]:
                lines.append(f"- `{media_id}` → `{resolved.relative_to(RAW_DIR.parent).as_posix()}` (fuente: `{src}`)")
        if r["en_imgs"]:
            lines.append("**EN:**")
            for src, media_id, resolved, exists in r["en_imgs"]:
                lines.append(f"- `{media_id}` → `{resolved.relative_to(RAW_DIR.parent).as_posix()}` (fuente: `{src}`)")
        lines.append("")

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Artículos con fuentes: {total_articles}")
    print(f"Ya ilustrados: {articles_already_illustrated}")
    print(f"Con imágenes disponibles para insertar: {articles_with_images_available}")
    print(f"Total imágenes disponibles: {total_images_available}")
    print(f"Detalle completo en {OUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
