---
title: "E-commerce"
resumen: "Caso de uso: vender productos desde la pantalla del agente durante una llamada entrante."
seccion: "5.3 E-commerce"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [atencion-cliente-mensajeria-ecommerce, call-center-inbound, marketing-outbound]
---

# E-commerce

## Qué es

Caso de uso para habilitar venta de productos directamente desde la ficha del cliente, típicamente combinado con [atención al cliente entrante](call-center-inbound.md) o con una [campaña saliente](marketing-outbound.md).

> La aplicación de **atención al cliente entrante** (呼入客服) sobre la que normalmente corre este caso de uso se distingue de la de [oficina virtual](oficina-virtual.md) en un punto relevante para el historial de compras: usa la **tabla de clientes única y compartida del sistema**, en vez de una tabla de clientes independiente por aplicación. Es decir, los datos del cliente (y su historial de compras de e-commerce) son los mismos sin importar por cuál servicio de atención al cliente entrante haya llamado antes.

## Cómo se usa

### 1. Instalar el módulo (si no está instalado)

Ve a **Sistema → Gestión de módulos** y confirma que el módulo de e-commerce esté instalado.

> Las dos guías en inglés sobre e-commerce en atención al cliente describen exactamente este mismo procedimiento (instalar el módulo → crear el catálogo de e-commerce → cargar productos → vincular el catálogo al servicio de atención entrante → vender desde la pantalla emergente, dividida en dos páginas de scroll por lo extenso del contenido) sin aportar pasos adicionales — se citan como confirmación cruzada del flujo ya descrito en esta sección y en las secciones 2 a 5.

### 2. Crear el catálogo de e-commerce

En **E-commerce → E-commerce → Agregar**, crea una categoría de venta (por ejemplo, una por línea de producto) — ver [4.10 E-commerce](../modulos/atencion-cliente-mensajeria-ecommerce.md#e-commerce).

### 3. Cargar productos

En **E-commerce → Gestión de productos**, elige el catálogo recién creado en la parte superior y agrega los productos que va a poder vender el agente.

### 4. Vincular el catálogo a un servicio

Tanto en atención al cliente entrante como en una tarea de campaña saliente, existe un campo para asociar un catálogo de e-commerce. Una vez vinculado, el catálogo aparece en la pantalla emergente del agente cuando atiende a un cliente de ese servicio o tarea.

### 5. Vender durante la llamada

En la ficha del cliente, la sección de e-commerce permite:

1. **Buscar productos** por nombre, tipo o código de barras.
2. **Agregar al pedido** los productos encontrados — el pedido en curso se arma en una lista aparte.
3. **Ajustar** precio, cantidad y descuento de cada línea antes de confirmar.
4. **Guardar el pedido**, con los datos de envío precargados desde la ficha del cliente (el agente puede corregirlos si el envío es a otra persona/dirección).
5. **Consultar el historial de compras** del cliente bajo demanda (no se carga automáticamente, para no afectar el rendimiento).

### Vender durante una campaña saliente

Al crear o editar una tarea de [campaña saliente](marketing-outbound.md), el mismo campo de catálogo de e-commerce descrito en el paso 4 permite vincular un catálogo específico a esa tarea de marcación (en vez de a un servicio de atención entrante). Una vez vinculado:

- El pop-up del cliente que ve el agente en la plataforma de trabajo del agente durante esa tarea muestra la sección de e-commerce, siempre que el módulo esté instalado y la tarea tenga un catálogo vinculado.
- Cada pedido generado queda etiquetado con el módulo y la tarea/negocio de origen (por ejemplo, la campaña saliente específica), lo que permite distinguirlo de pedidos generados desde atención entrante que use el mismo catálogo — ver la columna "Módulo / negocio del módulo" en la referencia rápida.

**Consultar pedidos y ventas por catálogo**

En **E-commerce → Pedidos recientes** y **E-commerce → Registro de ventas recientes**, selecciona el catálogo en el desplegable superior para ver todos los pedidos o ventas generados desde cualquier módulo que use ese catálogo (campaña saliente, atención entrante, etc.), no solo los de la tarea saliente.

**Retención de datos**

En **Sistema → Configuración → Procesamiento de datos masivos**, el parámetro de retención de datos de e-commerce controla cuánto tiempo se conservan los pedidos y registros de venta antes de moverse automáticamente a **Pedidos históricos** y **Registro de ventas histórico**.

## Referencia rápida

| Campo del pedido | Qué registra |
|---|---|
| Número de pedido | Identificador único |
| Módulo / negocio del módulo | De qué servicio o tarea de campaña vino el pedido |
| Producto, cantidad, precio, descuento | Detalle de la línea vendida |
| Monto total a cobrar | Resultado final por línea |
| Agente y fecha de creación | Trazabilidad de la venta |

---

## Fuentes

- `raw/zh/用途和案例/如何在呼入客服系统中使用电子商务.txt`
- `raw/zh/模块使用说明/电子商务/电子商务.txt`
- `raw/zh/用途和案例/在外呼营销中使用电子商务模块.txt`
- `raw/en/how-to/how_to_config_e-commerce_for_customer_service.txt`
- `raw/en/how-to/how_to_use_e_commerce_in_customer_service_module.txt`
- `raw/zh/电子商务.txt`