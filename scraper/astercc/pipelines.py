import os
import json
import logging
from pathlib import Path


OUTPUT_DIR = Path("../raw")
log = logging.getLogger(__name__)


class SavePagePipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider=None):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.metadata: list[dict] = []

    def process_item(self, item, spider=None):
        from urllib.parse import unquote
        page_id   = item["page_id"]
        namespace = item["namespace"]
        content   = item["content"]

        if not content or not content.strip():
            log.warning(f"Página vacía, omitida: {page_id}")
            return item

        # Quitar el prefijo del namespace si ya está incluido en el page_id
        rel_id = page_id
        if rel_id.startswith(f"{namespace}:"):
            rel_id = rel_id[len(namespace) + 1:]

        # Decodificar caracteres URL-encoded (%E9%A2... → chino legible)
        rel_id = unquote(rel_id)
        rel = rel_id.replace(":", os.sep)
        out_path = OUTPUT_DIR / namespace / (rel + ".txt")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")

        self.metadata.append({
            "page_id":   page_id,
            "namespace": namespace,
            "url":       item["url"],
            "chars":     len(content),
            "file":      str(out_path),
        })

        log.info(f"Guardado: {out_path}")
        return item

    def close_spider(self, spider=None):
        meta_path = OUTPUT_DIR / "metadata.json"
        meta_path.write_text(
            json.dumps(self.metadata, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        log.info(f"Metadatos guardados: {meta_path} ({len(self.metadata)} páginas)")
