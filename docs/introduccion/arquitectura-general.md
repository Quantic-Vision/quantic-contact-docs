---
title: "Arquitectura general"
resumen: "Cómo están organizados los componentes técnicos de AsterCC."
seccion: "1.3 Arquitectura general"
tipo: concepto
nivel: intermedio
roles: [administrador, desarrollador]
fuente: zh+en
obsoleto: false
relacionados: [que-es-astercc, funcionalidades]
---

# Arquitectura general

## Qué es

AsterCC organiza sus funciones en **tres capas**, de la más básica de telefonía a la más orientada a negocio:

```
┌─────────────────────────────────────────────┐
│ 3. Funciones de negocio (tipo CRM)           │
│    Campañas, encuestas, work orders,         │
│    e-commerce, base de conocimiento...       │
├─────────────────────────────────────────────┤
│ 2. Funciones de call center (CTI)            │
│    Agentes, colas, eventos de llamada,       │
│    API para que los módulos de negocio       │
│    reaccionen a esos eventos                 │
├─────────────────────────────────────────────┤
│ 1. Funciones de PBX (telefonía)              │
│    Troncales, extensiones, rutas, IVR,       │
│    cuentas y permisos                        │
└─────────────────────────────────────────────┘
```

### 1. Capa de PBX (telefonía)

Es la central telefónica propiamente dicha: gestiona troncales, extensiones, rutas entrantes/salientes, IVR, grupos de timbrado, facturación y también la **gestión de cuentas y permisos** (se considera parte de esta capa porque el control de acceso aplica a nivel de toda la organización telefónica).

### 2. Capa de call center (CTI)

También llamada capa de **Computer Telephony Integration**. Provee la configuración de agentes y grupos de agentes (colas), y expone los eventos de llamada y una API para que los módulos de negocio —ya sean del propio AsterCC o de terceros— puedan reaccionar a esos eventos (por ejemplo, mostrar la ficha de un cliente cuando entra su llamada).

### 3. Capa de negocio (tipo CRM)

Construida sobre los eventos y la API que expone la capa de call center. Aquí viven los módulos funcionales que ve el usuario de negocio: campañas de marketing saliente, atención al cliente entrante, encuestas, e-commerce, work orders, base de conocimiento, etc. Algunos de estos módulos se combinan entre sí — por ejemplo, una campaña de marketing saliente normalmente se usa junto con el módulo de marcación predictiva.

## Componentes principales del sistema comercial

La versión comercial de AsterCC se compone de:

| Componente | Función |
|---|---|
| Sistema de cuentas y permisos | Autenticación y control de acceso; permite estructuras organizacionales de múltiples niveles y permisos configurables por rol. |
| IP PBX | Enrutamiento, facturación, grabación, IVR y conferencias — la funcionalidad de telefonía completa. |
| Aplicaciones de oficina | Mensajería masiva (SMS/correo), planificación de tareas, flujos de trabajo, base de conocimiento, importación de datos. |
| Sistema de call center | Gestión de agentes y colas, eventos de llamada, reportes, desempeño en tiempo real, calificación de agentes. |
| Aplicaciones de negocio | Módulos construidos sobre los eventos e interfaz del call center: atención al cliente, campañas, marcación predictiva, oficina virtual, encuestas, e-commerce, work orders, entre otros. |
| Aplicaciones de llamada | Integraciones a nivel de flujo de llamada, como TTS/STT o control de dispositivos externos al descolgar. |

## Cómo se usa

Para un administrador, entender esta arquitectura ayuda a decidir en qué capa investigar un problema o una nueva configuración:

- ¿El problema es de una llamada que no rutea o un troncal caído? → Capa de PBX ([4.1 PBX y telefonía](../modulos/pbx-y-telefonia.md)).
- ¿El problema es que un agente no recibe llamadas de una cola? → Capa de call center ([4.3 Cuentas, equipos y permisos](../modulos/cuentas-equipos-permisos.md), [4.7 Plataforma de trabajo del agente](../modulos/plataforma-del-agente.md)).
- ¿El problema es con una campaña, encuesta o ficha de cliente? → Capa de negocio (sección [4. Módulos del sistema](../modulos/index.md), subgrupos correspondientes).

## Referencia rápida

| Capa | Ejemplos de módulos |
|---|---|
| PBX | Troncales, rutas, IVR, cuentas y permisos |
| Call center (CTI) | Agentes, colas, eventos de llamada, API |
| Negocio (CRM) | Campañas, encuestas, e-commerce, work orders, base de conocimiento |

---

*Fuentes: `raw/zh/start.txt`, `raw/en/start.txt`, `raw/zh/呼叫中心系统功能列表.txt`, `raw/en/astercc_call_center_quick_feature_list.txt`.*
