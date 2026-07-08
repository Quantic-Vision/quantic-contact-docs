---
title: "¿Qué es AsterCC?"
resumen: "Descripción general de AsterCC como plataforma de call center basada en Asterisk."
seccion: "1.1 ¿Qué es AsterCC?"
tipo: concepto
nivel: basico
roles: [administrador, agente, desarrollador]
fuente: zh+en
obsoleto: false
relacionados: [funcionalidades, arquitectura-general]
---

# ¿Qué es AsterCC?

## Qué es

AsterCC es un sistema de **contact center** construido sobre [Asterisk](../glosario.md#asterisk), que además incorpora funciones de **CRM** (gestión de relación con el cliente). Entre sus capacidades más usadas están:

- Pantalla emergente (pop-up) con la ficha del cliente al recibir o realizar una llamada.
- Grabación de llamadas.
- Menús de voz interactivos ([IVR](../glosario.md)).
- [Colas](../glosario.md#cola-grupo-de-agentes) de llamadas.

Con AsterCC, cada llamada de un cliente queda registrada: cuando ese cliente vuelve a llamar, su información y su historial de contacto aparecen automáticamente en pantalla. También es posible diseñar un IVR de autoservicio para que el cliente resuelva consultas sin necesidad de un agente. El módulo de reportes permite además extraer información clave a partir de miles de llamadas.

AsterCC también ofrece herramientas prácticas adicionales: programación y recordatorio de tareas, difusión de campañas por teléfono/SMS/correo, y consulta de ubicaciones o rutas mediante mapas en línea.

## Integración con sistemas propios

Si tu organización ya tiene un sistema de negocio propio, AsterCC puede integrarse con él a través de su **interfaz de desarrollo secundario** (ver [Guía de desarrollo y customización](../desarrollo/index.md)). Por ejemplo, es posible mostrar la ficha del cliente proveniente de tu propio sistema cuando entra una llamada.

## Para proveedores de servicio

AsterCC soporta el modo **SaaS**: un mismo sistema puede dar servicio a múltiples clientes de forma aislada, tanto en su función de call center como en su función de central telefónica (PBX). Esto lo hace una opción habitual para proveedores de servicio que ofrecen call center o PBX como servicio (hosted call center / hosted PBX).

## Referencia rápida

| Aspecto | Detalle |
|---|---|
| Base tecnológica | [Asterisk](../glosario.md#asterisk) |
| Tipo de sistema | Contact center + CRM |
| Modo multiempresa | Sí (SaaS) |
| Integración con sistemas propios | Sí, vía interfaz de desarrollo secundario |

Para el detalle completo de funciones, ver [Funcionalidades del sistema](funcionalidades.md). Para entender cómo se organizan estas funciones internamente, ver [Arquitectura general](arquitectura-general.md).

---

## Fuentes

- `raw/zh/start.txt`
- `raw/en/start.txt`