---
title: "Guía de desarrollo y customización"
resumen: "Cómo integrar sistemas externos con AsterCC vía API HTTP, AMI, y pantallas emergentes por eventos."
seccion: "7. Guía de desarrollo y customización"
tipo: concepto
nivel: avanzado
roles: [desarrollador]
fuente: zh
obsoleto: false
relacionados: []
---

# Guía de desarrollo y customización

Esta sección cubre dos generaciones de mecanismos de integración de AsterCC con sistemas de terceros:

- La **API simple de acciones** (`asterccinterfaces?EVENT=...`) y la integración de pantalla emergente por eventos JavaScript — pensada para casos puntuales (originar llamada desde un botón, mostrar el CRM al timbrar).
- El **manual de interfaces v2.0** (HTTP / JavaScript / WebService) — un conjunto más completo de ~33 operaciones para construir una integración completa de escritorio de agente (sesión, control de llamada, supervisión, datos y eventos).

| Artículo | Contenido |
|---|---|
| [API y AMI](api-y-ami.md) | Referencia de la API HTTP de acciones simples y el acceso a Asterisk AMI |
| [Guía para desarrolladores](guia-desarrolladores.md) | Cómo implementar pantalla emergente (pop-up) integrando un sistema propio |
| [Introducción a la API de integración](introduccion-api-integracion.md) | Los tres protocolos del manual v2.0 (HTTP/JS/WebService), cuándo usar cada uno, formato común de petición/respuesta |
| [Códigos de retorno y codificación de idioma](codigos-retorno-e-idiomas.md) | Tabla de códigos `BackMsg_NN` y códigos de idioma |
| [API — Autenticación y sesión](api-autenticacion-y-sesion.md) | Login, logout, entrar/salir de colas, modos de trabajo y ACW, configurar extensión |
| [API — Control de llamada](api-control-de-llamada.md) | Originar, transferir, consultar, conferenciar, retener, colgar, DTMF, transferir a IVR |
| [API — Supervisión y control de agente](api-supervision-y-control-de-agente.md) | Monitorear, intervenir, interrumpir, susurrar, y consultar estados de agente/grupo/equipo |
| [API — Datos y grabaciones](api-datos-y-grabaciones.md) | Datos adjuntos a la llamada, importar clientes a una campaña, obtener grabaciones |
| [Recibir eventos en tiempo real de la API](eventos-tiempo-real-api.md) | Push al navegador (`http_push`), webhook al backend, formato del evento, depuración |
| [Integrar el envío de SMS](integrar-envio-de-sms.md) | Plataforma de SMS de terceros por HTTP, o módem GSM por puerto serie |

Ver también [Configurar Asterisk AMI](../administracion/asterisk-ami.md) para la configuración del lado de infraestructura.
