---
title: "Marcador y campañas"
resumen: "Cómo configurar una tarea de marketing saliente y el marcador predictivo."
seccion: "4.2 Marcador y campañas"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, marketing-outbound, marcacion-predictiva]
---

# Marcador y campañas

## Qué es

Este módulo configura las **tareas de marketing saliente** (campañas): a qué [paquete de clientes](../glosario.md#paquete-de-clientes-para-marcacion-saliente) llama la campaña, qué agentes participan, qué modo de marcación usan, y —opcionalmente— el **marcador predictivo** que automatiza el proceso de llamar antes de que el agente lo pida.

## Cómo se usa

### 1. Crear una tarea de campaña

En **Marketing outbound → Tareas de campaña**, al crear una nueva tarea defines, entre otros:

| Campo | Qué controla |
|---|---|
| Tipo de paquete de clientes | Cliente individual o cliente institucional |
| Paquete de clientes | Uno nuevo, la tabla general del equipo, o un paquete ya existente |
| Paquete de horario de trabajo | En qué horario está activa la campaña |
| Encuesta asociada | Encuesta que se dispara al abrir la ficha del cliente |
| Equipo y grupo de agentes | Quién ejecuta la tarea |
| Obtención de datos por el agente | Si el agente puede pedir manualmente un cliente, o solo recibe lo asignado |
| Permitir agregar clientes nuevos | Si el agente puede dar de alta clientes durante la llamada |
| E-commerce asociado | Vincula un catálogo para generar pedidos desde la ficha del cliente |

### 2. Elegir el modo de marcación

| Modo | Cómo funciona |
|---|---|
| Manual (por defecto) | El agente hace doble clic en el cliente, ve su ficha, y marca manualmente |
| Preview | El agente ve la ficha y el sistema marca automáticamente |
| Automático | El agente inicia su turno; el sistema muestra la ficha y marca sin intervención, avanzando al siguiente cliente tras cada llamada según un intervalo configurable |
| A elección del agente | El agente puede alternar entre los tres modos anteriores |

Parámetros asociados al modo automático: **intervalo entre llamadas**, **cantidad de reintentos**, y **segundos de prórroga** (para cuando el agente necesita más tiempo antes de la siguiente llamada).

### 3. Configurar el marcador predictivo (opcional)

Si la tarea usa marcación predictiva, se configura por separado en **Marcador → Configuración del marcador**:

- **Cuentas y límites de concurrencia:** existen tres niveles de límite — licencia del sistema, límite por equipo (configurado aquí), y límite por tarea de campaña. Ningún nivel puede superar al que está por encima.
- **Regla de marcación:** define si el operador del marcador puede elegir libremente entre "por concurrencia" y "por agentes disponibles", o si se fuerza una de las dos.
- **Destino al contestar:** a qué se transfiere la llamada cuando el cliente contesta — al grupo de agentes directamente, o a un IVR primero.
- **Parámros de predicción:** duración promedio de timbrado, duración promedio de llamada, tasa de contactación esperada, tiempo de gestión posterior, y definición de "llamada corta" (para ajustar el algoritmo de predicción y evitar que sobren o falten llamadas para los agentes disponibles).

Ver también [Marcación predictiva](../casos-de-uso/marcacion-predictiva.md) para un caso de uso aplicado.

### 4. Asignar clientes a los agentes

Dos formas de asignar el paquete de clientes de una tarea a los agentes del grupo:

- **Asignación automática:** ideal para lotes grandes — se define qué porcentaje del total recibe cada agente (o se reparte por "pendientes" o "sin asignar"), y el sistema ejecuta la asignación en segundo plano.
- **Asignación manual:** ideal para ajustes puntuales — por ejemplo, mover una parte de los clientes de un agente a otro con mejor desempeño, o aislar un segmento específico para un agente en particular.

### 5. Configurar qué ve el agente

Desde la tarea ya creada, dos botones controlan la visibilidad de campos:

- **Configuración de campos para el agente (frontend):** qué campos del cliente puede ver, editar, y cuáles son obligatorios.
- **Configuración de campos para administración (backend):** qué campos ve el equipo de operaciones y cuáles se usan al exportar.

## Otras funciones del módulo

- **Gestión de resultados de llamada:** catálogo de resultados que el agente asigna a cada contacto (éxito, no contesta, número equivocado, DNC, etc.). El resultado DNC agrega automáticamente el número a la lista de no llamar.
- **Lista negra de marcación y filtros de lista negra**, para excluir números antes de marcar.
- **Monitoreo de volumen de datos:** cuántos clientes hay pendientes, en proceso, completados.
- **Gestión y estándares de control de calidad**, para que un supervisor califique llamadas de la campaña contra criterios definidos.
- **Reportes estadísticos** específicos de campañas.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear/editar tarea de campaña | Marketing outbound → Tareas de campaña |
| Configurar marcador predictivo | Marcador → Configuración del marcador |
| Asignar clientes | Dentro de la tarea → Asignación automática / manual |
| Resultados de llamada | Marketing outbound → Gestión de resultados |
| Control de calidad | Marketing outbound → Gestión de control de calidad |

---

*Fuentes: `raw/zh/模块使用说明/外呼营销/外呼营销任务.txt`, `raw/zh/模块使用说明/预拨号/拨号器设置.txt`.*
