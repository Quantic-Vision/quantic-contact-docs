import logging
from scrapy import signals


class DualLogExtension:
    """Escribe logs simultáneamente a consola y a scraper.log."""

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        return ext

    def spider_opened(self, spider):
        fh = logging.FileHandler("scraper.log", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s [%(name)s] %(levelname)-8s %(message)s"
        ))
        logging.getLogger().addHandler(fh)
