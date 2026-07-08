---
title: "Tarifas y facturación"
resumen: "Los tres niveles de tarifa de AsterCC (sistema, equipo, extensión) y cómo se calcula el costo de una llamada."
seccion: "4.4 Tarifas y facturación"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, reportes-y-estadisticas]
---

# Tarifas y facturación

## Qué es

AsterCC calcula el costo de las llamadas salientes en **tres niveles de tarifa**, cada uno con un propósito distinto:

| Nivel | Para qué sirve |
|---|---|
| Tarifa de sistema | Calcula el costo real que le cuesta al operador cada troncal — solo la configura el administrador de sistema |
| Tarifa de equipo | Lo que se le cobra a un equipo (cliente) por sus llamadas |
| Tarifa de extensión | Tarifa específica aplicada a una extensión o a un agente en llamadas entrantes |

Estos niveles son independientes entre sí: la tarifa de sistema no depende de qué troncal se haya usado realmente en la llamada — se calcula igual, solo con el propósito de medir el costo real de cada troncal.

## Cómo se usa

### Definir una regla de tarifa

Todas las tarifas se definen con la misma lógica de coincidencia (prefijo + longitud de número):

| Campo | Qué define |
|---|---|
| Prefijo del número | Qué números aplican esta tarifa (`0` para llamadas nacionales, `00` para internacionales, `001` para EE.UU., `default` para cualquier número) |
| Longitud del número | Filtra además por cantidad de dígitos (`0` = sin restricción) |
| Periodo de facturación | Cada cuánto se cobra |
| Tarifa de conexión | Costo fijo al contestar la llamada |
| Duración inicial | Tiempo cubierto por la tarifa de conexión antes de empezar a cobrar por minuto |
| Tarifa por minuto | Costo recurrente después de la duración inicial |
| Equipo | A qué equipo aplica (vacío = aplica a todos, con prioridad a la tarifa más específica) |
| Troncal | A qué troncal aplica esta tarifa (relevante en tarifa de sistema y de equipo) |

!!! tip
    Si no se selecciona un troncal en la tarifa de sistema, el costo se contabiliza igual dentro del costo total de salida, pero no se atribuye a ningún troncal en particular.

### Tarifa de sistema

Mide el costo real de cada llamada saliente según el troncal usado, acumulando tanto al costo del troncal como al costo total del sistema. Solo la puede configurar el administrador de sistema — no está pensada para facturar clientes, sino para que el operador sepa cuánto le cuesta realmente cada troncal.

### Tarifa de equipo

Define cuánto se le cobra a un equipo por sus llamadas salientes — el mecanismo típico cuando AsterCC se usa en modo multiempresa/SaaS y cada equipo paga por su consumo.

### Tarifa de extensión (agente)

Aplica una tarifa a nivel de extensión — usada, por ejemplo, para cobrar diferenciado por agente en llamadas entrantes atendidas.

## Referencia rápida

| Tarifa | Configúrala en | Quién la ve/usa |
|---|---|---|
| Sistema | Tarifas → Tarifa de sistema | Solo administrador de sistema |
| Equipo | Tarifas → Tarifa de equipo | Facturación al cliente/equipo |
| Extensión | Tarifas → Tarifa de extensión / agente | Costeo por agente |

---

*Fuente: `raw/zh/模块使用说明/费率管理/系统费率.txt`.*
