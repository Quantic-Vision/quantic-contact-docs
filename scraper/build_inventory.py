"""
Fase 2 — Construye inventario.md a partir del contenido en raw/en y raw/zh.

Mapea cada namespace descubierto a la nueva estructura de secciones del wiki
en español (ver plan-migracion-wiki-astercc.md v4/v5) y genera una tabla
de inventario agrupada por sección destino, lista para guiar la Fase 4.

Ejecutar desde scraper/:
    python build_inventory.py
"""

import re
from pathlib import Path
from collections import defaultdict

RAW_DIR = Path("../raw")
OUT_FILE = Path("../inventario.md")

# ─── MAPEO NAMESPACE → SECCIÓN DESTINO ─────────────────────────────────────────
# Clave: (idioma, namespace_top_level) → sección destino en el nuevo wiki.
# Para module_manual / 模块使用说明 se mapea por sub-namespace (segundo nivel).

NS_MAP = {
    ("en", "change_log"): "10. Historial de versiones",
    ("zh", "change_log"): "10. Historial de versiones",

    ("en", "download_and_install"): "2. Instalación y configuración inicial",
    ("zh", "下载和安装"): "2. Instalación y configuración inicial",
    ("en", "installation_guideline_and_setup"): "2. Instalación y configuración inicial",

    ("en", "custom_development_guide"): "7. Guía de desarrollo y customización",
    ("zh", "二次开发者指南"): "7. Guía de desarrollo y customización",

    ("en", "function"): "1.2 Funcionalidades del sistema",
    ("en", "regular_function_description_in_call_center"): "1.2 Funcionalidades del sistema",
    ("zh", "呼叫中心常用功能简介"): "1.2 Funcionalidades del sistema",

    ("en", "online_demo"): "1.4 Demo en línea",
    ("zh", "在线演示"): "1.4 Demo en línea",

    ("zh", "坐席工作平台"): "4.7 Plataforma de trabajo del agente",

    ("en", "real_case_guidance"): "5. Casos de uso y soluciones",
    ("zh", "实际案例指导"): "5. Casos de uso y soluciones",
    ("en", "use_case"): "5. Casos de uso y soluciones",
    ("zh", "用途和案例"): "5. Casos de uso y soluciones",
    ("zh", "解决方案"): "5. Casos de uso y soluciones",

    ("en", "faq"): "8. Preguntas frecuentes / 9. Solución de problemas",
    ("en", "questions_and_answers"): "8. Preguntas frecuentes / 9. Solución de problemas",
    ("zh", "常见问题及解答"): "8. Preguntas frecuentes / 9. Solución de problemas",

    ("zh", "报表"): "4.8 Reportes, estadísticas y financiero",

    ("en", "newbie"): "3. Primeros pasos",
    ("zh", "新手上路"): "3. Primeros pasos",

    ("zh", "界面简介"): "3.3 Recorrido por la interfaz",

    ("en", "how-to"): "6. Administración avanzada (revisar por tema)",

    ("en", "others"): "Otros (clasificar en Fase 4)",
    ("zh", "其他"): "Otros (clasificar en Fase 4)",
    ("zh", "历史文档"): "10. Historial de versiones (archivo histórico)",
}

# Páginas puntuales dentro de "others" / "其他" con destino claro (no genérico)
OTHERS_OVERRIDE = {
    "glossary": "Glosario",
    "名词解释": "Glosario",
    "asterisk_howtos": "6. Administración avanzada",
    "iaxmodem_and_hylafax": "4.10 Atención al cliente, mensajería y e-commerce",
    "contact": "Otros (clasificar en Fase 4)",
}

# Sub-namespaces de module_manual / 模块使用说明 → grupo de la sección 4
MODULE_MAP = {
    # PBX y telefonía
    "pbx": "4.1 PBX y telefonía",
    "pbx管理": "4.1 PBX y telefonía",
    "pbx高级管理": "4.1 PBX y telefonía",
    "ivr": "4.1 PBX y telefonía",
    "advanced": "6. Administración avanzada",
    "呼叫中心高级管理": "6. Administración avanzada",
    "call_center": "1.2 Funcionalidades del sistema",

    # Marcador y campañas
    "dialer": "4.2 Marcador y campañas",
    "预拨号": "4.2 Marcador y campañas",
    "campaign": "4.2 Marcador y campañas",
    "外呼营销": "4.2 Marcador y campañas",

    # Cuentas, equipos y permisos
    "user": "4.3 Cuentas, equipos y permisos",
    "账户和权限管理": "4.3 Cuentas, equipos y permisos",
    "system": "6. Administración avanzada",
    "system_modules": "6. Administración avanzada",
    "系统模块管理": "6. Administración avanzada",
    "系统设置": "6. Administración avanzada",
    "log": "6. Administración avanzada",
    "系统日志": "6. Administración avanzada",

    # Tarifas y facturación
    "rate": "4.4 Tarifas y facturación",
    "费率管理": "4.4 Tarifas y facturación",

    # Encuestas
    "survey": "4.5 Encuestas y cuestionarios",
    "问卷": "4.5 Encuestas y cuestionarios",

    # Base de conocimiento y Work Orders
    "knowledgebase": "4.6 Base de conocimiento y Work Orders",
    "知识库": "4.6 Base de conocimiento y Work Orders",
    "work_order": "4.6 Base de conocimiento y Work Orders",
    "工单管理": "4.6 Base de conocimiento y Work Orders",

    # Plataforma de trabajo del agente
    "agent_work_page": "4.7 Plataforma de trabajo del agente",
    "坐席平台": "4.7 Plataforma de trabajo del agente",

    # Reportes, estadísticas y financiero
    "statistics": "4.8 Reportes, estadísticas y financiero",
    "realtime": "4.8 Reportes, estadísticas y financiero",
    "报表和统计": "4.8 Reportes, estadísticas y financiero",
    "财务统计": "4.8 Reportes, estadísticas y financiero",
    "系统实时信息": "4.8 Reportes, estadísticas y financiero",

    # Oficina virtual / BPO
    "virtual_office": "4.9 Oficina virtual / BPO",
    "虚拟呼叫中心": "4.9 Oficina virtual / BPO",
    "bpo": "4.9 Oficina virtual / BPO",

    # Atención al cliente, mensajería y e-commerce (NUEVO — grupo 4.10)
    "customer": "4.10 Atención al cliente, mensajería y e-commerce",
    "customerservice": "4.10 Atención al cliente, mensajería y e-commerce",
    "呼入客服": "4.10 Atención al cliente, mensajería y e-commerce",
    "客户管理": "4.10 Atención al cliente, mensajería y e-commerce",
    "message": "4.10 Atención al cliente, mensajería y e-commerce",
    "群发信息管理": "4.10 Atención al cliente, mensajería y e-commerce",
    "微信": "4.10 Atención al cliente, mensajería y e-commerce",
    "传真管理": "4.10 Atención al cliente, mensajería y e-commerce",
    "e_commerce": "4.10 Atención al cliente, mensajería y e-commerce",
    "电子商务": "4.10 Atención al cliente, mensajería y e-commerce",

    # Estructura de cuenta / overview general de módulos
    "astercc_structure": "4.3 Cuentas, equipos y permisos",
    "astercc账户结构": "4.3 Cuentas, equipos y permisos",
    "基本模块": "4. Módulos del sistema",
}

# Páginas raíz sueltas (sin namespace) → sección destino, por nombre de archivo
ROOT_MAP = {
    "start": "1. Introducción a AsterCC",
    "work_order": "4.6 Base de conocimiento y Work Orders",
    "工单": "4.6 Base de conocimiento y Work Orders",
    "asterisk_ami_username_password": "6. Administración avanzada",
    "install_apc": "6. Administración avanzada",
    "install_astcc_mailman": "6. Administración avanzada",
    "openvpn": "6. Administración avanzada",
    "to_establish_an_outbound_program": "5. Casos de uso y soluciones",
    "why_i_get_can_not_found_license_file_when_start_astercc_daemons": "8. Preguntas frecuentes / 9. Solución de problemas",
    "astercc_call_center_quick_feature_list": "1.2 Funcionalidades del sistema",
    "使用u盘安装astercc-box": "2. Instalación y configuración inicial",
    "呼入客服": "4.10 Atención al cliente, mensajería y e-commerce",
    "呼叫中心系统功能列表": "1.2 Funcionalidades del sistema",
    "团队管理": "4.3 Cuentas, equipos y permisos",
    "外呼营销": "4.2 Marcador y campañas",
    "常见问题及解答": "8. Preguntas frecuentes / 9. Solución de problemas",
    "新手上路": "3. Primeros pasos",
    "模块使用说明": "4. Módulos del sistema",
    "电子商务": "4.10 Atención al cliente, mensajería y e-commerce",
    "界面简介": "3.3 Recorrido por la interfaz",
    "虚拟办公室": "4.9 Oficina virtual / BPO",
    "预拨号": "4.2 Marcador y campañas",
}

MODULE_NAMESPACE_NAMES = {"module_manual", "模块使用说明"}


def classify(lang: str, txt_path: Path) -> tuple[str, bool]:
    """
    Retorna (seccion_destino, requiere_revision).
    requiere_revision=True si no hubo match directo en los mapeos.
    """
    rel = txt_path.relative_to(RAW_DIR / lang)
    parts = rel.parts

    if len(parts) == 1:
        # Página suelta en la raíz del idioma
        slug = rel.stem
        if slug in ROOT_MAP:
            return ROOT_MAP[slug], False
        return "Otros (clasificar en Fase 4)", True

    top_ns = parts[0]

    if top_ns in ("others", "其他") and len(parts) == 2:
        slug = Path(parts[1]).stem
        if slug in OTHERS_OVERRIDE:
            return OTHERS_OVERRIDE[slug], False

    if top_ns in MODULE_NAMESPACE_NAMES:
        if len(parts) >= 3:
            # raw/{lang}/module_manual/{sub_ns}/{page}.txt
            sub_ns = parts[1]
        elif len(parts) == 2:
            # raw/{lang}/module_manual/{sub_ns}.txt  → página overview del submódulo
            sub_ns = Path(parts[1]).stem
        else:
            sub_ns = None

        if sub_ns == "start":
            # Portada del namespace module_manual completo
            return "4. Módulos del sistema", False
        if sub_ns and sub_ns in MODULE_MAP:
            return MODULE_MAP[sub_ns], False
        return "4. Módulos del sistema (sub-namespace sin mapear)", True

    key = (lang, top_ns)
    if key in NS_MAP:
        return NS_MAP[key], False

    return "Otros (clasificar en Fase 4)", True


def char_count(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return 0


def main():
    # sección → lista de (lang, rel_path, chars, revisar)
    by_section: dict[str, list] = defaultdict(list)
    totals = {"en": 0, "zh": 0}
    revisar_count = 0

    for lang in ("en", "zh"):
        lang_dir = RAW_DIR / lang
        if not lang_dir.exists():
            continue
        for txt_path in sorted(lang_dir.rglob("*.txt")):
            totals[lang] += 1
            seccion, revisar = classify(lang, txt_path)
            if revisar:
                revisar_count += 1
            chars = char_count(txt_path)
            rel = txt_path.relative_to(RAW_DIR)
            by_section[seccion].append((lang, str(rel), chars, revisar))

    # ─── Generar inventario.md ──────────────────────────────────────────────
    lines = []
    lines.append("# Inventario de contenido — Wiki AsterCC")
    lines.append("")
    lines.append("Generado automáticamente en Fase 2 a partir de `raw/en/` y `raw/zh/`.")
    lines.append("")
    lines.append(f"- Páginas EN: **{totals['en']}**")
    lines.append(f"- Páginas ZH: **{totals['zh']}**")
    lines.append(f"- Total: **{totals['en'] + totals['zh']}**")
    lines.append(f"- Requieren revisión de mapeo en Fase 4: **{revisar_count}**")
    lines.append("")
    lines.append("Estado de cada página: `pendiente` hasta que se escriba su artículo en `docs/`.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Orden de seccion: seguir el orden del plan, luego el resto alfabético
    section_order = [
        "Glosario",
        "1. Introducción a AsterCC",
        "1.2 Funcionalidades del sistema",
        "1.4 Demo en línea",
        "2. Instalación y configuración inicial",
        "3. Primeros pasos",
        "3.3 Recorrido por la interfaz",
        "4. Módulos del sistema",
        "4.1 PBX y telefonía",
        "4.2 Marcador y campañas",
        "4.3 Cuentas, equipos y permisos",
        "4.4 Tarifas y facturación",
        "4.5 Encuestas y cuestionarios",
        "4.6 Base de conocimiento y Work Orders",
        "4.7 Plataforma de trabajo del agente",
        "4.8 Reportes, estadísticas y financiero",
        "4.9 Oficina virtual / BPO",
        "4.10 Atención al cliente, mensajería y e-commerce",
        "5. Casos de uso y soluciones",
        "6. Administración avanzada",
        "6. Administración avanzada (revisar por tema)",
        "7. Guía de desarrollo y customización",
        "8. Preguntas frecuentes / 9. Solución de problemas",
        "10. Historial de versiones",
        "10. Historial de versiones (archivo histórico)",
        "4. Módulos del sistema (sub-namespace sin mapear)",
        "Otros (clasificar en Fase 4)",
    ]
    remaining = sorted(set(by_section.keys()) - set(section_order))
    ordered_sections = [s for s in section_order if s in by_section] + remaining

    for seccion in ordered_sections:
        items = by_section[seccion]
        en_count = sum(1 for i in items if i[0] == "en")
        zh_count = sum(1 for i in items if i[0] == "zh")
        lines.append(f"## {seccion}")
        lines.append("")
        lines.append(f"_{len(items)} páginas — EN: {en_count} · ZH: {zh_count}_")
        lines.append("")
        lines.append("| Idioma | Archivo origen | Caracteres | Estado | Revisar mapeo |")
        lines.append("|---|---|---|---|---|")
        for lang, rel, chars, revisar in sorted(items, key=lambda x: (x[0], x[1])):
            flag = "⚠️ sí" if revisar else ""
            lines.append(f"| {lang} | `{rel}` | {chars} | pendiente | {flag} |")
        lines.append("")

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventario generado: {OUT_FILE.resolve()}")
    print(f"Total páginas: {totals['en'] + totals['zh']} (EN {totals['en']} / ZH {totals['zh']})")
    print(f"Secciones destino: {len(by_section)}")
    print(f"Páginas que requieren revisión de mapeo en Fase 4: {revisar_count}")


if __name__ == "__main__":
    main()
