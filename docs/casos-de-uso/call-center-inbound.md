---
title: "Call center de atención al cliente (inbound)"
resumen: "Caso de uso completo: montar atención al cliente entrante con pantalla emergente, historial y work orders."
seccion: "5.1 Call center de atención al cliente (inbound)"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, atencion-cliente-mensajeria-ecommerce, base-conocimiento-work-orders]
---

# Call center de atención al cliente (inbound)

## Qué es

Caso de uso de referencia para armar un servicio de atención al cliente entrante: el cliente llama, el agente ve automáticamente su ficha (o el formulario de alta si es nuevo), y puede registrar el contacto, abrir un work order o vender un producto sin salir de la misma pantalla.

## Cómo se usa

### 1. Preparar la telefonía

1. Da de alta el [troncal](../modulos/pbx-y-telefonia.md#troncales-y-grupos-de-troncales) por el que entrarán las llamadas.
2. Crea el [grupo de agentes](../modulos/cuentas-equipos-permisos.md) que atenderá este servicio, con su cola asociada.
3. Si manejas más de una línea de negocio, da de alta un [DID](../modulos/pbx-y-telefonia.md#did-y-rutas-entrantessalientes) por línea, para poder distinguir a qué servicio corresponde cada llamada.
4. Crea la [ruta entrante](../modulos/pbx-y-telefonia.md#did-y-rutas-entrantessalientes) que conecta ese DID (o el troncal directamente, si no usas DID) con la cola del paso 2.

### 2. Crear el servicio de atención al cliente

Sigue [4.10 Atención al cliente](../modulos/atencion-cliente-mensajeria-ecommerce.md#atencion-al-cliente-entrante) para dar de alta el servicio, apuntando al grupo de agentes recién creado.

### 3. Qué ve el agente al recibir la llamada

- **Cliente nuevo:** se abre el formulario de alta, mostrando el número que llama, su ubicación geográfica (si está cargada) y la hora de la llamada. El agente puede buscar primero si ese número ya pertenece a un cliente existente antes de crear uno duplicado — y de encontrarlo, vincular el número a ese cliente en lugar de crear uno nuevo.
- **Cliente existente:** se abre directamente su ficha, con pestañas de **historial de contacto**, **work orders no completados**, **work orders completados recientemente** y **work orders completados históricos**.
- En ambos casos, el agente registra el **motivo de la llamada** al finalizar — si ese motivo está vinculado a una plantilla de work order, aparece la opción de crear uno directamente desde ahí.

### 4. Combinar con otros módulos (opcional)

- **Work orders:** vincula un motivo de llamada a una plantilla de [work order](../modulos/base-conocimiento-work-orders.md#work-orders) para que el agente pueda escalar un caso a otro equipo sin salir de la pantalla de atención.
- **E-commerce:** si el servicio tiene un catálogo de [e-commerce](../modulos/atencion-cliente-mensajeria-ecommerce.md#e-commerce) vinculado, el agente puede buscar productos, armar un pedido, y guardarlo con los datos de envío precargados desde la ficha del cliente — incluyendo consultar el historial de compras del cliente bajo demanda.

## Referencia rápida

| Paso | Módulo relacionado |
|---|---|
| Troncal + ruta entrante | [4.1 PBX y telefonía](../modulos/pbx-y-telefonia.md) |
| Grupo de agentes | [4.3 Cuentas, equipos y permisos](../modulos/cuentas-equipos-permisos.md) |
| Servicio de atención al cliente | [4.10 Atención al cliente](../modulos/atencion-cliente-mensajeria-ecommerce.md) |
| Escalar a otro equipo | [4.6 Work Orders](../modulos/base-conocimiento-work-orders.md) |
| Vender durante la llamada | [4.10 E-commerce](../modulos/atencion-cliente-mensajeria-ecommerce.md#e-commerce) |

---

*Fuentes: `raw/zh/用途和案例/呼入客服的配置弹屏和简单使用.txt`, `raw/zh/用途和案例/如何在呼入客服系统中使用电子商务.txt`.*
