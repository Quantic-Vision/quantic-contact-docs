"""
Migra el formato de citas de fuentes en docs/*.md:

    De:  *Fuentes: `raw/a.txt`, `raw/b.txt`.*
    A:   ## Fuentes

         - `raw/a.txt`
         - `raw/b.txt`

Ejecutar desde scraper/:
    python migrate_citations.py
"""

import re
from pathlib import Path

DOCS_DIR = Path("../docs")

# Captura la línea completa en cursiva que empieza con *Fuente(s):
OLD_LINE_RE = re.compile(r"^\*Fuentes?:?\s*(.+?)\*\s*$", re.MULTILINE)
PATH_RE = re.compile(r"`([^`]+)`")


def convert(text: str) -> tuple[str, int]:
    matches = list(OLD_LINE_RE.finditer(text))
    if not matches:
        return text, 0

    count = 0
    for m in reversed(matches):  # reemplazar de atrás hacia adelante para no invalidar offsets
        paths = PATH_RE.findall(m.group(1))
        if not paths:
            continue
        bullet_list = "\n".join(f"- `{p}`" for p in paths)
        replacement = f"## Fuentes\n\n{bullet_list}"
        text = text[: m.start()] + replacement + text[m.end():]
        count += 1
    return text, count


def main():
    total_files = 0
    total_converted = 0
    for md in sorted(DOCS_DIR.rglob("*.md")):
        original = md.read_text(encoding="utf-8")
        converted, count = convert(original)
        if count:
            md.write_text(converted, encoding="utf-8")
            total_files += 1
            total_converted += count
            print(f"Migrado: {md.relative_to(DOCS_DIR)}")

    print(f"\nArchivos migrados: {total_files}")


if __name__ == "__main__":
    main()
