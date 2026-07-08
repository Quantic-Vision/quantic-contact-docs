---
title: "Encuestas y cuestionarios"
resumen: "Cómo armar una encuesta con lógica condicional y cuotas, y usarla en una campaña o en atención al cliente."
seccion: "4.5 Encuestas y cuestionarios"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [marcador-y-campanas, atencion-cliente-mensajeria-ecommerce]
---

# Encuestas y cuestionarios

## Qué es

El módulo de encuestas permite crear cuestionarios con grupos de preguntas, lógica condicional entre preguntas, y cuotas de respuesta — usables tanto en campañas de marketing saliente como en atención al cliente entrante.

## Cómo se usa

### 1. Crear la encuesta

En **Encuestas → Gestión de encuestas → Agregar**, define:

| Campo | Qué controla |
|---|---|
| Equipo | A qué equipo pertenece (campañas y atención al cliente solo pueden usar encuestas de su propio equipo) |
| Tipo | Normal (texto) o de voz — determina si el saludo/cierre son texto o audio |
| Cuota | Si se activa el límite de respuestas (ver más abajo) |
| Copiar de encuesta existente | Permite clonar grupos, preguntas y opciones de otra encuesta como punto de partida |
| Saludo / cierre | Texto (o audio) que el agente usa para introducir y cerrar la encuesta |

Una encuesta queda en estado **libre** hasta que una campaña o el módulo de atención al cliente la selecciona — en ese momento pasa a **asignada** y no puede ser tomada por otra tarea al mismo tiempo.

### 2. Definir grupos y preguntas

- **Grupos de preguntas:** agrupan preguntas relacionadas (ej. "filtro", "cuerpo", "datos del cliente"); pueden mostrarse en orden aleatorio.
- **Tipos de pregunta:**

| Tipo | Comportamiento |
|---|---|
| Opción única | Una sola respuesta posible |
| Opción múltiple | Varias respuestas, con mínimo/máximo configurable |
| Combinada | Varias sub-preguntas que comparten el mismo set de opciones (tipo matriz) |
| Texto libre | Campo abierto para respuestas largas |

- **Referenciar datos del cliente:** una pregunta puede autocompletarse con un dato ya existente en la ficha del cliente (por ejemplo, si el campo "marca de auto" del cliente es "Toyota", la opción correspondiente se marca sola). Se puede permitir o no que el agente edite esa respuesta autocompletada.

### 3. Ordenar y enlazar preguntas

- El **orden de preguntas** se define por grupo y luego dentro del grupo — arrastrando para reordenar.
- El **relleno de preguntas** permite insertar la respuesta de una pregunta anterior dentro del texto de una posterior, usando el marcador `[FILL]` (ej.: *"¿A través de qué medios conoció la marca [FILL]?"*, donde `[FILL]` se sustituye por la respuesta de una pregunta previa sobre marca).

### 4. Lógica condicional

Permite saltar preguntas, ocultar preguntas u ocultar opciones según respuestas anteriores:

1. Elige qué pregunta dispara la lógica.
2. Define la condición (es igual a / contiene alguna de / no contiene ninguna de ciertas opciones).
3. Define la acción: **saltar a otra pregunta**, **ocultar una pregunta**, u **ocultar una opción**.
4. Define el objetivo de esa acción.

Usa la función de **vista previa de encuesta** para simular el recorrido de un agente y validar que la lógica funciona como se espera.

### 5. Cuotas

Solo disponibles si la encuesta tiene la cuota activada. Sirven para dejar de encuestar sobre un segmento una vez alcanzado un número de respuestas — evita gastar tiempo de agente en cuotas ya cubiertas. Dos formas de definir una cuota:

- **Por encuesta/pregunta/opción:** por ejemplo, "solo 1000 respuestas totales", o "solo 500 respuestas a la pregunta 2", o "solo 200 que elijan la opción B de la pregunta 3".
- **Por dato del cliente:** por ejemplo, "solo 1000 clientes de una ciudad + operador específico", o "solo 500 hombres".

Cada cuota admite un **margen de sobrecupo** (por cantidad o porcentaje) para absorber el desfase natural entre cuándo se corta la asignación y cuándo efectivamente se completan las últimas respuestas en curso.

### 6. Ver y exportar resultados

1. Ve a **Marketing outbound → Control de calidad**, elige la tarea de campaña y la encuesta asociada, y busca.
2. Solo se contabilizan clientes en estado "enviado con éxito" o "enviado con error".
3. Para exportar, elige el formato, agrega la tarea de exportación con su horario de ejecución, y descárgala luego desde **Administración avanzada del call center → Gestión de archivos exportados**.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear/editar encuesta | Encuestas → Gestión de encuestas |
| Ver resultados de una campaña | Marketing outbound → Control de calidad |
| Descargar exportación | Administración avanzada del call center → Gestión de archivos exportados |
| Marcador de relleno de texto | `[FILL]` |

---

*Fuente: `raw/zh/模块使用说明/问卷/问卷管理.txt`.*
