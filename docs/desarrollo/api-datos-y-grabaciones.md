---
title: "Datos y grabaciones (API de integración)"
resumen: "Operaciones de la API de integración para fijar datos adjuntos a una llamada, importar clientes a una campaña y obtener la URL de una grabación — en HTTP, JavaScript y WebService."
seccion: "7.8 API de integración — Datos y grabaciones"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh+en
obsoleto: true
relacionados: [introduccion-api-integracion, codigos-retorno-e-idiomas, api-control-de-llamada, api-y-ami]
---

# Datos y grabaciones (API de integración)

## Qué es

Operaciones para adjuntar datos personalizados a una llamada en curso, importar clientes a una campaña de marcación saliente (y opcionalmente al [predial](../glosario.md#paquete-de-clientes-para-marcacion-saliente)), y obtener la URL de descarga/reproducción de una grabación. Ver la [introducción a la API](introduccion-api-integracion.md) para el formato común de petición/respuesta.

## Cómo se usa

### Fijar datos adjuntos (variable de canal / "随路数据")

Asocia una variable personalizada a la llamada en curso — útil para pasar datos de negocio (ej. un ID de ticket) que luego se pueden leer desde el CDR o desde eventos.

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=SetVar&orgidentity=&usertype=&user=&pwdtype=&password=&varname=&varvalue=` |
| JavaScript | `setvarCJI(orgidentity, usertype, user, pwdtype, password, varname, varvalue, callbackFuc)` |
| WebService | `setVar(orgidentity, usertype, user, pwdtype, password, varname, varvalue)` |

`varname` solo admite mayúsculas, números, `-` y `_`, y debe empezar con mayúscula o número (ver [BackMsg_101](codigos-retorno-e-idiomas.md)).

### Importar clientes a una campaña (y al predial)

Ya documentada en detalle, con todos los parámetros, en [API y AMI — importar datos a una campaña](api-y-ami.md#importar-datos-a-una-campana-o-al-predial-importws). Las tres variantes del manual v2.0 comparten exactamente los mismos parámetros:

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=Import&orgidentity=&usertype=&user=&pwdtype=&password=&modeltype=&model_id=&source=&context=&source_user=&source_pwd=&exetime=&delrow=&phone_field=&priority_field=&dialtime_field=&emptyagent=&resetstatus=&dupway=&dupdiallist=&changepackage=` |
| JavaScript | `importCJI(orgidentity, usertype, user, pwdtype, password, modeltype, model_id, source, context, source_user, source_pwd, exetime, delrow, phone_field, priority_field, dialtime_field, emptyagent, resetstatus, dupway, dupdiallist, changepackage, callbackFuc)` |
| WebService | `importWS(orgidentity, usertype, user, pwdtype, password, modeltype, model_id, source, context, source_user, source_pwd, exetime, delrow, phone_field, priority_field, dialtime_field, emptyagent, resetstatus, dupway, dupdiallist, changepackage)` |

!!! warning
    Todos los parámetros son obligatorios en las tres variantes — los que no apliquen deben enviarse como cadena vacía (`''`), nunca omitirse.

### Obtener la URL de una grabación

| Protocolo | Firma |
|---|---|
| HTTP | `EVENT=GetMonitor&sessionid=&calldate=&mp3=` |
| JavaScript | `getMonitorCJI(sessionid, calldate, callbackFuc, mp3)` |
| WebService | `getMonitor(sessionid, calldate, mp3)` |

`sessionid`: identificador único de la llamada (el mismo `sessionid`/`diallogid` que aparece en los [eventos en tiempo real](eventos-tiempo-real-api.md)). `calldate`: fecha en que ocurrió la llamada, formato `AAAA-MM-DD`. `mp3` (`yes`/`no`, por defecto `no`): si se debe convertir a MP3 antes de entregar la URL.

!!! note "Requiere configuración previa"
    Esta operación necesita el parámetro `webroot_address` configurado en `/etc/astercc.conf`, sección `[system]` — es la URL web pública del servidor de AsterCC (ej. `webroot_address = http://192.168.1.100:80/`), usada para construir la URL de la grabación que se devuelve.

## Referencia rápida

| Necesito | Operación |
|---|---|
| Adjuntar un dato de negocio a la llamada actual | `SetVar` |
| Cargar clientes nuevos a una campaña / al predial | `Import` / `importCJI` / `importWS` |
| Obtener el enlace de descarga de una grabación | `GetMonitor` |

---

## Fuentes

- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/设置随路数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/设置随路数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/设置随路数据.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/数据导入接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/数据导入接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/数据导入接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/获取录音地址.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/获取录音地址.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/获取录音地址.txt`
- `raw/en/custom_development_guide/apis/http/set_data_to_agent.txt`
- `raw/en/custom_development_guide/apis/javascript/set_call_data.txt`
- `raw/en/custom_development_guide/apis/webservice/set_data_to_agent.txt`
- `raw/en/custom_development_guide/apis/http/import.txt`
- `raw/en/custom_development_guide/apis/javascript/import.txt`
- `raw/en/custom_development_guide/apis/webservice/import.txt`
- `raw/en/custom_development_guide/how_to_import_the_customers_information_via_api.txt`
- `raw/en/custom_development_guide/apis/http/get_recording_url.txt`
- `raw/en/custom_development_guide/apis/javascript/get_recording_url.txt`
- `raw/en/custom_development_guide/apis/webservice/get_recording_url.txt`
