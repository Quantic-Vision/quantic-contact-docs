---
title: "Autenticación y sesión (API de integración)"
resumen: "Operaciones de la API de integración para iniciar/cerrar sesión, entrar y salir de colas, cambiar de modo de trabajo y configurar la extensión — en HTTP, JavaScript y WebService."
seccion: "7.5 API de integración — Autenticación y sesión"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh+en
obsoleto: true
relacionados: [introduccion-api-integracion, codigos-retorno-e-idiomas, api-control-de-llamada, api-supervision-y-control-de-agente]
---

# Autenticación y sesión (API de integración)

## Qué es

Operaciones para gestionar el ciclo de vida de la sesión de un agente desde un sistema externo: iniciar y cerrar sesión en AsterCC, entrar/salir de colas, cambiar el modo de trabajo (qué tipo de llamadas recibe) y el modo de trabajo posterior a la llamada (ACW), y fijar qué extensión usa el agente. Ver la [introducción a la API](introduccion-api-integracion.md) para el formato común de petición/respuesta y los parámetros de autenticación (`orgidentity`, `usertype`, `user`, `pwdtype`, `password`).

## Cómo se usa

### Iniciar sesión (login)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=LOGIN&orgidentity=&usertype=&user=&pwdtype=&password=` |
| JavaScript | `loginCJI(orgidentity, usertype, user, pwdtype, password, callbackFuc)` |
| WebService | `login(orgidentity, usertype, user, pwdtype, password)` |

Respuesta (éxito): incluye además un `status`/`param` con el detalle de cada cola en la que participa el agente, formato `agent_group_id=1&groupname=<nombre>&status=<idle|ringing|busy|pause>&groupadmin=<yes|no>&agenttype=<static|dynamic>&agentline=<online|offline>&errorcall=<yes|no>&agent_id=<id>|||` (un bloque por cola, terminado en `|||`). JavaScript devuelve además un código `3` propio: "ya está conectado".

### Cerrar sesión (logout)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=LOGOUT&orgidentity=&usertype=&user=&pwdtype=&password=` |
| JavaScript | `logoutCJI(orgidentity, usertype, user, pwdtype, password, callbackFuc)` |
| WebService | `logout(orgidentity, usertype, user, pwdtype, password)` |

### Entrar/salir de una o más colas (checkin/checkout)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=QUEUE&type=&usertype=&user=&orgidentity=&list=&pwdtype=&password=&deviceexten=&pushevent=` |
| JavaScript | `queueActionCJI(type, usertype, user, orgidentity, list, pwdtype, password, deviceexten, pushevent, callbackFuc)` |
| WebService | `queueAction(type, usertype, user, orgidentity, list, pwdtype, password, deviceexten, pushevent)` |

Parámetros: `type` (`1`=entrar, `2`=salir); `list` = IDs de grupo de agentes separados por coma (vacío = todos los grupos del agente); `deviceexten` (opcional) = extensión a usar al entrar; `pushevent` (`yes`/`no`, por defecto `no`) = si se debe emitir el evento de notificación de agente.

Respuesta: código `1` con detalle por grupo (`<id>:<resultado>`, ej. `1:success,2:NotChecked`), código `2` con motivo de fallo general, o código `3` cuando algunos grupos fallan (`1:NotChecked,2:NotFoundGroup`). Resultados posibles por grupo: `success`, `CheckedIn` (ya estaba dentro), `NotInGroup`, `NotFoundGroup`, `NotChecked` (al salir, si no había entrado).

### Cambiar el modo de trabajo (entrante/saliente/todo)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=WORKWAY&status=&usertype=&user=&orgidentity=&pwdtype=&password=&agent_group_id=` |
| JavaScript | `workwayActionCJI(status, usertype, user, orgidentity, pwdtype, password, agent_group_id, pushevent, callbackFuc)` |
| WebService | `workwayAction(status, usertype, user, orgidentity, pwdtype, password, agent_group_id)` |

`status`: `dialin` (solo llamadas entrantes), `dialout` (solo salientes), `all` (ambas). `agent_group_id`: lista separada por coma; vacío = todos los grupos donde el agente tiene sesión iniciada.

### Cambiar el modo de trabajo posterior a la llamada (ACW)

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=ACW&type=&usertype=&user=&orgidentity=&agent_group_id=&pwdtype=&password=` |
| JavaScript | `acwActionCJI(type, usertype, user, orgidentity, pwdtype, password, agent_group_id, pushevent, callbackFuc)` |
| WebService | `acwAction(type, usertype, user, orgidentity, pwdtype, password, agent_group_id)` |

`type`: `1`=ACW al ringing (entra en cuanto timbra el cliente/agente), `2`=ACW al answer (solo si hubo respuesta), `3`=sin ACW. El modo ACW retiene al agente sin asignarle llamadas mientras documenta la gestión, y ese tiempo se contabiliza como jornada laboral.

### Finalizar el modo ACW manualmente

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=ACWOFF&usertype=&user=&orgidentity=&pwdtype=&password=` |
| JavaScript | `acwOffCJI(usertype, user, orgidentity, pwdtype, password, pushevent, callbackFuc)` |
| WebService | `acwOff(usertype, user, orgidentity, pwdtype, password)` |

### Pausar / reanudar el servicio de todas las colas activas

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=QUEUEPAUSE&type=&usertype=&user=&orgidentity=&pause_reason=&pwdtype=&password=&dnd=` |
| JavaScript | `queuePauseCJI(type, usertype, user, orgidentity, pwdtype, password, pause_reason, pushevent, callbackFuc, dnd)` |
| WebService | `queuePause(type, usertype, user, orgidentity, pwdtype, password, pause_reason, dnd)` |

`type`: `1`=pausar, `2`=reanudar. `pause_reason` (para estadísticas de pausa, opcional): `training`, `meeting`, `leave`, `lunch`, `rest`, `other`. `dnd` (cualquier valor no vacío) sincroniza también la extensión física a modo no disponible.

### Configurar la extensión del agente

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=SetDevice&orgidentity=&exten=&user=&pwdtype=&password=` |
| JavaScript | `setdeviceCJI(orgidentity, exten, user, pwdtype, password, callbackFuc)` |
| WebService | `setdevice(orgidentity, exten, user, pwdtype, password)` |

Útil en entornos donde el equipo (PC + teléfono) es fijo pero el agente es itinerante: el agente inicia sesión, fija su extensión con esta operación, y luego entra a la cola. Si el agente es dinámico en algún grupo y ya tiene sesión iniciada en él, debe salir de la cola antes de llamar a esta operación.

## Referencia rápida

| Necesito | Operación |
|---|---|
| Autenticar a un agente/cuenta externamente | `LOGIN` / `loginCJI` / `login` |
| Terminar la sesión | `LOGOUT` / `logoutCJI` / `logout` |
| Poner al agente disponible para una cola | `QUEUE` (`type=1`) |
| Sacar al agente de una cola | `QUEUE` (`type=2`) |
| Que el agente solo reciba llamadas entrantes | `WORKWAY` (`status=dialin`) |
| Activar el modo de documentación tras colgar | `ACW` |
| Sacar manualmente al agente del modo ACW | `ACWOFF` |
| Pausar temporalmente sin salir de la cola | `QUEUEPAUSE` (`type=1`) |
| Asignar una extensión a un agente itinerante | `SetDevice` |

---

## Fuentes

- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/登录接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/登录接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/登录接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/登出接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/登出接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/登出接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/坐席组_签入_签出.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/坐席组_签入_签出.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/坐席组_签入_签出.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/工作模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/工作模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/工作模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/话后模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/话后模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/话后模式切换.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/结束话后.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/结束话后.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/结束话后.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/暂停_继续_服务.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/暂停_继续_服务.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/暂停_继续_服务.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/设置分机.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/设置分机.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/设置分机.txt`
- `raw/en/custom_development_guide/apis/http/login.txt`
- `raw/en/custom_development_guide/apis/javascript/login.txt`
- `raw/en/custom_development_guide/apis/webservice/login.txt`
- `raw/en/custom_development_guide/apis/http/logout.txt`
- `raw/en/custom_development_guide/apis/javascript/logout.txt`
- `raw/en/custom_development_guide/apis/webservice/logout.txt`
- `raw/en/custom_development_guide/apis/http/agent_group_checkin_checkout.txt`
- `raw/en/custom_development_guide/apis/javascript/agent_group_checkin_checkout.txt`
- `raw/en/custom_development_guide/apis/webservice/agent_group_checkin_checkout.txt`
- `raw/en/custom_development_guide/apis/http/switch_work_mode.txt`
- `raw/en/custom_development_guide/apis/javascript/switch_work_mode.txt`
- `raw/en/custom_development_guide/apis/webservice/switch_work_mode.txt`
- `raw/en/custom_development_guide/apis/http/switch_acw_mode.txt`
- `raw/en/custom_development_guide/apis/javascript/switch_acw_mode.txt`
- `raw/en/custom_development_guide/apis/webservice/switch_acw_mode.txt`
- `raw/en/custom_development_guide/apis/http/exit_acw.txt`
- `raw/en/custom_development_guide/apis/javascript/exit_acw.txt`
- `raw/en/custom_development_guide/apis/webservice/exit_acw.txt`
- `raw/en/custom_development_guide/apis/http/pause_unpause.txt`
- `raw/en/custom_development_guide/apis/javascript/pause_unpause.txt`
- `raw/en/custom_development_guide/apis/webservice/pause_unpause.txt`
- `raw/en/custom_development_guide/apis/http/bind_extension.txt`
- `raw/en/custom_development_guide/apis/javascript/bind_extension.txt`
- `raw/en/custom_development_guide/apis/webservice/bind_extension.txt`
