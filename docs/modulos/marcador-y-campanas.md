---
title: "Marcador y campañas"
resumen: "Cómo configurar una tarea de marketing saliente y el marcador predictivo."
seccion: "4.2 Marcador y campañas"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, marcador-predictivo-avanzado, marketing-outbound, marcacion-predictiva]
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

### Pantalla emergente del agente (resumen)

Al abrir la ficha de un cliente durante una campaña, el agente ve pestañas de **historial de contacto**, y si la tarea usa la tabla general de clientes, también **work orders no completados**, **completados recientemente** y **completados históricos** — igual mecánica que en [atención al cliente entrante](atencion-cliente-mensajeria-ecommerce.md#atencion-al-cliente-entrante). Si el resultado de llamada elegido está vinculado a una plantilla de work order, aparece un enlace para crear uno sin salir de la ficha. Si el cliente es individual y pertenece a una organización, también puede consultarse la ficha de esa organización desde la misma pantalla.

### 6. Paquete de clientes en detalle

El [paquete de clientes](../glosario.md#paquete-de-clientes-para-marcacion-saliente) es una tabla independiente generada al crear la tarea (o reutilizada, si se elige un paquete existente).

| Campo | Qué define |
|---|---|
| Estado | "Sin tarea asignada" o "en progreso con una tarea" |
| Tipo de paquete | Cliente individual o institucional — determina la estructura de la tabla y de dónde toma los datos |
| Usar tabla general del cliente | Si el paquete refleja la tabla general del equipo en vez de ser una copia independiente |
| Total de clientes / completados | Contadores informativos del paquete |
| Clave única | Campo(s) que evitan duplicados al importar o agregar manualmente (por defecto, "teléfono uno") |
| Índice | Campos de búsqueda frecuente marcados para acelerar consultas (por defecto, "teléfono uno" y "teléfono dos") |
| Equipo | Solo ese equipo puede usar este paquete en una tarea |

!!! tip
    Si "usar tabla general" está activo, no se puede seleccionar clientes manualmente desde el paquete (se nutre automáticamente de la tabla general). Si está inactivo, se puede usar "seleccionar clientes" para copiar registros puntuales — o todos — desde la tabla general del equipo hacia este paquete.

No se puede cambiar la clave única si ya existen duplicados en el paquete — hay que depurarlos primero desde **Gestión de clientes** de la tarea.

### 7. Registro de llamadas de la campaña

Cada llamada de la tarea queda en su propio registro, con campos como número de teléfono usado, marca de tiempo de solicitud de marcado (solo aplica a predictivo), tiempo de respuesta del cliente vs. del agente, ruta que siguió la llamada dentro del sistema (ej. `entersystem,queue3,AGENT:8000`), y el estado de marcación en el momento de colgar (pendiente, timbrando cliente, timbrando agente, etc.). Permite escuchar/descargar grabación individualmente, o exportar en lote por rango de búsqueda (con la opción de borrar el archivo original del servidor tras exportarlo, para liberar espacio).

### 8. Gestión de clientes de la tarea

Pantalla para buscar, agregar, editar y eliminar clientes dentro del paquete de una tarea específica — los campos visibles siguen la configuración de "campos para administración" del paso 5. Incluye una función de **detección de duplicados** por el campo que se elija, y dos modos de eliminación:
- Eliminar solo de la lista de marcación (predial) — el cliente permanece en el paquete.
- Eliminar del paquete completo (predial + tabla base).

## Otras funciones del módulo

### Gestión de resultados de llamada

Catálogo de resultados que el agente asigna tras cada contacto (ej. "no coopera", "sin tiempo", "número equivocado"). Cada resultado se puede asociar a:

- Un **estado de procesamiento** (todos / sin procesar / en seguimiento / fallido / exitoso) — el resultado solo aparece en pantalla cuando el agente elige ese estado.
- Si la llamada fue **contestada o no** — la lista de resultados disponibles cambia según esto.
- Un **equipo** y/o **tarea específica** — para acotar qué resultados ve cada quien.
- Una **plantilla de work order** — si se asocia, el agente puede crear directamente un work order al elegir ese resultado (solo disponible si la tarea usa la tabla general de clientes).

### DNC — lista de no llamar, en tres niveles

Un número marcado como DNC (do-not-call) se filtra automáticamente del paquete de clientes en el nivel correspondiente:

| Nivel | Alcance |
|---|---|
| Sistema | Filtra a todos los equipos |
| Equipo | Filtra solo dentro de ese equipo |
| Tarea de campaña | Filtra solo dentro de esa tarea |

La carga de números al DNC se hace por importación (en **Administración avanzada del call center → Importación**), eligiendo el nivel según se seleccione equipo y/o tarea. También se pueden agregar números manualmente (uno por línea) o vaciar por completo un nivel de lista.

### Plan de filtrado de lista negra (automatización del DNC)

En vez de importar manualmente, se puede programar que el sistema filtre periódicamente el paquete de una tarea contra el DNC vigente — define equipo, tarea, y horario de ejecución (se puede editar y reactivar). Cada corrida deja disponible para descarga el listado de clientes que fueron filtrados esa vez.

### Control de calidad

En **Gestión de control de calidad**, se elige la tarea (y encuesta, si aplica) para revisar contactos uno por uno: escuchar la grabación, ver la ficha y las respuestas de encuesta, y marcar el contacto como aprobado o no — con opción de **calificar** con puntaje si hay estándares de calidad definidos.

**Estándares de control de calidad:** catálogo de criterios de puntaje (suma o resta), acotable por equipo y/o tarea — por ejemplo, una rúbrica de 100 puntos donde cada criterio aprobado suma.

**Exportar grabaciones en lote:** desde control de calidad, filtrando por tarea + estado "enviado con éxito" (el caso típico cuando un cliente externo pide auditar solo las llamadas exitosas), se puede generar un paquete descargable de audios — con la misma opción de descarga vía web o FTP que el registro de llamadas.

### Monitoreo de volumen de datos

Vista rápida por tarea: total de clientes, cuántos se importaron, cuántos ya se marcaron, cuántos resultaron en éxito, cuántos faltan por marcar, cuántos quedan en la lista de marcación predictiva, y cuándo fue la última vez que se recuperaron datos hacia esa lista.

### Estadísticas de la campaña

Reporte agregable por tarea o por agente, en un rango de fechas, con indicadores como: clientes/llamadas totales, tasa de contactación (por cliente y por intento), duración total y de conversación, desglose por cada resultado de llamada configurado, cuántas quedaron sin guardar, inválidas, en seguimiento, exitosas (antes y después de control de calidad), y cuántas de las exitosas pasaron o no la revisión de calidad.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear/editar tarea de campaña | Marketing outbound → Tareas de campaña |
| Configurar marcador predictivo | Marcador → Configuración del marcador (ver también [Marcador predictivo — referencia avanzada](marcador-predictivo-avanzado.md)) |
| Asignar clientes | Dentro de la tarea → Asignación automática / manual |
| Resultados de llamada | Marketing outbound → Gestión de resultados |
| Gestionar el paquete de clientes | Marketing outbound → Gestión de paquetes de clientes |
| Cargar/gestionar DNC | Marketing outbound → Lista negra de marcación / Plan de filtrado |
| Control de calidad | Marketing outbound → Gestión de control de calidad |
| Ver registro de llamadas de la tarea | Marketing outbound → Registro de llamadas |
| Estadísticas de campaña | Marketing outbound → Reportes estadísticos |

---

## Fuentes

- `raw/zh/模块使用说明/外呼营销.txt`
- `raw/zh/模块使用说明/外呼营销/外呼营销任务.txt`
- `raw/zh/模块使用说明/外呼营销/客户集合包管理.txt`
- `raw/zh/模块使用说明/外呼营销/呼叫结果管理.txt`
- `raw/zh/模块使用说明/外呼营销/禁拨黑名单.txt`
- `raw/zh/模块使用说明/外呼营销/黑名单过滤计划.txt`
- `raw/zh/模块使用说明/外呼营销/质检管理.txt`
- `raw/zh/模块使用说明/外呼营销/质检标准管理.txt`
- `raw/zh/模块使用说明/外呼营销/数据量监控.txt`
- `raw/zh/模块使用说明/外呼营销/统计报表.txt`
- `raw/zh/模块使用说明/外呼营销/呼叫记录.txt`
- `raw/zh/模块使用说明/外呼营销/客户管理.txt`
- `raw/zh/模块使用说明/外呼营销/坐席界面.txt`
- `raw/zh/模块使用说明/预拨号/拨号器设置.txt`