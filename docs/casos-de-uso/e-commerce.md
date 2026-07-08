---
title: "E-commerce"
resumen: "Caso de uso: vender productos desde la pantalla del agente durante una llamada entrante."
seccion: "5.3 E-commerce"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [atencion-cliente-mensajeria-ecommerce, call-center-inbound]
---

# E-commerce

## Qué es

Caso de uso para habilitar venta de productos directamente desde la ficha del cliente, típicamente combinado con [atención al cliente entrante](call-center-inbound.md) o con una [campaña saliente](marketing-outbound.md).

## Cómo se usa

### 1. Instalar el módulo (si no está instalado)

Ve a **Sistema → Gestión de módulos** y confirma que el módulo de e-commerce esté instalado.

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

## Referencia rápida

| Campo del pedido | Qué registra |
|---|---|
| Número de pedido | Identificador único |
| Módulo / negocio del módulo | De qué servicio o tarea de campaña vino el pedido |
| Producto, cantidad, precio, descuento | Detalle de la línea vendida |
| Monto total a cobrar | Resultado final por línea |
| Agente y fecha de creación | Trazabilidad de la venta |

---

*Fuentes: `raw/zh/用途和案例/如何在呼入客服系统中使用电子商务.txt`, `raw/zh/模块使用说明/电子商务/电子商务.txt`.*
