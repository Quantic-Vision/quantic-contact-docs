---
title: "Introducción a la API de integración"
resumen: "Los tres protocolos de la API de integración de AsterCC (HTTP, JavaScript, WebService), cuándo usar cada uno y el formato común de petición y respuesta."
seccion: "7.3 API de integración — Introducción"
tipo: concepto
nivel: avanzado
roles: [desarrollador]
fuente: zh+en
obsoleto: true
relacionados: [api-y-ami, codigos-retorno-e-idiomas, api-autenticacion-y-sesion, api-control-de-llamada, api-supervision-y-control-de-agente, api-datos-y-grabaciones]
---

# Introducción a la API de integración

## Qué es

AsterCC ofrece un **manual de interfaces v2.0** con tres protocolos equivalentes para que una aplicación de terceros (típicamente el CRM o sistema de negocio desplegado junto al escritorio del agente) controle la telefonía y consulte estados desde fuera de AsterCC: **HTTP**, **JavaScript** y **WebService**. Los tres exponen el mismo conjunto de operaciones (inicio de sesión, control de llamada, supervisión de agentes, consulta de estados, datos y grabaciones) — documentadas operación por operación en:

- [Autenticación y sesión](api-autenticacion-y-sesion.md)
- [Control de llamada](api-control-de-llamada.md)
- [Supervisión y control de agente](api-supervision-y-control-de-agente.md)
- [Datos y grabaciones](api-datos-y-grabaciones.md)
- [Códigos de retorno y codificación de idioma](codigos-retorno-e-idiomas.md)

!!! warning "Puede estar desactualizado"
    Este manual de interfaces (v2.0) proviene de la guía de desarrollo original (~2018). Antes de integrar en producción, valida contra el manual vigente de tu versión de AsterCC. Es un protocolo **distinto y más completo** que la [API HTTP de acciones simples](api-y-ami.md) (`asterccinterfaces?EVENT=...`) documentada en la sección 7.1 — esa API más simple sigue existiendo y es útil para casos puntuales (originar llamada desde un botón, importar datos), pero para construir una integración completa de escritorio de agente se usa el manual v2.0 descrito aquí.

## Cómo se usa

### Los tres protocolos y cuándo usar cada uno

| Protocolo | Endpoint / mecanismo | Cuándo usarlo |
|---|---|---|
| **HTTP** | `http://<ip>:<puerto>/asterccinterfaces` — parámetros por query string, con `EVENT=<NOMBRE_ACCION>` | Integraciones servidor-a-servidor o desde cualquier lenguaje que pueda hacer una petición HTTP (PHP, Python, backend de un CRM). Es el protocolo más simple de invocar fuera del navegador. |
| **JavaScript** | Script `astcccwi... astcc_CJI.js` cargado desde `http://<ip>:<puerto>/asterccinterface/astcc_CJI.js`, expone funciones `xxxCJI(...)` | La **pantalla del agente en el navegador** (aplicación B/S embebida o cross-domain junto a la plataforma de trabajo del agente). Cada función recibe un parámetro adicional `callbackFuc` — una función de [callback](../glosario.md#webhook-callback) que AsterCC invoca de forma asíncrona con el resultado en JSON. Página de referencia para pruebas: `http://<ip>:<puerto>/asterccinterface/test_CJI.html`. |
| **WebService** | SOAP/WSDL en `http://<ip>:<puerto>/<appname>` (archivo `astcccwi.php?wsdl`, con `astcccwi.wsdl` editado con la IP del servidor) | Integraciones servidor-a-servidor desde plataformas que consumen SOAP directamente (ej. sistemas Java/.NET empresariales con clientes WSDL generados). |

!!! note "Detalles adicionales de la fuente en inglés"
    La guía en inglés (`raw/en/custom_development_guide/apis/`) aporta dos detalles concretos no capturados en la versión ZH: la página de prueba de la interfaz JavaScript se llama `test_CJI_en.html` (variante en inglés del `test_CJI.html` de la fuente china — el nombre depende del idioma de la instalación), y el webroot por defecto del servidor donde se despliega el WSDL de WebService es `/var/www/html/asterCC/app/webroot/` (ejemplo de la fuente EN: `http://192.168.1.45:4580`).

En resumen: **JavaScript es para la pantalla embebida del agente en el navegador** (necesita el callback asíncrono porque corre en el hilo de la UI); **HTTP y WebService son para integraciones servidor-a-servidor**, y son intercambiables — HTTP es más simple de invocar, WebService es preferible si tu plataforma ya tiene tooling maduro para consumir WSDL.

### Formato de petición

- **HTTP:** todos los parámetros van en la query string de una sola URL, con `EVENT=<NOMBRE>` identificando la operación. Ejemplo (login): `EVENT=LOGIN&orgidentity=orgidentity&usertype=usertype&user=user&pwdtype=pwdtype&password=password`.
- **JavaScript:** se llama una función `nombreOperacionCJI(param1, param2, ..., callbackFuc)` — el nombre de la función varía por operación (ej. `loginCJI`, `makeCallCJI`), y siempre añade `callbackFuc` como último parámetro (o antepenúltimo si hay parámetros opcionales después).
- **WebService:** se invoca un método SOAP con el mismo nombre que la función JS pero sin el sufijo `CJI` (ej. `login`, `makeCall`), pasando los parámetros posicionalmente, sin `callbackFuc`.

### Formato de respuesta

- **HTTP y WebService** devuelven un **string** con el patrón `|Retuen|<código>|Retuen|<mensaje>` (el literal `Retuen` es un error de escritura del fabricante que se mantiene en la API real — no es un typo de esta traducción). El código `1` indica éxito, `2` indica error; algunas operaciones agregan más segmentos `|Retuen|` (ej. login agrega `|Retuen|<status>` con el estado del agente en cada cola).
- **JavaScript** devuelve **JSON** equivalente: `{code: <código>, message: <mensaje>}` (con campos adicionales según la operación, ej. `status` en login), entregado como argumento al `callbackFuc`.
- El significado de cada código de error (`BackMsg_NN`) está centralizado en [Códigos de retorno y codificación de idioma](codigos-retorno-e-idiomas.md).

### Parámetros de autenticación comunes a casi toda operación

| Parámetro | Qué define |
|---|---|
| `orgidentity` | Identificador único del equipo/organización |
| `usertype` | `agent` (autenticar como agente por número de agente) o `account` (autenticar como cuenta de usuario) |
| `user` | Número de agente o nombre de usuario, según `usertype` |
| `pwdtype` | Tipo de contraseña: `plaintext` (texto plano) o `md5` (hash MD5) |
| `password` | La contraseña, en el formato indicado por `pwdtype` |

## Referencia rápida

| Necesito | Uso |
|---|---|
| Integrar la pantalla del agente en el navegador | Interfaz **JavaScript** (`astcc_CJI.js`) |
| Integrar mi backend/CRM con AsterCC sin tocar el navegador | Interfaz **HTTP** o **WebService** — cualquiera de las dos |
| Saber qué significa un código de error devuelto | [Códigos de retorno](codigos-retorno-e-idiomas.md) |
| Iniciar sesión, cambiar de modo de trabajo, cerrar sesión | [Autenticación y sesión](api-autenticacion-y-sesion.md) |
| Originar, transferir, retener o colgar una llamada | [Control de llamada](api-control-de-llamada.md) |
| Monitorear, intervenir o consultar el estado de agentes/colas | [Supervisión y control de agente](api-supervision-y-control-de-agente.md) |
| Importar clientes, obtener grabaciones, fijar datos adjuntos | [Datos y grabaciones](api-datos-y-grabaciones.md) |
| Recibir eventos de llamada en tiempo real | [Eventos en tiempo real de la API](eventos-tiempo-real-api.md) |

---

## Fuentes

- `raw/zh/二次开发者指南/start.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/http接口/http接口概述.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/javascript接口/javascript接口概述.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/webservice接口/webservice接口概述.txt`
- `raw/en/custom_development_guide/start.txt`
- `raw/en/custom_development_guide/apis.txt`
- `raw/en/custom_development_guide/apis/http.txt`
- `raw/en/custom_development_guide/apis/javascript.txt`
- `raw/en/custom_development_guide/apis/webservice.txt`
