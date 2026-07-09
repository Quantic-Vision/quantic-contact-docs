---
title: "Control de llamada (API de integración)"
resumen: "Operaciones de la API de integración para originar, transferir, retener, consultar, conferenciar y colgar llamadas, y enviar DTMF — en HTTP, JavaScript y WebService."
seccion: "7.6 API de integración — Control de llamada"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh+en
obsoleto: true
relacionados: [introduccion-api-integracion, codigos-retorno-e-idiomas, api-autenticacion-y-sesion, api-supervision-y-control-de-agente]
---

# Control de llamada (API de integración)

## Qué es

Operaciones para controlar el ciclo de vida de una llamada desde un sistema externo: originar, transferir, [consultar](../glosario.md#consulta-transferencia-recuperar-y-conferencia), formar conferencia, recuperar, retener/reanudar, colgar, enviar DTMF, y transferir a un IVR. Ver la [introducción a la API](introduccion-api-integracion.md) para el formato común de petición/respuesta.

## Cómo se usa

### Originar llamada

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=MAKECALL&targetdn=&targettype=&agentgroupid=&usertype=&user=&orgidentity=&pwdtype=&password=&modeltype=&model_id=&userdata=&agentexten=&callerid=&callername=&trunkidentity=&cidtype=` |
| JavaScript | `makeCallCJI(targetdn, targettype, agentgroupid, usertype, user, orgidentity, pwdtype, password, modeltype, model_id, userdata, callbackFuc, agentexten, callerid, callername, trunkidentity, cidtype)` |
| WebService | `makeCall(targetdn, targettype, agentgroupid, usertype, user, orgidentity, pwdtype, password, modeltype, model_id, userdata, agentexten, callerid, callername, trunkidentity, cidtype)` |

Parámetros clave: `targetdn` (número de agente si `targettype=inner`, o número externo si `targettype=exter`); `modeltype` (`BusinessApp`, `Campaign`, `Virtualcustomer` o `Customerservice`); `userdata` (cadena libre que se recibirá tal cual en los eventos de la llamada — ver [eventos en tiempo real](eventos-tiempo-real-api.md)); `agentexten`, `callerid`, `callername`, `trunkidentity`, `cidtype` (`0`=usar `callerid` de la API, `1`=el del troncal, `2`=el de la extensión) son opcionales.

### Colgar

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=HANGUP&uniqueid=&targetagent=&target=&pwdtype=&password=&usertype=&user=&orgidentity=` |
| JavaScript | `hangupCJI(uniqueid, targetagent, target, pwdtype, password, usertype, user, orgidentity, callbackFuc)` |
| WebService | `hangup(uniqueid, targetagent, target, pwdtype, password, usertype, user, orgidentity)` |

`target` define qué colgar: `channel` (requiere `uniqueid`), `agent` (la llamada del agente destino), `caller` (al cliente), `consult` (la(s) parte(s) en consulta), `all` (todo lo relacionado al agente, incluida la llamada del supervisor si está monitoreando/interviniendo), `groupadmin` (cuelga solo al supervisor, terminando su monitoreo/intervención/susurro). Si se pasan varios `uniqueid` (separados por coma), la respuesta detalla el resultado de cada uno (`<uniqueid>:success` o `:failed`).

### Transferencia y conferencia (tras una consulta)

Ambas operaciones se ejecutan **después** de establecer una llamada de [consulta](#consulta).

| Operación | HTTP | JavaScript | WebService |
|---|---|---|---|
| Transferir | `EVENT=TRANSFER&pwdtype=&password=&usertype=&user=&orgidentity=` | `transferCJI(pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `transfer(pwdtype, password, usertype, user, orgidentity)` |
| Conferencia | `EVENT=CONFERENCE&pwdtype=&password=&usertype=&user=&orgidentity=` | `conferenceCJI(pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `conference(pwdtype, password, usertype, user, orgidentity)` |
| Recuperar (volver al cliente) | `EVENT=CALLRETURN&pwdtype=&password=&usertype=&user=&orgidentity=` | `callReturnCJI(pwdtype, password, usertype, user, orgidentity, callbackFuc)` | `callRetuen(pwdtype, password, usertype, user, orgidentity)` (ver nota) |

!!! note "Discrepancia entre fuentes ZH y EN — nombre del método WebService de Recuperar"
    La fuente en chino (`raw/zh/.../webservice接口/接回接口.txt`) define el método como `callRetuen(...)` — con el mismo error de escritura ("Retuen" por "Return") que aparece en el formato de respuesta de toda la API. La fuente en inglés equivalente (`raw/en/custom_development_guide/apis/webservice/resume.txt`) documenta en cambio el nombre **`callReturn(...)`, correctamente escrito**, para el mismo método. El formato de la respuesta (`|Retuen|<código>|Retuen|<mensaje>`) mantiene el typo en ambas fuentes — la discrepancia es solo en el nombre del método SOAP. Si tu integración fallara al invocar `callRetuen`, prueba con `callReturn`.

### Consulta

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=CONSULT&targetdn=&agentgroupid=&consulttype=&pwdtype=&password=&usertype=&user=&orgidentity=` |
| JavaScript | `consultCJI(targetdn, agentgroupid, consulttype, pwdtype, password, usertype, user, orgidentity, callbackFuc)` |
| WebService | `consult(targetdn, agentgroupid, consulttype, pwdtype, password, usertype, user, orgidentity)` |

`consulttype`: `internal` (consulta interna — `targetdn` es el número de otro agente, `agentgroupid` el grupo de ese agente) o `external` (consulta externa — `targetdn` es un número externo, `agentgroupid=0`).

### Retener y reanudar (hold/resume)

| Operación | HTTP | JavaScript | WebService |
|---|---|---|---|
| Retener | `EVENT=Hold&silence=&orgidentity=&usertype=&user=&pwdtype=&password=` | `holdCJI(silence, orgidentity, usertype, user, pwdtype, password, callbackFuc)` | `hold(silence, orgidentity, usertype, user, pwdtype, password)` |
| Reanudar | `EVENT=Resume&orgidentity=&usertype=&user=&pwdtype=&password=` | `resumeCJI(orgidentity, usertype, user, pwdtype, password, callbackFuc)` | `resume(orgidentity, usertype, user, pwdtype, password)` |

`silence` (`0`/`1`) define si el cliente escucha silencio o música de espera al quedar retenido. Aplica solo cuando la llamada es exclusivamente agente-cliente (dos partes).

!!! note "Solo en HTTP — campo `status` adicional en la respuesta (fuente EN)"
    La fuente en inglés para HTTP (`raw/en/custom_development_guide/apis/http/moh.txt` y `.../exit_moh.txt`) documenta un formato de respuesta con un tercer segmento: `|Return|<código>|Return|<mensaje>|Return|<status>`. Este campo `status` adicional no aparece en las variantes JavaScript ni WebService (que devuelven solo `code`/`message`), ni en la fuente china. No se ha podido confirmar su significado exacto — trátalo como informativo hasta validarlo contra el servidor real.

### Doble llamada / devolución (backCall)

Envía primero la llamada al número de origen (`exten`) y, una vez que este responde, marca al destino (`targetdn`) — patrón conocido como "devolución de llamada" o *click-to-call* de dos etapas.

| Protocolo | Firma |
|---|---|
| HTTP | `backCall(orgidentity, exten, targetdn, callerid, user, password, pwdtype, userdata)` |
| JavaScript | `backCallCJI(orgidentity, exten, targetdn, callerid, user, password, pwdtype, userdata, callbackFuc)` |
| WebService | `backCall(orgidentity, exten, targetdn, callerid, user, password, pwdtype, userdata)` |

`userdata` es texto libre que queda almacenado en el campo `userdata` del registro de la llamada.

### Enviar DTMF

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=SendDtmf&orgidentity=&usertype=&user=&pwdtype=&password=&dtmf=` |
| JavaScript | `dtmfCJI(orgidentity, usertype, user, pwdtype, password, dtmf, callbackFuc)` |
| WebService | `sendDtmf(orgidentity, usertype, user, pwdtype, password, dtmf)` |

`dtmf` solo admite dígitos, `*` y `#` (ver [glosario: DTMF](../glosario.md#dtmf)).

### Transferir al agente a un IVR

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=AgentToIvr&orgidentity=&usertype=&user=&pwdtype=&password=&ivrexten=&ivrflow=&transfer=` |
| JavaScript | `agenttoivrCJI(orgidentity, usertype, user, pwdtype, password, ivrexten, ivrflow, transfer, callbackFuc)` |
| WebService | `agentToIvr(orgidentity, usertype, user, pwdtype, password, ivrexten, ivrflow, transfer)` |

`ivrexten`: extensión interna del [IVR](../glosario.md#ivr-respuesta-de-voz-interactiva) principal. `ivrflow`: simula las teclas que presionaría el cliente para navegar el IVR, separadas por `-` (ej. `1-2-5`). `transfer`: `0`=transferencia con liberación, `1`=transferencia con retención (el agente queda a la espera).

## Referencia rápida

| Necesito | Operación |
|---|---|
| Originar una llamada desde el sistema externo | `MAKECALL` |
| Colgar la llamada actual del agente | `HANGUP` (`target=agent`) |
| Consultar a otro agente antes de transferir | `CONSULT` (`consulttype=internal`) |
| Completar la transferencia tras la consulta | `TRANSFER` |
| Unir a las tres partes en conferencia | `CONFERENCE` |
| Poner al cliente en espera | `Hold` |
| Marcar primero al agente y luego al destino | `backCall` |
| Enviar tonos DTMF durante la llamada | `SendDtmf` |
| Enviar al agente a un flujo de IVR | `AgentToIvr` |

---

## Fuentes

- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/呼叫接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/呼叫接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/呼叫接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/挂断接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/挂断接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/挂断接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/转接接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/转接接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/转接接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/会议接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/会议接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/会议接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/接回接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/接回接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/接回接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/咨询接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/咨询接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/咨询接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/通话暂停接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/通话暂停接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/通话暂停接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/通话继续接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/通话继续接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/通话继续接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/双呼回拨.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/双呼回拨.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/双呼回拨.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/发送dtmf.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/发送dtmf.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/发送dtmf.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/坐席转ivr.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/坐席转ivr.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/坐席转ivr.txt`
- `raw/en/custom_development_guide/apis/http/call.txt`
- `raw/en/custom_development_guide/apis/javascript/call.txt`
- `raw/en/custom_development_guide/apis/webservice/call.txt`
- `raw/en/custom_development_guide/apis/http/hangup.txt`
- `raw/en/custom_development_guide/apis/javascript/hangup.txt`
- `raw/en/custom_development_guide/apis/webservice/hangup.txt`
- `raw/en/custom_development_guide/apis/http/transfer.txt`
- `raw/en/custom_development_guide/apis/javascript/transfer.txt`
- `raw/en/custom_development_guide/apis/webservice/transfer.txt`
- `raw/en/custom_development_guide/apis/http/conference.txt`
- `raw/en/custom_development_guide/apis/javascript/conference.txt`
- `raw/en/custom_development_guide/apis/webservice/conference.txt`
- `raw/en/custom_development_guide/apis/http/resume.txt`
- `raw/en/custom_development_guide/apis/javascript/resume.txt`
- `raw/en/custom_development_guide/apis/webservice/resume.txt`
- `raw/en/custom_development_guide/apis/http/consult.txt`
- `raw/en/custom_development_guide/apis/javascript/consult.txt`
- `raw/en/custom_development_guide/apis/webservice/consult.txt`
- `raw/en/custom_development_guide/apis/http/moh.txt`
- `raw/en/custom_development_guide/apis/javascript/moh.txt`
- `raw/en/custom_development_guide/apis/webservice/moh.txt`
- `raw/en/custom_development_guide/apis/http/exit_moh.txt`
- `raw/en/custom_development_guide/apis/javascript/exit_moh.txt`
- `raw/en/custom_development_guide/apis/webservice/exit_moh.txt`
- `raw/en/custom_development_guide/apis/http/callback.txt`
- `raw/en/custom_development_guide/apis/javascript/callback.txt`
- `raw/en/custom_development_guide/apis/webservice/callback.txt`
- `raw/en/custom_development_guide/apis/http/send_dtmf.txt`
- `raw/en/custom_development_guide/apis/javascript/send_dtmf.txt`
- `raw/en/custom_development_guide/apis/webservice/send_dtmf.txt`
- `raw/en/custom_development_guide/apis/http/transfer_to_ivr.txt`
- `raw/en/custom_development_guide/apis/javascript/transfer_to_ivr.txt`
- `raw/en/custom_development_guide/apis/webservice/transfer_to_ivr.txt`
