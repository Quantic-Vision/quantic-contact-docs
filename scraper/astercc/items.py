import scrapy


class WikiPageItem(scrapy.Item):
    page_id   = scrapy.Field()   # ej: "en:installation:iso"
    namespace = scrapy.Field()   # "en" o "zh"
    content   = scrapy.Field()   # texto raw de DokuWiki
    url       = scrapy.Field()   # URL de origen
