BOT_NAME = "astercc"
SPIDER_MODULES = ["astercc.spiders"]
NEWSPIDER_MODULE = "astercc.spiders"

# ── Identidad ──────────────────────────────────────────────────────────────────
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
ROBOTSTXT_OBEY = False

# ── Concurrencia ───────────────────────────────────────────────────────────────
CONCURRENT_REQUESTS = 1          # una request a la vez — comportamiento humano
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# ── Delays con AutoThrottle (simula persona) ───────────────────────────────────
DOWNLOAD_DELAY = 4.0             # base mínima en segundos
RANDOMIZE_DOWNLOAD_DELAY = True  # Scrapy multiplica por random(0.5, 1.5) → 2–6 s

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 4.0
AUTOTHROTTLE_MAX_DELAY = 30.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# ── Reintentos ─────────────────────────────────────────────────────────────────
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [429, 500, 502, 503, 504]
RETRY_BACKOFF_BASE = 2.0        # espera exponencial entre reintentos

# ── Headers por defecto ────────────────────────────────────────────────────────
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8,zh;q=0.7",
}

# ── Cache HTTP (permite reanudar sin re-descargar) ─────────────────────────────
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0   # nunca expira — usar --set HTTPCACHE_ENABLED=False para forzar re-descarga
HTTPCACHE_DIR = ".httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = [429, 500, 502, 503, 504]

# ── Job dir (permite reanudar el spider si se interrumpe) ─────────────────────
JOBDIR = ".scrapy_job"

# ── Pipeline ───────────────────────────────────────────────────────────────────
ITEM_PIPELINES = {
    "astercc.pipelines.SavePagePipeline": 100,
}

# ── Logs (consola + archivo simultáneamente) ───────────────────────────────────
LOG_LEVEL = "INFO"
FEED_EXPORT_ENCODING = "utf-8"

EXTENSIONS = {
    "scrapy.extensions.corestats.CoreStats": 0,
    "scrapy.extensions.logcount.LogCount": 0,
    "scrapy.extensions.telnet.TelnetConsole": None,   # deshabilitar telnet
    "scrapy.extensions.logstats.LogStats": 0,
    "scrapy.extensions.spiderstate.SpiderState": 0,
    "scrapy.extensions.throttle.AutoThrottle": 0,
    "astercc.extensions.DualLogExtension": 100,
}
