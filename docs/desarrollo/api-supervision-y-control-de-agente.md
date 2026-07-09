---
title: "Supervisión y control de agente (API de integración)"
resumen: "Operaciones de la API de integración para monitorear, intervenir e interrumpir llamadas, susurrar, y consultar el estado de agentes, grupos y colas — en HTTP, JavaScript y WebService."
seccion: "7.7 API de integración — Supervisión y control de agente"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh
obsoleto: true
relacionados: [introduccion-api-integracion, codigos-retorno-e-idiomas, api-control-de-llamada, api-datos-y-grabaciones]
---

# Supervisión y control de agente (API de integración)

## Qué es

Operaciones para que un supervisor (o el sistema que actúa en su nombre) [monitoree, intervenga, interrumpa forzadamente o susurre](../glosario.md#monitoreo-intervencion-interrupcion-forzada-y-susurro) sobre la llamada de un agente, y para consultar en tiempo real el estado de un agente, un grupo de agentes, o el equipo completo. Ver la [introducción a la API](introduccion-api-integracion.md) para el formato común de petición/respuesta.

!!! note "Diferencia entre protocolos"
    La operación **"Obtener el estado de todos los agentes del equipo"** existe en **HTTP y WebService**, pero **no tiene equivalente en la interfaz JavaScript** — no hay una función `CJI` para esta consulta a nivel de equipo completo.

## Cómo se usa

### Monitoreo, intervención, interrupción forzada y susurro

Las cuatro operan sobre la llamada de un `target` (número de agente):

| Operación | HTTP | JavaScript | WebService |
|---|---|---|---|
| Monitoreo (escucha silenciosa) | `EVENT=SILENTMONITOR&target=&phonenumber=&pwdtype=&password=&usertype=&user=&orgidentity=` | `silentMonitorCJI(target, phonenumber, pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `silentMonitor(target, phonenumber, pwdtype, password, usertype, user, orgidentity)` |
| Intervención (strong insert) | `EVENT=INTRUDE&target=&phonenumber=&pwdtype=&password=&usertype=&user=&orgidentity=` | `intrudeCJI(target, phonenumber, pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `intrude(target, phonenumber, pwdtype, password, usertype, user, orgidentity)` |
| Interrupción forzada | `EVENT=ForcedRelease&target=&phonenumber=&pwdtype=&password=&usertype=&user=&orgidentity=` | `forcedReleaseCJI(target, phonenumber, pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `forcedRelease(target, phonenumber, pwdtype, password, usertype, user, orgidentity)` |
| Susurro | `EVENT=Whisper&target=&phonenumber=&pwdtype=&password=&usertype=&user=&orgidentity=` | `whisperCJI(target, phonenumber, pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `whisper(target, phonenumber, usertype, user, pwdtype, password, orgidentity)` |

En las cuatro, `phonenumber` es el número del propio supervisor que ejecuta la acción, y `target` es el número de agente cuya llamada se va a monitorear/intervenir/interrumpir/susurrar. Para finalizar cualquiera de estos estados, usar la operación `HANGUP` de [control de llamada](api-control-de-llamada.md#colgar) con `target=groupadmin`.

### Obtener el estado de un agente

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=AGENTSTATUS&orgidentity=&usertype=&user=&pwdtype=&password=` |
| JavaScript | `agentStatusCJI(orgidentity, usertype, user, pwdtype, password, callbackFuc)` |
| WebService | `agentStatus(orgidentity, usertype, user, pwdtype, password)` |

Respuesta: cadena `status` con el estado del agente en cada una de sus colas, formato `agentgroupid1-status1,agentgroupid2-status2,...,` (cada bloque termina en coma).

### Obtener el estado de un grupo de agentes

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=AgentgroupStatus&orgidentity=&usertype=&user=&pwdtype=&password=&agent_group_id=&status=` |
| JavaScript | `agentgroupStatusCJI(orgidentity, usertype, user, pwdtype, password, agent_group_id, status, callbackFuc)` |
| WebService | `agentgroupStatus(orgidentity, usertype, user, pwdtype, password, agent_group_id, status)` |

`status`: lista separada por comas de `all`, `idle`, `busy`, `ring`, `pause`, `acw`, `login`, `logout` — filtra qué agentes del grupo se devuelven. Respuesta: `<número de agente>:<estado>` por cada agente que cumple el filtro.

### Obtener el estado de todos los agentes del equipo (HTTP y WebService únicamente)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=TeamStatus&orgidentity=&usertype=&user=&pwdtype=&password=&status=` |
| WebService | `teamStatus(orgidentity, usertype, user, pwdtype, password, status)` |

Mismo formato de `status` y de respuesta que la consulta por grupo, pero abarca todo el equipo.

### Contar agentes por estado dentro de un grupo (por número de cola)

| Protocolo | Firma |
|---|---|
| HTTP / JavaScript / WebService | `groupStatusNum(orgidentity, queuenumber, type)` |

`type`: `idle`, `ringing`, `pause`, `busy`, `acw` (cuenta solo ese estado) o `all`/vacío (cuenta todos). Respuesta con `type` específico: `<1 o 0>|<cantidad o BackMsg>` (ej. `1|2` = éxito, 2 agentes libres). Respuesta con `type=all`: `<resultado>|<total en sesión>|<libres>|<timbrando>|<pausados>|<en llamada>|<en ACW>`.

### Contar clientes por estado en la cola (predial)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=queueCustomerNum&orgidentity=&queuenumber=&prio=` |
| JavaScript | `queueCustomerNumCJI(orgidentity, queuenumber, prio, callbackFuc)` |
| WebService | `queueCustomerNum(orgidentity, queuenumber, prio)` |

`queuenumber` (`0` = todas las colas); `prio` = solo contar clientes con prioridad mayor o igual a este valor (por defecto `0`). Respuesta: `<total en cola>|<timbrando>|<esperando>|<en llamada>` (HTTP/JS con código de éxito primero; WebService antepone además su propio `1`/`0` de éxito).

### Datos en tiempo real de un agente (hoy)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=AgentRealtime&orgidentity=&usertype=&user=&pwdtype=&password=` |
| JavaScript | `agentRealtimeCJI(orgidentity, usertype, user, pwdtype, password, callbackFuc)` |
| WebService | `agentRealtime(orgidentity, usertype, user, pwdtype, password)` |

Devuelve, separados por `|`: nombre del agente, número de agente, estado actual (`idle`, `pause`, `ring`, `busy`, `acw`, `logout`), duración del estado actual, número total de pausas, número de pausas por cada motivo (`rest`, `leave`, `meeting`, `training`, `lunch`, `other`), y duración total de cada tipo de pausa (todo en segundos).

### Estadísticas de un agente en un grupo (hoy)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=AgentStatisticDay&orgidentity=&usertype=&user=&pwdtype=&password=&agent_group_id=` |
| JavaScript | `agentStatisticDayCJI(orgidentity, usertype, user, pwdtype, password, agent_group_id, callbackFuc)` |
| WebService | `agentStatisticDay(orgidentity, usertype, user, pwdtype, password, agent_group_id)` |

`agent_group_id`: lista separada por coma, o `0` para todos los grupos del agente. Respuesta: JSON `{"code":1,"message":{"<agent_group_id>":{"agent_status":..., "total_call_duration":"HH:MM:SS", "in_bound_call_answered":N, "out_bound_call_answered":N, "total_calls":N, "waiting_calls":N}}}` — una entrada por grupo consultado.

## Referencia rápida

| Necesito | Operación |
|---|---|
| Escuchar la llamada de un agente sin que lo note | `SILENTMONITOR` |
| Unirme activamente a la llamada de un agente | `INTRUDE` |
| Colgar la llamada de un agente en curso | `ForcedRelease` |
| Hablar con el agente sin que el cliente escuche | `Whisper` |
| Ver en qué colas está y su estado un agente | `AGENTSTATUS` |
| Ver el estado de todos los agentes de un grupo | `AgentgroupStatus` |
| Ver el estado de todos los agentes del equipo | `TeamStatus` (solo HTTP/WebService) |
| Contar cuántos agentes están libres en una cola | `groupStatusNum` (`type=idle`) |
| Contar clientes esperando en el predial | `queueCustomerNum` |
| Ver cuánto lleva un agente en su estado actual | `AgentRealtime` |
| Ver estadísticas del día de un agente en su grupo | `AgentStatisticDay` |

---

## Fuentes

- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/监听接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/监听接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/监听接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/强插接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/强插接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/强插接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/强拆接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/强拆接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/强拆接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/密语接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/密语接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/密语接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取坐席状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取坐席状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取坐席状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取坐席组状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取坐席组状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取坐席组状态接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取团队内所有坐席的状态.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取团队内所有坐席的状态.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取坐席组中各种坐席状态的数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取坐席组中各种坐席状态的数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取坐席组中各种坐席状态的数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取坐席组队列中各种状态的客户数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取坐席组队列中各种状态的客户数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取坐席组队列中各种状态的客户数量.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取单一坐席实时数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取单一坐席实时数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取单一坐席实时数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取单一坐席当日在坐席组中的统计数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取单一坐席当日在坐席组中的统计数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取单一坐席当日在坐席组中的统计数据.txt`
