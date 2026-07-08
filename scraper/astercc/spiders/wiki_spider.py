"""
Spider para wiki.astercc.org (DokuWiki).

Estructura del índice DokuWiki:
  - Sub-namespaces: /doku.php?id=start&idx=en%3Amodule_manual  → recursar
  - Páginas:        /doku.php?id=en:module_manual:pbx           → descargar raw

Ejecutar desde el directorio scraper/:
    scrapy crawl wiki

Reanudar tras interrupción:
    scrapy crawl wiki

Forzar re-descarga ignorando caché:
    scrapy crawl wiki -s HTTPCACHE_ENABLED=False
"""

import re
from urllib.parse import unquote, urljoin

import scrapy

from astercc.items import WikiPageItem


BASE_URL   = "https://wiki.astercc.org"
NAMESPACES = ["en", "zh"]


def index_url(ns: str) -> str:
    return f"{BASE_URL}/doku.php?id=start&idx={ns}"


def export_raw_url(page_id: str) -> str:
    return f"{BASE_URL}/doku.php?id={page_id}&do=export_raw"


def namespace_of(page_id: str) -> str:
    return page_id.split(":")[0] if ":" in page_id else page_id


class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["wiki.astercc.org"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._discovered: set[str] = set()

    # ── Inicio ─────────────────────────────────────────────────────────────────

    async def start(self):
        for ns in NAMESPACES:
            yield scrapy.Request(
                index_url(ns),
                callback=self.parse_index,
                meta={"namespace": ns},
            )

    # ── Índice ─────────────────────────────────────────────────────────────────

    def parse_index(self, response):
        ns = response.meta["namespace"]

        for a in response.css("a[href]"):
            href = a.attrib["href"]

            # ── Sub-namespace: ?id=start&idx=en%3Amodule_manual ────────────────
            idx_match = re.search(r"[?&]idx=([^&]+)", href)
            if idx_match:
                raw_idx = unquote(idx_match.group(1))          # "en:module_manual"
                if raw_idx.startswith(f"{ns}:") or raw_idx == ns:
                    full_url = urljoin(BASE_URL, href)
                    yield scrapy.Request(
                        full_url,
                        callback=self.parse_index,
                        meta={"namespace": ns},
                    )
                continue

            # ── Página: ?id=en:module_manual:pbx (sin idx ni do=) ──────────────
            id_match = re.search(r"[?&]id=([^&]+)", href)
            if not id_match:
                continue
            page_id = unquote(id_match.group(1))

            # Descartar URLs de acción (do=revisions, do=login, etc.)
            if "do=" in href:
                continue

            if not page_id.startswith(f"{ns}:"):
                continue

            if page_id in self._discovered:
                continue

            self._discovered.add(page_id)
            yield scrapy.Request(
                export_raw_url(page_id),
                callback=self.parse_page,
                meta={"page_id": page_id, "namespace": ns},
            )

    # ── Descarga raw ───────────────────────────────────────────────────────────

    def parse_page(self, response):
        page_id   = response.meta["page_id"]
        namespace = response.meta["namespace"]
        content   = response.text

        if not content.strip():
            self.logger.warning(f"Vacía: {page_id}")
            return

        yield WikiPageItem(
            page_id=page_id,
            namespace=namespace,
            content=content,
            url=response.url,
        )

    # ── Log final ──────────────────────────────────────────────────────────────

    def closed(self, reason):
        by_ns: dict[str, int] = {}
        for pid in self._discovered:
            ns = namespace_of(pid)
            by_ns[ns] = by_ns.get(ns, 0) + 1
        for ns, count in sorted(by_ns.items()):
            self.logger.info(f"[{ns}] páginas descubiertas: {count}")
        self.logger.info(f"Total: {len(self._discovered)} | Razón de cierre: {reason}")
