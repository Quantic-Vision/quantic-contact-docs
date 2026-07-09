---
title: "Tarifas y facturación"
resumen: "Los cinco niveles de tarifa de AsterCC — sistema, equipo, extensión, agente y usuario virtual — y cómo la tarifa de extensión también decide qué troncal usa una llamada."
seccion: "4.4 Tarifas y facturación"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [pbx-y-telefonia, cuentas-equipos-permisos, oficina-virtual-bpo, reportes-y-estadisticas]
---

# Tarifas y facturación

## Qué es

AsterCC calcula el costo de las llamadas en **cinco niveles de tarifa**, cada uno con un propósito distinto:

| Nivel | Para qué sirve | Quién la configura |
|---|---|---|
| Tarifa de sistema | Costo real que le cuesta al operador cada troncal | Solo administrador de sistema |
| Tarifa de equipo | Lo que se le cobra a un equipo/cliente por sus llamadas salientes | Administrador de sistema (solo lectura para el equipo) |
| Tarifa de extensión | Costo por extensión saliente — **y además decide qué troncal usa la llamada** | Administrador de sistema o de equipo |
| Tarifa de agente (llamadas entrantes) | Paga al agente por cada llamada entrante atendida — típico para liquidar personal freelance | Administrador de sistema o de equipo |
| Tarifa de usuario virtual | Cobra por llamadas entrantes y transferencias de un [usuario virtual (oficina virtual)](oficina-virtual-bpo.md) | Administrador de sistema o de equipo |

Los primeros niveles son independientes entre sí — la tarifa de sistema mide el costo real sin importar qué tarifa de equipo o extensión se haya aplicado a esa misma llamada.

## Cómo se usa

### Estructura común de una regla de tarifa (sistema, equipo, extensión)

| Campo | Obligatorio | Qué define |
|---|---|---|
| Prefijo del número | Sí | Qué números aplican esta tarifa (`0` nacional, `00` internacional, `001` EE.UU., `default` cualquier número) |
| Longitud del número | Sí | Filtra además por cantidad de dígitos (`0` = sin restricción) |
| Periodo de facturación | Sí | Cada cuánto se cobra |
| Estado | Sí | Si la regla está activa |
| Nombre del objetivo | No | Etiqueta libre (ej. "local", "larga distancia", "EE.UU.") |
| Tarifa de conexión | No | Costo fijo al contestar |
| Duración inicial | No | Tiempo cubierto por la tarifa de conexión antes de cobrar por minuto |
| Tarifa por minuto | No | Costo recurrente tras la duración inicial |
| Equipo | No | Vacío = aplica a todos los equipos; el sistema siempre prioriza la tarifa más específica sobre la general |
| Troncal | Solo en sistema/equipo | A qué troncal se atribuye el costo (en tarifa de sistema, si se deja vacío el costo se contabiliza igual pero sin atribuir a un troncal específico) |

### Tarifa de sistema

Mide el costo real de cada llamada saliente según el troncal usado — acumula tanto al costo de ese troncal como al costo total del sistema. No está pensada para facturar clientes, sino para que el operador conozca su propio costo real: no influye en qué troncal se selecciona para la llamada, solo la contabiliza una vez que el troncal ya fue elegido por la tarifa de extensión. Es de solo lectura para administradores de equipo.

### Tarifa de equipo

Define cuánto se le cobra a un equipo por sus llamadas salientes — el mecanismo típico en modo multiempresa/SaaS. También es de solo lectura para el administrador del equipo (la fija el administrador de sistema).

### Tarifa de extensión — también decide el troncal de salida

Esta es la tarifa con más impacto funcional: además de calcular el costo de una llamada saliente por extensión, **su coincidencia determina a qué troncal se envía la llamada**. Dos campos adicionales respecto a la estructura común:

| Campo | Qué define |
|---|---|
| Grupo de cuentas | Si se define, la tarifa solo aplica a extensiones de ese [grupo de cuentas](cuentas-equipos-permisos.md#grupos-de-cuentas) — si se deja vacío, aplica a toda extensión interna del equipo |
| Troncal | El troncal que efectivamente recibe la llamada al coincidir esta regla |

**Orden de selección del troncal** (de más a menos específico):
1. Tarifa a nivel de grupo de cuentas.
2. Tarifa a nivel de equipo (sin grupo de cuentas específico).
3. Tarifa a nivel de sistema (sin equipo específico).

Dentro de un mismo nivel, el orden de coincidencia es: **prefijo + longitud exactos** → **solo longitud** → **solo prefijo** → **regla `default`** (comodín).

!!! warning
    Si una llamada no coincide con ninguna tarifa de extensión en ningún nivel, no hay una ruta implícita — la llamada no tiene por dónde salir. Siempre debe existir al menos una regla `default` en algún nivel que cubra el tráfico no explícitamente tarifado.

Un administrador de equipo, al entrar a esta pantalla, ve tanto las tarifas de extensión propias de su equipo como la tarifa `default` general — esta última es de solo lectura para él, ya que la fija el administrador de sistema.

### Tarifa de agente (llamadas entrantes)

Paga al agente una tarifa por cada llamada entrante que atiende — no usa prefijo ni longitud de número, ya que no se trata de marcación saliente.

| Campo | Qué define |
|---|---|
| Periodo de facturación | Único campo obligatorio |
| Equipo | Vacío = aplica a todos los equipos |
| Grupo de agentes | La tarifa se aplica por grupo — distintos grupos pueden pagar distinto |
| Agente | Opcional — acota la tarifa a un agente específico dentro del grupo; vacío = aplica a todo el grupo |

El monto acumulado se liquida luego desde [Gestión de agentes → Pagar](cuentas-equipos-permisos.md#agentes), y queda auditado en el log financiero del agente.

### Tarifa de usuario virtual

Cobra por el uso que hace un [usuario virtual de oficina virtual](oficina-virtual-bpo.md) del sistema — llamadas entrantes y transferencias.

| Campo | Obligatorio | Qué define |
|---|---|---|
| Nombre de la tarifa | Sí | Identificación libre |
| Tarifa por minuto | Sí | Costo recurrente |
| Periodo de facturación | Sí | Cada cuánto se cobra |
| Equipo | No | A qué equipo aplica |
| Usuario virtual | No | A cuál usuario virtual de ese equipo aplica |
| Tarifa de conexión | No | Costo fijo al contestar |
| Duración inicial | No | Tiempo cubierto antes de cobrar por minuto |
| Vigencia (inicio/fin) | No | Rango de fechas en que esta tarifa está activa |
| Tipo de tarifa | No | **Entrante** (llamada que recibe el usuario virtual) o **transferencia** — si es transferencia, se puede acotar por prefijo del destino |
| Notas | No | Descripción libre |

## Referencia rápida

| Tarifa | Configúrala en | Afecta el enrutamiento de la llamada |
|---|---|---|
| Sistema | Tarifas → Tarifa de sistema | No |
| Equipo | Tarifas → Tarifa de equipo | No |
| Extensión | Tarifas → Tarifa de extensión | **Sí — decide el troncal** |
| Agente (entrante) | Tarifas → Tarifa de agente | No |
| Usuario virtual | Tarifas → Tarifa de usuario virtual | No |

---

## Fuentes

- `raw/zh/模块使用说明/费率管理/系统费率.txt`
- `raw/zh/模块使用说明/费率管理/团队费率.txt`
- `raw/zh/模块使用说明/费率管理/分机费率.txt`
- `raw/zh/模块使用说明/费率管理/坐席呼入费率.txt`
- `raw/zh/模块使用说明/费率管理.txt`
- `raw/zh/模块使用说明/虚拟呼叫中心/费率管理.txt`
- `raw/en/module_manual/rate.txt`
- `raw/en/module_manual/rate/agentrates.txt`
- `raw/en/module_manual/rate/customerrates.txt`
- `raw/en/module_manual/rate/systemrates.txt`
- `raw/en/module_manual/rate/teamrates.txt`
