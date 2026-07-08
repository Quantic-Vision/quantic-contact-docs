"""
Auditoría de cobertura — Fase 4 (verificación honesta, no estimada).

Compara los archivos `raw/` realmente citados como fuente en `docs/*.md`
(bajo el heading "## Fuentes", como lista de viñetas) contra el listado
completo de páginas scrapeadas, y reporta cobertura separada por idioma
(EN vs ZH), agrupando lo no citado por namespace.

Ejecutar desde scraper/:
    python audit_coverage.py
"""

import re
from pathlib import Path
from collections import defaultdict

DOCS_DIR = Path("../docs")
RAW_DIR = Path("../raw")
OUT_FILE = Path("../auditoria_cobertura.md")

# Heading "## Fuentes" seguido de líneas "- `raw/...`"
SOURCES_BLOCK_RE = re.compile(r"^## Fuentes\s*\n((?:- `[^`]+`\s*\n?)+)", re.MULTILINE)
BULLET_PATH_RE = re.compile(r"^- `([^`]+)`", re.MULTILINE)


def get_cited_paths():
    cited = set()
    doc_by_path = defaultdict(list)
    for md in DOCS_DIR.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for block_match in SOURCES_BLOCK_RE.finditer(text):
            block = block_match.group(1)
            for p in BULLET_PATH_RE.findall(block):
                norm = p.replace("\\", "/")
                cited.add(norm)
                doc_by_path[norm].append(str(md.relative_to(DOCS_DIR)))
    return cited, doc_by_path


def get_all_raw_pages():
    pages = []
    for lang in ("en", "zh"):
        lang_dir = RAW_DIR / lang
        if not lang_dir.exists():
            continue
        for txt in sorted(lang_dir.rglob("*.txt")):
            pages.append(str(txt.relative_to(RAW_DIR.parent)).replace("\\", "/"))
    return pages


def lang_of(path: str) -> str:
    # raw/en/... o raw/zh/...
    parts = path.split("/")
    return parts[1] if len(parts) > 1 else "?"


def top_namespace(path: str) -> str:
    parts = path.split("/")
    if len(parts) >= 3:
        return f"{parts[1]}/{parts[2]}"
    return parts[1] if len(parts) > 1 else path


def main():
    cited, doc_by_path = get_cited_paths()
    all_pages = get_all_raw_pages()

    by_lang_total = defaultdict(int)
    by_lang_covered = defaultdict(int)
    not_covered = []

    for p in all_pages:
        lang = lang_of(p)
        by_lang_total[lang] += 1
        if p in cited:
            by_lang_covered[lang] += 1
        else:
            not_covered.append(p)

    total = len(all_pages)
    covered_total = sum(by_lang_covered.values())
    pct_total = 100 * covered_total / total if total else 0

    by_ns = defaultdict(list)
    for p in not_covered:
        by_ns[top_namespace(p)].append(p)

    lines = []
    lines.append("# Auditoría de cobertura — raw/ vs docs/")
    lines.append("")
    lines.append("Cálculo: **archivos fuente citados bajo `## Fuentes` en algún artículo** ÷ **archivos fuente totales en `raw/`**.")
    lines.append("")
    lines.append("## Cobertura global")
    lines.append("")
    lines.append(f"- Total: **{covered_total}/{total} ({pct_total:.1f}%)**")
    lines.append("")
    lines.append("## Cobertura por idioma")
    lines.append("")
    lines.append("| Idioma | Citadas | Total | % |")
    lines.append("|---|---|---|---|")
    for lang in sorted(by_lang_total.keys()):
        c = by_lang_covered[lang]
        t = by_lang_total[lang]
        pct = 100 * c / t if t else 0
        lines.append(f"| {lang.upper()} | {c} | {t} | {pct:.1f}% |")
    lines.append("")
    lines.append("> El chino (ZH) es la fuente primaria del proyecto (más completa en el wiki original).")
    lines.append("> Un archivo EN bajo cobertura no implica necesariamente contenido perdido si su equivalente ZH")
    lines.append("> ya fue leído y es una traducción cercana — pero si nunca se verificó, no se puede asumir que")
    lines.append("> coincide. El detalle de abajo lista ambos idiomas para poder decidir caso por caso.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Páginas NO citadas, agrupadas por namespace")
    lines.append("")

    for ns in sorted(by_ns.keys(), key=lambda k: -len(by_ns[k])):
        items = by_ns[ns]
        lines.append(f"### {ns} — {len(items)} páginas sin citar")
        lines.append("")
        for p in sorted(items):
            lines.append(f"- `{p}`")
        lines.append("")

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print(f"Cobertura total: {covered_total}/{total} ({pct_total:.1f}%)")
    for lang in sorted(by_lang_total.keys()):
        c = by_lang_covered[lang]
        t = by_lang_total[lang]
        pct = 100 * c / t if t else 0
        print(f"  {lang.upper()}: {c}/{t} ({pct:.1f}%)")
    print(f"Detalle completo en {OUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
