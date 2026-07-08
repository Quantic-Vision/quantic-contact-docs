"""
Fase 3 — Genera los placeholders de docs/ según la estructura del plan,
cada uno con el front matter obligatorio (ver CLAUDE.md / plan v4).

Ejecutar desde la raíz del proyecto:
    .venv\\Scripts\\python scaffold_docs.py
"""

from pathlib import Path

DOCS = Path("docs")

# (ruta, title, resumen, seccion, tipo, nivel, roles, es_indice)
PAGES = [
    # ── Introducción ────────────────────────────────────────────────────────
    ("introduccion/index.md", "Introducción a AsterCC", "Panorama general de qué es AsterCC y cómo empezar a explorar esta sección.", "1. Introducción a AsterCC", "concepto", "basico", ["administrador", "agente", "desarrollador"], True),
    ("introduccion/que-es-astercc.md", "¿Qué es AsterCC?", "Descripción general de AsterCC como plataforma de call center basada en Asterisk.", "1.1 ¿Qué es AsterCC?", "concepto", "basico", ["administrador", "agente", "desarrollador"], False),
    ("introduccion/funcionalidades.md", "Funcionalidades del sistema", "Lista de las funcionalidades principales que ofrece AsterCC.", "1.2 Funcionalidades del sistema", "referencia", "basico", ["administrador", "agente"], False),
    ("introduccion/arquitectura-general.md", "Arquitectura general", "Cómo están organizados los componentes técnicos de AsterCC.", "1.3 Arquitectura general", "concepto", "avanzado", ["administrador", "desarrollador"], False),
    ("introduccion/demo-en-linea.md", "Demo en línea", "Cómo acceder a la demo pública de AsterCC.", "1.4 Demo en línea", "guia", "basico", ["administrador", "agente"], False),

    # ── Instalación ──────────────────────────────────────────────────────────
    ("instalacion/index.md", "Instalación y configuración inicial", "Qué necesitas antes de instalar AsterCC y cómo está organizada esta sección.", "2. Instalación y configuración inicial", "concepto", "basico", ["administrador"], True),
    ("instalacion/requisitos.md", "Requisitos del sistema", "Requisitos de hardware y software para instalar AsterCC.", "2.1 Requisitos del sistema", "referencia", "basico", ["administrador"], False),
    ("instalacion/descarga-e-instalacion.md", "Descargar e instalar AsterCC", "Cómo descargar la ISO e instalar AsterCC manualmente.", "2.2 Descarga e instalación (ISO / manual)", "tutorial", "basico", ["administrador"], False),
    ("instalacion/instalar-desde-usb.md", "Instalar desde USB (AsterCC Box)", "Cómo instalar AsterCC Box usando una memoria USB booteable.", "2.3 Instalación desde USB (AsterCC Box)", "tutorial", "intermedio", ["administrador"], False),
    ("instalacion/configuracion-post-instalacion.md", "Configurar AsterCC después de instalar", "Pasos de configuración inicial recomendados tras la instalación.", "2.4 Configuración post-instalación", "tutorial", "intermedio", ["administrador"], False),
    ("instalacion/licencias-y-errores-comunes.md", "Licencias y errores comunes de inicio", "Cómo activar la licencia y resolver errores frecuentes al arrancar AsterCC.", "2.5 Licencias y errores comunes de inicio", "troubleshooting", "intermedio", ["administrador"], False),

    # ── Primeros pasos ───────────────────────────────────────────────────────
    ("primeros-pasos/index.md", "Primeros pasos", "Guías rápidas para empezar a usar AsterCC según tu rol.", "3. Primeros pasos", "concepto", "basico", ["administrador", "agente"], True),
    ("primeros-pasos/guia-administradores.md", "Guía rápida para administradores", "Primeros pasos recomendados para un administrador nuevo en AsterCC.", "3.1 Guía rápida para administradores", "tutorial", "basico", ["administrador"], False),
    ("primeros-pasos/guia-agentes.md", "Guía rápida para agentes", "Primeros pasos recomendados para un agente nuevo en AsterCC.", "3.2 Guía rápida para agentes", "tutorial", "basico", ["agente"], False),
    ("primeros-pasos/recorrido-interfaz.md", "Recorrido por la interfaz", "Tour por los paneles principales de la interfaz de AsterCC.", "3.3 Recorrido por la interfaz", "tutorial", "basico", ["administrador", "agente"], False),

    # ── Módulos ──────────────────────────────────────────────────────────────
    ("modulos/index.md", "Módulos del sistema", "Panorama de los módulos funcionales de AsterCC y cómo están agrupados.", "4. Módulos del sistema", "concepto", "basico", ["administrador"], True),
    ("modulos/pbx-y-telefonia.md", "PBX y telefonía", "Troncales, extensiones, colas, rutas, IVR y demás configuración telefónica.", "4.1 PBX y telefonía", "guia", "intermedio", ["administrador"], False),
    ("modulos/marcador-y-campanas.md", "Marcador y campañas", "Configuración del dialer, marcación predictiva y campañas outbound.", "4.2 Marcador y campañas", "guia", "intermedio", ["administrador"], False),
    ("modulos/cuentas-equipos-permisos.md", "Cuentas, equipos y permisos", "Gestión de usuarios, roles, equipos y estructura de cuenta en AsterCC.", "4.3 Cuentas, equipos y permisos", "guia", "intermedio", ["administrador"], False),
    ("modulos/tarifas-y-facturacion.md", "Tarifas y facturación", "Configuración de tarifas por equipo, extensión o sistema.", "4.4 Tarifas y facturación", "guia", "intermedio", ["administrador"], False),
    ("modulos/encuestas.md", "Encuestas y cuestionarios", "Creación y gestión de encuestas para campañas o servicio al cliente.", "4.5 Encuestas y cuestionarios", "guia", "intermedio", ["administrador"], False),
    ("modulos/base-conocimiento-work-orders.md", "Base de conocimiento y Work Orders", "Gestión de artículos de conocimiento y órdenes de trabajo.", "4.6 Base de conocimiento y Work Orders", "guia", "intermedio", ["administrador", "agente"], False),
    ("modulos/plataforma-del-agente.md", "Plataforma de trabajo del agente", "Softphone, panel de llamadas, correo/SMS y mapa en la plataforma del agente.", "4.7 Plataforma de trabajo del agente", "guia", "basico", ["agente"], False),
    ("modulos/reportes-y-estadisticas.md", "Reportes, estadísticas y financiero", "Reportes de desempeño, estadísticas en tiempo real y datos financieros.", "4.8 Reportes, estadísticas y financiero", "referencia", "intermedio", ["administrador"], False),
    ("modulos/oficina-virtual-bpo.md", "Oficina virtual / BPO", "Configuración de oficina virtual y operación tipo BPO.", "4.9 Oficina virtual / BPO", "guia", "intermedio", ["administrador"], False),
    ("modulos/atencion-cliente-mensajeria-ecommerce.md", "Atención al cliente, mensajería y e-commerce", "Gestión de clientes, mensajería masiva, WeChat, fax y e-commerce.", "4.10 Atención al cliente, mensajería y e-commerce", "guia", "intermedio", ["administrador", "agente"], False),

    # ── Casos de uso ─────────────────────────────────────────────────────────
    ("casos-de-uso/index.md", "Casos de uso y soluciones", "Escenarios reales de uso de AsterCC según el tipo de negocio.", "5. Casos de uso y soluciones", "concepto", "basico", ["administrador"], True),
    ("casos-de-uso/call-center-inbound.md", "Call center de atención al cliente (inbound)", "Cómo montar un call center de atención al cliente entrante.", "5.1 Call center de atención al cliente (inbound)", "guia", "intermedio", ["administrador"], False),
    ("casos-de-uso/marketing-outbound.md", "Marketing outbound / televentas", "Cómo montar una operación de televenta o marketing saliente.", "5.2 Marketing outbound / televentas", "guia", "intermedio", ["administrador"], False),
    ("casos-de-uso/e-commerce.md", "E-commerce", "Cómo integrar AsterCC en una operación de e-commerce.", "5.3 E-commerce", "guia", "intermedio", ["administrador"], False),
    ("casos-de-uso/oficina-virtual.md", "Oficina virtual", "Cómo ofrecer servicios de oficina virtual con AsterCC.", "5.4 Oficina virtual", "guia", "intermedio", ["administrador"], False),
    ("casos-de-uso/marcacion-predictiva.md", "Marcación predictiva", "Cómo configurar y operar campañas de marcación predictiva.", "5.5 Marcación predictiva", "guia", "avanzado", ["administrador"], False),
    ("casos-de-uso/casos-tecnicos-avanzados.md", "Casos técnicos avanzados", "Integraciones avanzadas: IVR con webservice, IMS y otros casos técnicos.", "5.6 Casos técnicos avanzados", "guia", "avanzado", ["administrador", "desarrollador"], False),

    # ── Administración avanzada ──────────────────────────────────────────────
    ("administracion/index.md", "Administración avanzada", "Configuración avanzada de infraestructura y servicios de soporte.", "6. Administración avanzada", "concepto", "avanzado", ["administrador"], True),
    ("administracion/asterisk-ami.md", "Configurar Asterisk AMI", "Cómo configurar el Asterisk Manager Interface (AMI).", "6.1 Configuración de Asterisk AMI", "tutorial", "avanzado", ["administrador", "desarrollador"], False),
    ("administracion/openvpn.md", "Configurar OpenVPN", "Cómo configurar OpenVPN para acceso remoto seguro.", "6.2 OpenVPN", "tutorial", "avanzado", ["administrador"], False),
    ("administracion/apc.md", "Configurar APC (caché de PHP)", "Cómo instalar y configurar APC para acelerar PHP.", "6.3 APC (caché de PHP)", "tutorial", "avanzado", ["administrador"], False),
    ("administracion/mailman.md", "Configurar Mailman / correo saliente", "Cómo instalar y configurar Mailman para correo saliente.", "6.4 Mailman / correo saliente", "tutorial", "avanzado", ["administrador"], False),

    # ── Desarrollo ───────────────────────────────────────────────────────────
    ("desarrollo/index.md", "Guía de desarrollo y customización", "Recursos para desarrolladores que quieran extender AsterCC.", "7. Guía de desarrollo y customización", "concepto", "avanzado", ["desarrollador"], True),
    ("desarrollo/api-y-ami.md", "API y AMI", "Referencia de la API y del Asterisk Manager Interface para integraciones.", "7.1 API y AMI", "referencia", "avanzado", ["desarrollador"], False),
    ("desarrollo/guia-desarrolladores.md", "Guía para desarrolladores", "Cómo extender o personalizar AsterCC a nivel de código.", "7.2 Guía para desarrolladores", "guia", "avanzado", ["desarrollador"], False),

    # ── FAQ / Troubleshooting / Changelog ────────────────────────────────────
    ("faq/index.md", "Preguntas frecuentes", "Preguntas conceptuales frecuentes sobre AsterCC.", "8. Preguntas frecuentes (FAQ)", "faq", "basico", ["administrador", "agente"], True),
    ("troubleshooting/index.md", "Solución de problemas", "Errores específicos y cómo resolverlos, indexados por el mensaje de error.", "9. Solución de problemas", "troubleshooting", "intermedio", ["administrador"], True),
    ("changelog/index.md", "Historial de versiones", "Registro de cambios por versión de AsterCC.", "10. Historial de versiones (Change Log)", "referencia", "basico", ["administrador", "desarrollador"], True),

    # ── Glosario ─────────────────────────────────────────────────────────────
    ("glosario.md", "Glosario", "Términos técnicos usados en la documentación de AsterCC, con su traducción estándar al español.", "Glosario", "referencia", "basico", ["administrador", "agente", "desarrollador"], True),
]


def front_matter(title, resumen, seccion, tipo, nivel, roles, fuente="pendiente", obsoleto=False):
    roles_str = ", ".join(roles)
    return f"""---
title: "{title}"
resumen: "{resumen}"
seccion: "{seccion}"
tipo: {tipo}
nivel: {nivel}
roles: [{roles_str}]
fuente: {fuente}
obsoleto: {str(obsoleto).lower()}
relacionados: []
---
"""


def body_for(title, resumen, es_indice):
    if es_indice:
        return f"""# {title}

{resumen}

> Página índice generada en Fase 3. El contenido y los enlaces a los artículos de esta sección se completan en Fase 4.
"""
    return f"""# {title}

{resumen}

> Placeholder generado en Fase 3. Contenido pendiente de redacción en Fase 4.

## Qué es

_Pendiente._

## Cómo se usa

_Pendiente._

## Referencia rápida

_Pendiente (si aplica)._
"""


def main():
    created = 0
    for rel_path, title, resumen, seccion, tipo, nivel, roles, es_indice in PAGES:
        path = DOCS / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        content = front_matter(title, resumen, seccion, tipo, nivel, roles) + "\n" + body_for(title, resumen, es_indice)
        path.write_text(content, encoding="utf-8")
        created += 1
    print(f"Placeholders creados: {created}")


if __name__ == "__main__":
    main()
