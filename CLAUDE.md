# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Objetivo del proyecto

Migración y reescritura del wiki de AsterCC (sistema de call center basado en Asterisk) al español. El wiki original está en DokuWiki con contenido en inglés (`en`) y chino (`zh`). El destino es un wiki local en español publicado con MkDocs.

El proceso es completamente automatizado — Luis no hace ningún paso manual.

---

## Arquitectura general

```
Documentación AsterCC/
├── CLAUDE.md                        ← este archivo
├── plan-migracion-wiki-astercc.md   ← plan de trabajo vivo (actualizar si cambia el proceso)
├── raw/                             ← contenido scrapeado del wiki original
│   ├── en/                          ← páginas en inglés (.txt, formato DokuWiki)
│   │   └── images/                  ← imágenes descargadas referenciadas desde EN
│   ├── zh/                          ← páginas en chino (.txt, formato DokuWiki)
│   │   └── images/                  ← imágenes descargadas referenciadas desde ZH
│   └── metadata.json                ← inventario generado por el spider
├── docs/                            ← contenido final en español (.md) — input de MkDocs
├── mkdocs.yml                       ← configuración de MkDocs (a crear)
└── scraper/                         ← proyecto Scrapy + scripts de apoyo
    ├── scrapy.cfg
    ├── .venv/                       ← entorno virtual Python (Scrapy 2.16)
    ├── .httpcache/                  ← caché HTTP de Scrapy (permite reanudar)
    ├── .scrapy_job/                 ← estado del spider (permite reanudar)
    ├── scraper.log                  ← log del spider
    ├── images.log                   ← log del descargador de imágenes
    ├── download_images.py           ← script standalone para descargar imágenes
    └── astercc/
        ├── settings.py              ← configuración de Scrapy
        ├── items.py                 ← WikiPageItem
        ├── pipelines.py             ← guarda páginas en raw/{namespace}/
        ├── extensions.py            ← DualLogExtension (log a consola + archivo)
        └── spiders/
            └── wiki_spider.py       ← spider principal
```

---

## Comandos principales

Todos los comandos se ejecutan desde `scraper/` con el venv activado:

```powershell
cd "....\Documentación AsterCC\scraper"
.\.venv\Scripts\activate
```

### Scrapear el wiki (Fase 1)
```powershell
scrapy crawl wiki
```

### Reanudar tras interrupción
```powershell
scrapy crawl wiki          # usa .httpcache + .scrapy_job automáticamente
```

### Forzar re-descarga ignorando caché
```powershell
scrapy crawl wiki -s HTTPCACHE_ENABLED=False
```

### Limpiar y empezar desde cero
```powershell
Remove-Item -Recurse -Force .httpcache, .scrapy_job, ..\raw -ErrorAction SilentlyContinue
scrapy crawl wiki
```

### Descargar imágenes referenciadas (después del scraping)
```powershell
.\.venv\Scripts\python download_images.py
```

### Regenerar el inventario (Fase 2)
```powershell
.\.venv\Scripts\python build_inventory.py
```
Lee todo `raw/en/` y `raw/zh/`, mapea cada página a la nueva estructura y escribe `../inventario.md`. Re-ejecutar si se agregan/quitan páginas de `raw/`.

### Servir el wiki en local (después de generar docs/)
```powershell
cd ..
mkdocs serve
```

---

## Cómo funciona el spider

**Descubrimiento de páginas:** El spider navega el índice DokuWiki con el parámetro `idx=`. El sitemap XML devuelve 404 y XML-RPC está deshabilitado en el servidor.

- Sub-namespaces: `?id=start&idx=en%3Amodule_manual` → recursar
- Páginas: `?id=en:module_manual:pbx` → descargar raw

**Descarga de contenido:** Cada página se descarga como texto plano vía `?id=<page_id>&do=export_raw`. El formato es DokuWiki markup (no HTML).

**Rate limiting:** Scrapy AutoThrottle activo + `DOWNLOAD_DELAY=4.0` + `RANDOMIZE_DOWNLOAD_DELAY=True`. Una sola request concurrente.

**Resumibilidad:** `HTTPCACHE_ENABLED=True` (caché permanente en `.httpcache/`) + `JOBDIR=".scrapy_job"` (estado del spider).

**Paths de salida:** `raw/{namespace}/{sub/ruta}.txt`. El namespace se quita del path relativo para evitar duplicación (ej: `en:module_manual:pbx` → `raw/en/module_manual/pbx.txt`).

---

## Cómo funciona el descargador de imágenes

`download_images.py` es un script standalone (no Scrapy). Analiza todos los `.txt` en `raw/`, extrae referencias DokuWiki con el patrón:

```
{{:namespace:path:imagen.jpg?768|alt}}
```

URL de descarga: `https://wiki.astercc.org/lib/exe/fetch.php?media=namespace:path:imagen.jpg`

Destino: `raw/{namespace}/images/{path}/{imagen.jpg}`

Rate limit: entre 4.1 y 7.0 segundos entre descargas (< 15 img/min).

---

## Formato DokuWiki (raw)

Los archivos `.txt` descargados usan sintaxis DokuWiki. Las referencias más importantes al convertir a Markdown:

| DokuWiki | Markdown |
|---|---|
| `====== Título ======` | `# Título` |
| `===== Título =====` | `## Título` |
| `**negrita**` | `**negrita**` |
| `//cursiva//` | `*cursiva*` |
| `[[page_id\|texto]]` | `[texto](url)` |
| `{{:ns:img.jpg\|alt}}` | `![alt](../images/img.jpg)` |
| `<code>...</code>` | ` ```...``` ` |

---

## Estructura del wiki en español (MkDocs)

La estructura de secciones vive en `plan-migracion-wiki-astercc.md` (v4+) y se ajusta durante la Fase 2 contra el inventario real — no está fija de antemano. Orden de generación: Glosario + secciones 1–3 primero (MVP), luego 4–5, luego 6–10.

**Fuentes por tipo de artículo:**
- Instalación/setup → ZH (más completo), enriquecer con EN
- Módulos → ZH + EN combinados
- Casos de uso → ZH exclusivo
- FAQ / Solución de problemas → ZH + EN unificados, separados por intención de búsqueda

### Principios de redacción (obligatorios en Fase 4)

1. **Estructura interna por artículo:** Qué es → Cómo se usa → Referencia rápida (tabla de campos, solo si el módulo lo amerita).
2. **Convención de nombres:** verbo infinitivo para tareas ("Configurar IVR"), sustantivo para referencia/concepto ("Arquitectura general").
3. **Jerarquía máxima de 3 niveles** en `mkdocs.yml` — contenido de nivel 4+ del wiki original se convierte en artículos listados desde una página índice de nivel 3, no en más anidación de nav.
4. **Contenido desactualizado se marca, no se omite:** admonition `!!! warning "Puede estar desactualizado"` cuando el inventario lo flaggea (info de 2018 sin validar).
5. **Terminología centralizada en `docs/glosario.md`** — un término técnico se traduce una sola vez y se reutiliza igual en todo el wiki. Si aparece un término nuevo durante la redacción, se agrega al glosario antes de usarlo.
6. **Portada con rutas por rol** (Administrador / Agente / Desarrollador) — enlazan a subconjuntos de la misma estructura, sin duplicar contenido.
7. **Front matter YAML obligatorio** en todo `.md` de `docs/`:
   ```yaml
   ---
   title: "Configurar IVR"
   resumen: "Cómo crear y editar un menú de voz (IVR) para enrutar llamadas entrantes."
   seccion: "4.1 PBX y telefonía"
   tipo: tutorial          # tutorial | guia | referencia | concepto | faq | troubleshooting
   nivel: intermedio       # basico | intermedio | avanzado
   roles: [administrador]  # administrador | agente | desarrollador
   fuente: zh              # zh | en | zh+en
   obsoleto: false
   relacionados: [configurar-colas, configurar-rutas-entrantes]
   ---
   ```
   Nunca escribir un `.md` en `docs/` sin este bloque completo — es el criterio #1 de "artículo completo" en el plan.
8. **Citas de fuentes — lista explícita, sin comodines, formato de lista.** Cada artículo termina con:
   ```markdown
   ---

   ## Fuentes

   - `raw/zh/模块使用说明/pbx管理/分机管理.txt`
   - `raw/zh/模块使用说明/pbx高级管理/队列管理.txt`
   ```
   Reglas:
   - **Nunca usar comodines** (`*.txt`, rutas de carpeta sin archivo) — cada línea es un archivo individual que efectivamente se leyó.
   - Un archivo se cita si su contenido fue leído y usado — no basta con que "debería" estar cubierto por otro archivo similar.
   - Si un tema tiene equivalente en EN y en ZH pero solo se leyó uno, se cita solo el leído — no asumir que el otro dice lo mismo sin verificarlo.
   - Auditar cobertura real con `scraper/audit_coverage.py` (compara citas contra el listado completo de `raw/`, separado por idioma EN/ZH) — no confiar en estimaciones.

### Sección "Módulos del sistema" — mapeo por dominio funcional

No usa las categorías genéricas originales del wiki. Se agrupa por dominio real, confirmado en Fase 2 contra el inventario completo (`module_manual`/`模块使用说明` tienen ~26 sub-namespaces). Mapeo definitivo, codificado en `scraper/build_inventory.py` (`MODULE_MAP`):

| Grupo | Contenido |
|---|---|
| 4.1 PBX y telefonía | troncales, extensiones, colas, rutas, IVR, música en espera, timbrado, buzón de voz, administración avanzada de PBX |
| 4.2 Marcador y campañas | dialer, marcación predictiva, campañas outbound |
| 4.3 Cuentas, equipos y permisos | usuarios, roles, equipos, estructura de cuenta AsterCC |
| 4.4 Tarifas y facturación | tarifas por equipo/extensión/sistema |
| 4.5 Encuestas y cuestionarios | 问卷 (survey) |
| 4.6 Base de conocimiento y Work Orders | knowledgebase, work_order, 工单管理 |
| 4.7 Plataforma de trabajo del agente | softphone, panel de llamadas, correo/SMS, mapa, 坐席平台 |
| 4.8 Reportes, estadísticas y financiero | statistics, realtime, financiero, 报表 |
| 4.9 Oficina virtual / BPO | virtual_office, bpo, 虚拟呼叫中心 |
| 4.10 Atención al cliente, mensajería y e-commerce | customer, customerservice, message, e-commerce, WeChat (微信), fax (传真管理), mensajería masiva (群发信息管理) |

Grupo 4.10 se descubrió durante la Fase 2 — no estaba en el diseño original de 9 grupos; el contenido ZH-exclusivo de atención al cliente/mensajería no encajaba en ninguno de los otros 9.

Contenido operativo/administrativo (logs, configuración de sistema, gestión avanzada del call center) se mapea a la sección 6 "Administración avanzada", no a la sección 4.

**Glosario:** las páginas fuente son `raw/en/others/glossary.txt` y `raw/zh/其他/名词解释.txt` — leerlas primero al escribir `docs/glosario.md`.

Este mapeo se confirma/ajusta en Fase 2 contra el inventario definitivo — la tabla de arriba es la mejor aproximación con el contenido ya scrapeado.

---

## Restricciones conocidas del servidor

- El wiki (`wiki.astercc.org`) bloquea requests desde IPs externas (anti-DoS). Solo accesible desde la red local del usuario.
- XML-RPC deshabilitado (`501 Not Implemented`).
- Sitemap XML devuelve `404`.
- El índice navega exclusivamente por `?id=start&idx=<namespace>`.
