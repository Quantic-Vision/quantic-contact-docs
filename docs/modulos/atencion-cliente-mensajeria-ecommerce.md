---
title: "Atención al cliente, mensajería y e-commerce"
resumen: "Configuración de atención al cliente entrante, gestión de clientes, e-commerce, fax, WeChat y mensajería masiva."
seccion: "4.10 Atención al cliente, mensajería y e-commerce"
tipo: guia
nivel: intermedio
roles: [administrador, agente]
fuente: zh
obsoleto: false
relacionados: [marcador-y-campanas, base-conocimiento-work-orders, call-center-inbound]
---

# Atención al cliente, mensajería y e-commerce

## Qué es

Este grupo cubre los módulos orientados al cliente entrante y a canales de comunicación adicionales: **atención al cliente** (post-venta, soporte, reclamos), **gestión de clientes** (fichas individuales e institucionales), **e-commerce** (venta de productos desde la pantalla del agente), y canales de mensajería (**correo/SMS masivo, WeChat, fax**).

## Cómo se usa

### Atención al cliente entrante

En **Atención al cliente → Atención al cliente → Agregar**, se define un "servicio" con:

| Campo | Qué controla |
|---|---|
| Nombre del servicio | Identifica el propósito del servicio (ej. "Soporte técnico", "Reclamos") |
| Grupo de agentes | Quién atiende este servicio |
| Enlace de trabajo | Página que se muestra al agente cuando entra la llamada |
| Cargar historial por defecto | Si se recomienda desactivar para no sobrecargar el servidor cuando no es necesario |
| Prioridad de tipo de cliente nuevo | Si el alta por defecto es cliente individual, institucional, o con preferencia configurable |
| E-commerce asociado | Habilita operaciones de venta desde la ficha del cliente |
| Número/nombre que llama | Configurable a nivel del servicio, con la misma jerarquía de prioridad que en campañas (agente > extensión > servicio, salvo que se fuerce) |

Un mismo servicio puede tener **varios grupos de agentes**, cada uno con su propia pantalla y su propio **motivo de llamada por defecto** — típico cuando un IVR deriva "consultas" a un grupo y "reclamos" a otro, dentro del mismo servicio de atención al cliente.

Los clientes de atención al cliente **son los mismos** que los de [gestión de clientes](#gestion-de-clientes) (individual/institucional) — no hay una tabla de clientes separada por servicio.

### Gestión de clientes

- **Cliente individual / institucional:** dos tipos de ficha de cliente en el sistema, cada una con sus propios campos personalizados y etiquetas.
- **Etiquetas de cliente:** clasificación libre para segmentar o filtrar clientes.
- **Registro de contacto:** historial de todas las interacciones con un cliente, sin importar si vinieron de atención al cliente o de una campaña.
- **Campos personalizados y configuración de la tabla general:** permiten adaptar qué información se captura por cliente según el negocio.

### E-commerce

En **E-commerce → E-commerce → Agregar** se crea un "catálogo" de venta:

| Campo | Qué controla |
|---|---|
| Nombre del catálogo | Ej. "Suplementos", "Electrónica" — se pueden tener varios catálogos independientes |
| Equipo | A qué equipo pertenece |
| Origen | Canal de la venta (saliente, entrante, revista, internet, etc.) |

Una vez creado, se administran **productos**, **pedidos recientes/históricos** y **logística de envío** dentro de ese catálogo. El catálogo se vincula luego a una tarea de campaña o a un servicio de atención al cliente para que el agente pueda generar pedidos directamente desde la ficha del cliente durante la llamada.

### Mensajería masiva

- **Plantillas de mensaje:** para SMS y correo reutilizables.
- **Envío masivo:** dispara una plantilla a un conjunto de destinatarios; queda registrado en **mensajes por enviar**, **mensajes enviados** y **archivo de mensajes**.
- **Mensajería interna:** anuncios y mensajes internos entre cuentas del sistema, distinto de la mensajería hacia clientes.
- **Servidores de correo y SMS:** configuración de las pasarelas usadas para el envío.

### WeChat y Fax

- **WeChat:** administración de cuentas oficiales de WeChat vinculadas y de sus menús interactivos, para atender consultas desde ese canal.
- **Fax:** gestión de dispositivos de fax, envío de fax, y registro de faxes recibidos/enviados — útil en flujos que aún dependen de este canal (contratos, comprobantes).

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear servicio de atención al cliente | Atención al cliente → Atención al cliente |
| Gestionar clientes individuales/institucionales | Gestión de clientes |
| Crear catálogo de e-commerce | E-commerce → E-commerce |
| Enviar mensajería masiva | Mensajería → Envío masivo |
| Configurar WeChat | Mensajería → WeChat |
| Enviar/gestionar fax | Mensajería → Fax |

---

*Fuentes: `raw/zh/模块使用说明/呼入客服/呼入客服.txt`, `raw/zh/模块使用说明/电子商务/电子商务.txt`.*
