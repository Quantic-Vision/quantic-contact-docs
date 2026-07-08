---
title: "Base de conocimiento y Work Orders"
resumen: "Cómo organizar artículos de conocimiento para los agentes y cómo modelar un flujo de work order entre equipos."
seccion: "4.6 Base de conocimiento y Work Orders"
tipo: guia
nivel: intermedio
roles: [administrador, agente]
fuente: zh
obsoleto: false
relacionados: [cuentas-equipos-permisos, atencion-cliente-mensajeria-ecommerce]
---

# Base de conocimiento y Work Orders

## Qué es

Dos módulos distintos que suelen usarse juntos: la **base de conocimiento** centraliza el know-how operativo para que los agentes no dependan de la memoria de "expertos" individuales, y los **work orders (órdenes de trabajo)** modelan un flujo de trabajo que pasa de un equipo a otro hasta resolverse — por ejemplo, un pedido que pasa de ventas a finanzas, a almacén, a logística, y de vuelta al agente que originó el caso.

## Cómo se usa

### Base de conocimiento

1. Ve a **Base de conocimiento → Base de conocimiento** y selecciona el equipo.
2. Crea **categorías de conocimiento** (y subcategorías, arrastrando para anidar u ordenar).
3. Dentro de una categoría, agrega un artículo de conocimiento con:

| Campo | Qué define |
|---|---|
| Nombre | Identifica brevemente el artículo |
| Etiquetas | Para búsqueda rápida por tema |
| Estado | **Borrador** (solo lo ve su creador) o **Publicado** (visible para quien tenga permiso de ver la base) |
| Archivo adjunto | Material de soporte descargable |
| Contenido con formato / contenido en texto plano | El texto en formato enriquecido se muestra al leer el artículo; el texto plano es lo que se indexa para búsqueda |

4. Los agentes pueden **buscar por texto libre** o hacer clic en una etiqueta para filtrar artículos relacionados.
5. El **permiso por rol** controla, para cada cuenta, si puede: agregar categorías, agregar artículos, editar, ver, eliminar, y **publicar** (un artículo enviado por alguien sin permiso de publicar queda pendiente de revisión hasta que alguien con ese permiso lo apruebe).

### Work Orders

Antes de usar el módulo, hay que definir una **plantilla de work order** — el flujo que seguirá ese tipo de caso.

1. Ve a **Gestión de work orders → Work order → Agregar** y define:

| Campo | Qué define |
|---|---|
| Equipo | A qué equipo pertenece esta plantilla |
| Alcance de flujo | Entre qué grupos de agentes puede moverse el work order (si no se usa flujo automático) |
| Flujo inicial directo | Si el primer grupo del flujo es el mismo que crea el work order, si se asigna directo a ese grupo o espera asignación manual |
| Permiso de edición | Quién puede modificar contenido, responder, o cambiar el estado — "todos" o "solo el dueño y el jefe de grupo" |
| Retener agente en el flujo | Si al pasar de un grupo a otro, se prioriza asignar al mismo agente que lo creó o que lo tuvo antes, antes de dejarlo en la bandeja general del siguiente grupo |
| Acción de cierre | Qué pasa al cerrar el último nodo: nada, crear automáticamente un work order de seguimiento, o dejar que el agente decida |
| Copia de correo por defecto | Direcciones que se notifican en cada cambio del work order |

2. Define **campos personalizados** para capturar información específica del proceso (texto corto, selección, texto largo, archivo, fecha, fecha y hora).
3. Si el proceso siempre sigue el mismo camino, configura el **flujo automático**: al guardar la secuencia de grupos, el work order avanza solo de un grupo al siguiente al completarse cada paso, y se cierra automáticamente al terminar el último.

### Dónde se crea un work order

Un work order se puede originar desde cuatro lugares:
1. Pantalla emergente de atención al cliente entrante, si el resultado de la llamada está vinculado a esta plantilla.
2. Gestión de llamadas perdidas, para dar seguimiento a una llamada no atendida.
3. Pantalla emergente de una campaña de marketing saliente, si el resultado de la llamada está vinculado a esta plantilla.
4. La pantalla **"Mis work orders"**, donde un jefe de grupo puede crear uno manualmente para su equipo.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear categoría/artículo de conocimiento | Base de conocimiento → Base de conocimiento |
| Controlar permisos de la base de conocimiento | Cuentas y permisos → Gestión de roles → Base de conocimiento |
| Crear plantilla de work order | Gestión de work orders → Work order |
| Vincular resultado de llamada a un work order | Configuración de resultados de llamada (atención al cliente / campaña) |

---

## Fuentes

- `raw/zh/模块使用说明/知识库/知识库.txt`
- `raw/zh/模块使用说明/工单管理/工单.txt`