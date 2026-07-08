"""
Descargador de imágenes referenciadas en los archivos raw del wiki AsterCC.

- Analiza todos los .txt en raw/en/ y raw/zh/
- Extrae referencias DokuWiki: {{:namespace:path:imagen.jpg?size|alt}}
- Descarga cada imagen única a raw/{namespace}/images/{path}/
- Límite: < 15 imágenes/min (mínimo 4.1 s entre descargas + jitter aleatorio)
- Reanudable: omite imágenes ya descargadas

Ejecutar desde el directorio scraper/:
    .venv\\Scripts\\python download_images.py
"""

import re
import time
import random
import logging
import hashlib
from pathlib import Path
from urllib.parse import quote, urlencode

import requests

# ─── CONFIG ───────────────────────────────────────────────────────────────────

BASE_URL   = "https://wiki.astercc.org"
RAW_DIR    = Path("../raw")
NAMESPACES = ["en", "zh"]

# Límite de velocidad: < 15 img/min → mínimo 4.1 s entre descargas
DELAY_MIN  = 4.1
DELAY_MAX  = 7.0    # jitter hasta 7 s para simular comportamiento humano
DELAY_ON_ERROR  = 20.0
MAX_RETRIES     = 4
REQUEST_TIMEOUT = 30

LOG_FILE = "images.log"

# ─── LOGGING ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

def log_section(title: str):
    log.info("")
    log.info(f"{'─' * 60}")
    log.info(f"  {title}")
    log.info(f"{'─' * 60}")

# ─── HTTP SESSION ─────────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Referer": BASE_URL,
})

# ─── EXTRACCIÓN DE REFERENCIAS ────────────────────────────────────────────────

# Captura: {{:namespace:path:archivo.ext?tamaño|alt}}
# Grupo 1 = media_id completo (ej: "zh:new:img.jpg")
IMG_PATTERN = re.compile(
    r'\{\{:?'                               # {{ con : opcional
    r'([^}|?\s]+\.(?:png|jpg|jpeg|gif|svg|bmp|webp))'  # grupo 1: media_id
    r'(?:\?[^|}]*)?'                        # ?tamaño opcional
    r'(?:\|[^}]*)?'                         # |alt opcional
    r'\}\}',
    re.IGNORECASE,
)


def extract_image_refs(txt_path: Path) -> list[str]:
    """Extrae media_ids únicos de un archivo .txt de DokuWiki."""
    content = txt_path.read_text(encoding="utf-8", errors="ignore")
    matches = IMG_PATTERN.findall(content)
    # Normalizar: quitar : inicial si lo tiene
    normalized = [m.lstrip(":") for m in matches]
    # Deduplicar preservando orden
    seen: set[str] = set()
    unique = []
    for m in normalized:
        if m not in seen:
            seen.add(m)
            unique.append(m)
    return unique


def namespace_of(media_id: str) -> str:
    """Retorna el namespace (primer componente) de un media_id."""
    return media_id.split(":")[0] if ":" in media_id else "en"


def media_id_to_path(media_id: str, namespace: str) -> Path:
    """
    Convierte 'zh:新手上路:imagen.jpg' a:
    raw/zh/images/新手上路/imagen.jpg
    """
    parts = media_id.split(":")
    # Quitar el namespace del inicio si está incluido
    if parts[0] == namespace:
        parts = parts[1:]
    rel = Path(*parts) if len(parts) > 1 else Path(parts[0])
    return RAW_DIR / namespace / "images" / rel


def media_fetch_url(media_id: str) -> str:
    """URL de descarga para un media_id de DokuWiki."""
    return f"{BASE_URL}/lib/exe/fetch.php?media={quote(media_id, safe=':')}"

# ─── DESCARGA ─────────────────────────────────────────────────────────────────

def download_image(media_id: str, dest: Path) -> bool:
    """
    Descarga una imagen con reintentos.
    Retorna True si fue descargada o ya existía, False si falló.
    """
    if dest.exists() and dest.stat().st_size > 0:
        log.info(f"  [SKIP]     Ya existe → {dest}")
        return True

    url = media_fetch_url(media_id)
    log.info(f"  [URL]      {url}")
    log.info(f"  [DESTINO]  {dest}")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)
            r.raise_for_status()

            content_type = r.headers.get("Content-Type", "")
            if "text/html" in content_type:
                log.warning(f"  [WARN]     Servidor devolvió HTML en vez de imagen — posiblemente no existe")
                return False

            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

            size_kb = dest.stat().st_size / 1024
            log.info(f"  [OK]       Descargada ({size_kb:.1f} KB)")
            return True

        except requests.exceptions.HTTPError as e:
            code = e.response.status_code if e.response else "?"
            if code == 404:
                log.warning(f"  [404]      Imagen no encontrada en el servidor")
                return False
            log.warning(f"  [ERROR]    HTTP {code} — intento {attempt}/{MAX_RETRIES}")
        except requests.exceptions.RequestException as e:
            log.warning(f"  [ERROR]    {e} — intento {attempt}/{MAX_RETRIES}")

        if attempt < MAX_RETRIES:
            wait = DELAY_ON_ERROR * attempt + random.uniform(0, 5)
            log.info(f"  [ESPERA]   {wait:.1f}s antes de reintentar...")
            time.sleep(wait)

    log.error(f"  [FALLO]    No se pudo descargar tras {MAX_RETRIES} intentos")
    return False

# ─── FASE 1: ANÁLISIS ─────────────────────────────────────────────────────────

def analyze_files() -> dict[str, str]:
    """
    Recorre todos los .txt y extrae referencias de imágenes.
    Retorna dict: { media_id → namespace_destino }
    """
    log_section("FASE 1 — Análisis de archivos")

    all_images: dict[str, str] = {}  # media_id → namespace
    total_files = 0
    files_with_images = 0

    for ns in NAMESPACES:
        ns_dir = RAW_DIR / ns
        if not ns_dir.exists():
            log.warning(f"[ANÁLISIS] Directorio no encontrado: {ns_dir}")
            continue

        txt_files = list(ns_dir.rglob("*.txt"))
        log.info(f"[ANÁLISIS] Namespace [{ns}]: {len(txt_files)} archivos encontrados")

        for txt_path in sorted(txt_files):
            total_files += 1
            refs = extract_image_refs(txt_path)

            rel = txt_path.relative_to(RAW_DIR)
            if refs:
                files_with_images += 1
                log.info(f"[ANÁLISIS] {rel}")
                log.info(f"           └─ {len(refs)} imagen(es) referenciada(s)")
                for ref in refs:
                    img_ns = namespace_of(ref)
                    if ref not in all_images:
                        all_images[ref] = img_ns
                        log.info(f"              · {ref}")
            else:
                log.info(f"[ANÁLISIS] {rel}  (sin imágenes)")

    log.info("")
    log.info(f"[ANÁLISIS] ════════════════════════════════════")
    log.info(f"[ANÁLISIS] Archivos analizados   : {total_files}")
    log.info(f"[ANÁLISIS] Archivos con imágenes : {files_with_images}")
    log.info(f"[ANÁLISIS] Imágenes únicas       : {len(all_images)}")
    log.info(f"[ANÁLISIS] ════════════════════════════════════")

    return all_images

# ─── FASE 2: DESCARGA ─────────────────────────────────────────────────────────

def download_all(images: dict[str, str]):
    """Descarga todas las imágenes respetando el límite de velocidad."""
    log_section("FASE 2 — Descarga de imágenes")

    total   = len(images)
    ok      = 0
    skipped = 0
    failed  = 0

    items = list(images.items())
    for i, (media_id, ns) in enumerate(items, 1):
        dest = media_id_to_path(media_id, ns)

        log.info(f"[DESCARGA] [{i}/{total}] {media_id}")

        already_exists = dest.exists() and dest.stat().st_size > 0
        success = download_image(media_id, dest)

        if success and already_exists:
            skipped += 1
        elif success:
            ok += 1
        else:
            failed += 1

        # Límite de velocidad solo si realmente hubo descarga (no skip)
        if not already_exists and i < total:
            delay = random.uniform(DELAY_MIN, DELAY_MAX)
            rate  = 60 / delay
            log.info(f"  [PAUSA]    {delay:.1f}s  (≈ {rate:.1f} img/min — límite < 15)")
            time.sleep(delay)

    log.info("")
    log.info(f"[DESCARGA] ════════════════════════════════════")
    log.info(f"[DESCARGA] Total imágenes  : {total}")
    log.info(f"[DESCARGA] Descargadas     : {ok}")
    log.info(f"[DESCARGA] Ya existían     : {skipped}")
    log.info(f"[DESCARGA] Fallidas        : {failed}")
    log.info(f"[DESCARGA] Guardadas en    : raw/{{en,zh}}/images/")
    log.info(f"[DESCARGA] Log completo    : {LOG_FILE}")
    log.info(f"[DESCARGA] ════════════════════════════════════")

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    log_section("DESCARGADOR DE IMÁGENES — wiki.astercc.org")
    log.info(f"  Directorio raw : {RAW_DIR.resolve()}")
    log.info(f"  Namespaces     : {NAMESPACES}")
    log.info(f"  Límite         : < 15 imágenes/min ({DELAY_MIN}–{DELAY_MAX}s entre descargas)")

    images = analyze_files()

    if not images:
        log.info("[MAIN] No se encontraron imágenes para descargar. Fin.")
        return

    download_all(images)
    log.info("[MAIN] Proceso completado.")


if __name__ == "__main__":
    main()
