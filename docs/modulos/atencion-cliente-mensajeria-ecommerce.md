---
title: "Atención al cliente, mensajería y e-commerce"
resumen: "Configuración de atención al cliente entrante, gestión de clientes, e-commerce, fax, WeChat y mensajería masiva."
seccion: "4.10 Atención al cliente, mensajería y e-commerce"
tipo: guia
nivel: intermedio
roles: [administrador, agente]
fuente: zh
obsoleto: false
relacionados: [marcador-y-campanas, base-conocimiento-work-orders, call-center-inbound, mensajeria-wechat-fax]
---

# Atención al cliente, mensajería y e-commerce

## Qué es

Este grupo cubre los módulos orientados al cliente entrante: **atención al cliente** (post-venta, soporte, reclamos), **gestión de clientes** (fichas individuales e institucionales), y **e-commerce** (venta de productos desde la pantalla del agente). Los canales de mensajería (WeChat, fax, envío masivo) tienen su propia página de referencia: [Mensajería — WeChat, Fax y envío masivo](mensajeria-wechat-fax.md).

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

#### Productos

En **E-commerce → Gestión de productos**, cada producto define:

| Campo | Qué controla |
|---|---|
| Nombre del producto | Se recomienda que distinga variantes de venta del mismo ítem (ej. "leche 1 bolsa" vs. "leche 1 caja") |
| Publicado | Solo los productos publicados son visibles/vendibles por el agente |
| Tipo de producto | Físico, virtual, o servicio |
| Categoría | Clasificación libre del catálogo |
| Código de barras / especificación / unidad | Datos de referencia del producto |
| Cantidad | Cuántas unidades de la unidad base representa una venta — el sistema no calcula el despacho, solo registra cuántas veces se vendió el producto; la conversión a unidades de despacho es responsabilidad del negocio |
| Precio / precio de socio | Dos tarifas posibles por venta — el agente elige cuál aplica según indique el negocio |
| Vigencia (inicio/fin) | Solo informativa, para productos con periodo de validez (ej. garantías) |
| Prioridad | Los productos con mayor prioridad aparecen primero en la lista del agente — útil para poner los más vendidos en la primera página y reducir tiempo de búsqueda |
| Producto relacionado | Vincula a otro producto del mismo catálogo |
| Descripción funcional | Para que el agente pueda responder preguntas del cliente sobre el producto |

#### Pedidos (recientes e históricos)

Los pedidos se dividen en dos tablas — **recientes** e **históricos** — según el tiempo de retención configurado en **Sistema → Configuración → Procesamiento de grandes datos → Retención de datos de e-commerce**. Ambas comparten la misma estructura, con cuatro pestañas al editar un pedido:

| Pestaña | Contenido |
|---|---|
| Información básica | Número de pedido, módulo/negocio de origen, cliente, estado, precio original, descuento, monto a cobrar, si requiere factura, fechas de envío/entrega, agente y equipo que lo creó |
| Datos del destinatario | A quién y dónde se envía |
| Datos de envío | Transportista, guía, estado del envío |
| Productos comprados | Detalle de líneas del pedido |

No se pueden crear pedidos manualmente desde esta pantalla — solo se editan, exportan o eliminan; los pedidos nuevos se generan desde la pantalla emergente del agente durante una llamada.

#### Registro de ventas (recientes e históricos)

Complementario a los pedidos: mientras un pedido agrupa la operación completa, el **registro de ventas** detalla cada línea de producto vendida (producto, cantidad, precio, descuento, monto, agente, fechas) — útil para reportes por producto en vez de por pedido.

#### Logística

En **E-commerce → Logística**, se asignan zonas de despacho a un almacén:

| Campo | Qué define |
|---|---|
| Nombre de la zona | Identificación libre |
| Almacén | A qué almacén pertenece esta zona |
| Grupo logístico | Qué grupo de agentes gestiona esta zona |
| Equipo | A qué equipo pertenece |
| Agente responsable | Quién(es) del grupo gestiona(n) específicamente esta zona |
| Provincia / ciudad | Cobertura geográfica de la zona |

!!! warning
    Si una zona no define provincia/ciudad, cubre **todo el país** — en ese caso no puede existir una segunda zona sin provincia/ciudad para el mismo almacén, porque el sistema no podría decidir a cuál asignar un pedido nuevo. Para logística multi-almacén por región, se recomienda crear campos personalizados de tipo "relación" en el pedido (provincia/ciudad/distrito del destinatario) en vez de depender solo de esta pantalla.

Una vez creado, se vincula el catálogo a una tarea de campaña o a un servicio de atención al cliente para que el agente genere pedidos directamente desde la ficha del cliente durante la llamada.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear servicio de atención al cliente | Atención al cliente → Atención al cliente |
| Gestionar clientes individuales/institucionales | Gestión de clientes |
| Crear catálogo de e-commerce | E-commerce → E-commerce |
| Gestionar productos | E-commerce → Gestión de productos |
| Ver pedidos | E-commerce → Pedidos recientes / históricos |
| Configurar zonas de despacho | E-commerce → Logística |
| WeChat, Fax, envío masivo | Ver [Mensajería — WeChat, Fax y envío masivo](mensajeria-wechat-fax.md) |

---

## Fuentes

- `raw/zh/模块使用说明/呼入客服/呼入客服.txt`
- `raw/zh/模块使用说明/电子商务/电子商务.txt`
- `raw/zh/模块使用说明/电子商务/产品管理.txt`
- `raw/zh/模块使用说明/电子商务/近期订单.txt`
- `raw/zh/模块使用说明/电子商务/历史订单.txt`
- `raw/zh/模块使用说明/电子商务/近期售卖记录.txt`
- `raw/zh/模块使用说明/电子商务/历史售卖记录.txt`
- `raw/zh/模块使用说明/电子商务/物流管理.txt`