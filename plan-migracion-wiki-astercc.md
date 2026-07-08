# Plan de Trabajo: Migración y Reescritura del Wiki AsterCC en Español

**Objetivo:** Consolidar la documentación EN + ZH del wiki.astercc.org, reescribirla en español con énfasis en funcionalidad, buenas prácticas de documentación técnica, y publicarla en MkDocs sobre servidor local.

**Fecha:** 2026-07-02  
**Estado:** v4 — estructura basada en inventario real + buenas prácticas de IA (Information Architecture)

---

## Prerequisito único

El único paso que requiere acción externa es entregar la carpeta `data/pages/` exportada del servidor DokuWiki. Esta carpeta contiene todos los archivos `.txt` del wiki en inglés y chino. Una vez entregada, el resto del proceso lo ejecuta Claude sin intervención.

> Las imágenes se descargan aparte mediante `scraper/download_images.py`, con rate limit < 15 img/min.

---

## Principios de diseño de la documentación

Estos principios guían toda la Fase 4 (redacción) y no requieren validación — son criterios de calidad aplicados de forma consistente.

### 1. Estructura interna por artículo (inspirado en Diátaxis)
Cada artículo de módulo responde, en este orden, y con encabezados propios cuando el contenido lo amerita:
1. **Qué es** — explicación breve del propósito (1–2 párrafos).
2. **Cómo se configura / cómo se usa** — pasos numerados, orientados a tarea.
3. **Referencia rápida** — tabla de campos/parámetros si el módulo tiene configuración compleja. Se omite en artículos simples.

Esto evita que alguien buscando un parámetro puntual tenga que leer un tutorial completo.

### 2. Convención de nombres de página
- Artículos de tarea → verbo en infinitivo: *"Configurar IVR"*, *"Instalar desde USB"*.
- Artículos de referencia/concepto → sustantivo: *"Arquitectura general"*, *"Campos de campaña"*.

### 3. Jerarquía plana (máximo 3 niveles)
El contenido original en ZH llega a 4 niveles de profundidad (`módulos:pbx_avanzado:música_en_espera`). En la nueva estructura, el nivel 4 se convierte en artículos dentro de una página de índice de nivel 3, no en más anidación de navegación.

### 4. Contenido desactualizado — marcar, no borrar
El wiki no se actualiza desde 2018. En vez de omitir contenido dudoso silenciosamente, se marca con un aviso:
```markdown
!!! warning "Puede estar desactualizado"
    Este procedimiento proviene de la documentación original (2018) y no ha sido validado contra la versión actual.
```

### 5. Separar preguntas conceptuales de solución de errores
Las FAQ mezclan dos intenciones de búsqueda distintas. Se dividen en dos secciones (ver estructura abajo).

### 6. Glosario como fuente única de terminología
Un término técnico se traduce una sola vez y se reutiliza igual en todo el wiki (ej. "cola" para *queue*, no alternar con "fila").

### 7. Entradas por rol, no jerarquías paralelas
La portada ofrece rutas de entrada (Administrador / Agente / Desarrollador) que enlazan a subconjuntos de la misma estructura — no se duplica contenido para cada rol.

### 8. Front matter obligatorio en todo artículo
Todo archivo `.md` en `docs/` inicia con front matter YAML. Esquema fijo:

```yaml
---
title: "Configurar IVR"
resumen: "Cómo crear y editar un menú de voz (IVR) para enrutar llamadas entrantes."
seccion: "4.1 PBX y telefonía"
tipo: tutorial          # tutorial | guia | referencia | concepto | faq | troubleshooting
nivel: intermedio       # basico | intermedio | avanzado
roles: [administrador]  # administrador | agente | desarrollador
fuente: zh              # zh | en | zh+en
obsoleto: false         # true si el contenido tiene el aviso de la sección 4
relacionados:
  - configurar-colas
  - configurar-rutas-entrantes
---
```

Campos y su uso:
- `title` / `resumen` — se muestran en tarjetas de índice y en resultados de búsqueda.
- `seccion` — trazabilidad hacia la estructura del plan; permite regenerar la nav de `mkdocs.yml` desde el contenido si hace falta.
- `tipo` — habilita filtrar/etiquetar visualmente por modo de documentación (Diátaxis).
- `nivel` y `roles` — alimentan las rutas de entrada de la portada (principio 7).
- `fuente` — trazabilidad de dónde vino el contenido, útil si hay que re-verificar contra el original.
- `obsoleto` — si es `true`, el artículo lleva el admonition del principio 4; permite auditar cuántos artículos quedaron marcados.
- `relacionados` — slugs de otros artículos; alimenta una sección "Ver también" automática vía plugin.

`mkdocs.yml` habilita `mkdocs-material` con `plugins: [search, tags]` y el plugin de metadata para leer este front matter (`meta` / `awesome-pages` según disponibilidad al momento de la Fase 3).

---

## Estructura del proyecto generado

```
wiki-astercc/
├── raw/
│   ├── en/                # Páginas originales en inglés (.txt) + images/
│   └── zh/                # Páginas originales en chino (.txt) + images/
├── docs/                  # Contenido final en español (.md) — input de MkDocs
│   └── glosario.md
├── inventario.md          # Generado automáticamente en Fase 2
├── mkdocs.yml              # Configuración de MkDocs
└── scraper/                # Proyecto Scrapy + descargador de imágenes
```

---

## Fases del proceso

### Fase 1 — Organización del contenido raw
**Estado:** Completa.

Páginas y metadatos organizados en `raw/en/` y `raw/zh/` vía spider Scrapy. Imágenes descargadas por separado en `raw/{ns}/images/`.

---

### Fase 2 — Inventario y mapeo a la nueva estructura
**Ejecuta:** Claude

1. Cruzar páginas de `raw/en/` y `raw/zh/` por equivalente.
2. Clasificar: `solo_ZH`, `solo_EN`, `ambos`, `obsoleto`.
3. **Mapear cada página a su ubicación en la nueva estructura de secciones** (ver abajo) — este mapeo reemplaza la asignación genérica de prioridad por sección, y se basa en el contenido real descubierto, no en una estructura asumida de antemano.
4. Marcar páginas cuyo contenido amerita el aviso de "puede estar desactualizado".
5. Generar `inventario.md` con: página origen, idioma(s), destino en la nueva estructura, estado (`pendiente` / `completo`), flag de obsolescencia.

**Output:** `inventario.md` con 100% de páginas catalogadas y mapeadas a la nueva IA.

**Estado:** Completa. Generado por `scraper/build_inventory.py`.
- 1,068 páginas catalogadas (441 EN + 627 ZH), 0 pendientes de revisión de mapeo.
- Se descubrió un décimo grupo dentro de "Módulos del sistema" (ver sección 4.10 más abajo).
- Se identificaron las páginas fuente del Glosario: `en/others/glossary.txt` y `zh/其他/名词解释.txt`.

---

### Fase 3 — Setup de MkDocs
**Ejecuta:** Claude

1. Instalar MkDocs + Material Theme.
2. Configurar `mkdocs.yml`:
   - Navegación según la nueva estructura (abajo).
   - Plugin de búsqueda con soporte de español (stemming).
   - Tema Material con modo claro/oscuro, breadcrumbs, botón "editar página" deshabilitado (uso local).
   - Plugins para leer el front matter (tags, metadata) y renderizar "Ver también" desde `relacionados`.
3. Crear placeholders para todas las páginas de la estructura, incluida `glosario.md`.
4. Crear la portada (`index.md`) con las 3 rutas de entrada por rol.
5. Verificar que `mkdocs serve` levanta sin errores.

**Output:** MkDocs corriendo localmente con navegación completa y portada funcional.

---

### Fase 4 — Traducción y reescritura de contenido
**Ejecuta:** Claude

**Estrategia por fuente:** (sin cambios respecto a v3)

| Tipo de artículo | Fuente principal | Acción |
|---|---|---|
| Instalación / setup | ZH (más completo) | Traducir ZH → ES, enriquecer con EN |
| Módulos | ZH + EN | Combinar ambos, reescribir en ES |
| Casos de uso | ZH (exclusivo) | Traducir ZH → ES |
| FAQ / Troubleshooting | ZH + EN | Unificar y reescribir, separando por intención |
| Desarrollo | EN + ZH | Traducir y consolidar |

**Flujo por artículo:**
1. Leer fuente(s) según el inventario.
2. Aplicar estructura interna (Qué es → Cómo se usa → Referencia rápida).
3. Insertar imágenes ya descargadas con ruta relativa correcta.
4. Añadir aviso de obsolescencia si el inventario lo marcó.
5. Usar terminología del glosario; si aparece un término nuevo, añadirlo al glosario primero.
6. Escribir el `.md`, marcar `completo` en el inventario.

**Orden de trabajo (MVP primero):**
1. Glosario + Secciones 1–3 (Introducción, Instalación, Primeros pasos) + portada con rutas por rol
2. Sección 4 (Módulos)
3. Sección 5 (Casos de uso)
4. Secciones 6–9 (Administración avanzada, Desarrollo, FAQ/Troubleshooting, Changelog)

---

### Fase 5 — Verificación final
**Ejecuta:** Claude

1. Confirmar 100% de artículos `completo` en el inventario.
2. `mkdocs serve` sin enlaces rotos ni imágenes faltantes.
3. Verificar consistencia terminológica contra el glosario (grep de términos alternativos conocidos).
4. Confirmar que ningún nivel de navegación supera 3 niveles de profundidad.

---

## Nueva estructura de secciones

```
Portada (rutas por rol: Administrador / Agente / Desarrollador)

1. Introducción a AsterCC
   1.1 ¿Qué es AsterCC?
   1.2 Funcionalidades del sistema
   1.3 Arquitectura general
   1.4 Demo en línea

2. Instalación y configuración inicial
   2.1 Requisitos del sistema
   2.2 Descarga e instalación (ISO / manual)
   2.3 Instalación desde USB (AsterCC Box)
   2.4 Configuración post-instalación
   2.5 Licencias y errores comunes de inicio

3. Primeros pasos
   3.1 Guía rápida para administradores
   3.2 Guía rápida para agentes
   3.3 Recorrido por la interfaz

4. Módulos del sistema                          ← reestructurado según inventario real
   4.1 PBX y telefonía
       (troncales, extensiones, colas, rutas entrantes/salientes, IVR,
        música en espera, grupos de timbrado, buzón de voz)
   4.2 Marcador y campañas
       (dialer, marcación predictiva, campañas outbound)
   4.3 Cuentas, equipos y permisos
       (usuarios, roles, equipos, permisos, estructura de cuenta AsterCC)
   4.4 Tarifas y facturación
       (tarifas por equipo/extensión/sistema, facturación)
   4.5 Encuestas y cuestionarios
   4.6 Base de conocimiento y órdenes de trabajo (Work Orders)
   4.7 Plataforma de trabajo del agente
       (softphone, panel de llamadas, panel de correo/SMS, mapa)
   4.8 Reportes, estadísticas y financiero
   4.9 Oficina virtual / BPO
   4.10 Atención al cliente, mensajería y e-commerce   ← añadido en Fase 2
       (gestión de clientes, servicio entrante, mensajería masiva, WeChat, fax, e-commerce)

5. Casos de uso y soluciones
   5.1 Call center de atención al cliente (inbound)
   5.2 Marketing outbound / televentas
   5.3 E-commerce
   5.4 Oficina virtual
   5.5 Marcación predictiva
   5.6 Casos técnicos avanzados (integraciones, IVR con webservice, IMS, etc.)

6. Administración avanzada
   6.1 Configuración de Asterisk AMI
   6.2 OpenVPN
   6.3 APC (caché de PHP)
   6.4 Mailman / correo saliente

7. Guía de desarrollo y customización
   7.1 API y AMI
   7.2 Guía para desarrolladores

8. Preguntas frecuentes (FAQ)                   ← conceptuales

9. Solución de problemas                        ← nueva sección, errores específicos

10. Historial de versiones (Change Log)

Glosario                                        ← nueva página de referencia
```

> La sección 4 se ajustará con precisión exacta durante la Fase 2, una vez el inventario confirme la totalidad de sub-namespaces reales. Los 9 grupos arriba son la mejor aproximación actual basada en el contenido ya scrapeado.

---

## Criterio de artículo completo

Un artículo se cierra automáticamente cuando cumple:
1. Tiene front matter completo según el esquema fijo (principio 8).
2. Sigue la estructura interna (Qué es → Cómo se usa → Referencia rápida si aplica).
3. Tiene al menos un ejemplo concreto (comando, configuración o flujo paso a paso).
4. Usa terminología consistente con el glosario.
5. Incluye aviso de obsolescencia si el inventario lo marcó (y `obsoleto: true` en el front matter).
6. Está escrito en el archivo `.md` correspondiente en `docs/`, con el nombre de página siguiendo la convención (verbo para tareas, sustantivo para referencia).

---

## Estimación de esfuerzo

| Fase | Esfuerzo estimado |
|---|---|
| Fase 1 — Organización | Completa |
| Fase 2 — Inventario + mapeo a nueva IA | 30–45 min |
| Fase 3 — Setup MkDocs (con portada y glosario) | 30–45 min |
| Fase 4 — Contenido | 6–12 horas (según cantidad de artículos, incrementado por la granularidad añadida) |
| Fase 5 — Verificación | 20–30 min |

---

## Hitos

| Hito | Entregable | Estado |
|---|---|---|
| M1 | `inventario.md` generado y mapeado a la nueva estructura | ✅ Completo |
| M2 | MkDocs corriendo con portada, rutas por rol y glosario inicial | ✅ Completo |
| M3 | Secciones 1–3 escritas en español (MVP navegable) | ✅ Completo |
| M4 | Sección 4 (Módulos, 10 grupos) completa | ✅ Completo |
| M5 | Wiki completo v1.0 — todas las secciones con contenido | ✅ Completo |

**M3 completado el 2026-07-08.** Contenido publicado en `docs/`: Glosario (14 términos), Introducción (4 artículos), Instalación (5 artículos), Primeros pasos (3 artículos). Todos con front matter completo, fuentes citadas, y avisos de obsolescencia donde aplica (demo en línea, instalación por USB). Build `mkdocs build --strict` sin errores.

**M4 completado el 2026-07-08.** Los 10 artículos de Módulos del sistema están escritos con contenido real: PBX y telefonía, Marcador y campañas, Cuentas/equipos/permisos, Tarifas y facturación, Encuestas, Base de conocimiento y Work Orders, Plataforma del agente (referencia completa), Reportes/estadísticas/financiero, Oficina virtual/BPO, y Atención al cliente/mensajería/e-commerce. Enlaces cruzados entre módulos y hacia el glosario verificados. Build `mkdocs build --strict` sin errores.

**M5 completado el 2026-07-08.** Wiki v1.0 completo — 45 artículos con contenido real en `docs/`:
- **Sección 5 (Casos de uso, 6 artículos):** atención al cliente inbound, marketing outbound, e-commerce, oficina virtual, marcación predictiva, casos técnicos avanzados (ASR en IVR, troncal IMS).
- **Sección 6 (Administración avanzada, 4 artículos):** Asterisk AMI, OpenVPN, APC, Mailman — estos tres últimos marcados `obsoleto: true` con nota de qué los reemplaza en la instalación actual (Rocky 9/PHP 7.4).
- **Sección 7 (Desarrollo, 2 artículos):** API HTTP de acciones (`asterccinterfaces`) y guía de integración por pantalla emergente vía eventos JS.
- **Sección 8 (FAQ):** 5 preguntas conceptuales (diferencias cuenta/agente/extensión, login vs check-in, niveles de tarifa, modos DTMF, versiones).
- **Sección 9 (Solución de problemas):** 7 síntomas específicos con solución, indexados por error.
- **Sección 10 (Changelog):** parche de seguridad de login destacado (crítico para sistemas expuestos a internet) + tabla resumen de versiones principales.

Build final `mkdocs build --strict` sin errores — 0 enlaces rotos, 0 anchors inválidos, 0 placeholders sin completar en las 45 páginas de `docs/`.

---

*Elaborado con Claude — v6 — 2026-07-08*
