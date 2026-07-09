---
title: "Recorrido por la interfaz"
resumen: "Los tres paneles principales de la interfaz de administración y los elementos clave de la interfaz del agente."
seccion: "3.3 Recorrido por la interfaz"
tipo: tutorial
nivel: basico
roles: [administrador, agente]
fuente: zh+en
obsoleto: false
relacionados: [guia-administradores, guia-agentes, plataforma-del-agente]
---

# Recorrido por la interfaz

## Qué es

AsterCC tiene dos interfaces principales: la **interfaz de administración** (para configurar el sistema) y la **interfaz de agente** o [plataforma de trabajo del agente](../modulos/plataforma-del-agente.md) (para operar el día a día). Ambas comparten un diseño consistente basado en navegador.

## Cómo se usa

### Interfaz de administración

Al iniciar sesión con una cuenta de administrador, la pantalla se divide en tres zonas:

- **Zona superior:** área reservada, con el logo del sistema en la esquina superior izquierda.
- **Zona izquierda:** menú de funciones — varía según los permisos del usuario que inició sesión.
- **Zona derecha:** área principal de trabajo, donde se muestran listados y formularios.

Acciones comunes disponibles en la mayoría de las pantallas de listado:
- **Buscar:** expande o contrae el panel de búsqueda.
- **Restablecer:** limpia los criterios de búsqueda ingresados.
- **Exportar:** descarga los resultados filtrados en CSV o Excel.
- **Eliminar:** borra el o los elementos seleccionados.

### Interfaz del agente

Al iniciar sesión como agente se muestra la plataforma de trabajo, con estos elementos principales:

| Elemento | Función |
|---|---|
| Barra de menú | Navegación de funciones del agente |
| Información de sesión actual | Usuario conectado |
| Nombre del equipo | Equipo/organización al que pertenece la cuenta |
| Estado de la extensión VoIP | Velocidad de registro del dispositivo al servidor (si usa un dispositivo VoIP) |
| Mi grupo de agentes | Abre el [panel de grupo de agentes](#panel-de-grupo-de-agentes) |
| Iniciar sesión en cola | Conecta al agente a sus colas |
| Pausar servicio | Marca al agente como no disponible temporalmente |
| Finalizar gestión posterior | Termina manualmente el estado de gestión posterior a una llamada |
| Marcación | Abre el panel de marcación |
| Estado de llamada | Muestra la llamada activa |
| Consulta / recuperar / conferencia / transferir | Controles de la llamada activa |
| Panel de recordatorios | Avisos y tareas pendientes |
| Google Maps | Abre el panel de mapa |
| Correo / SMS | Abre el panel de mensajería |

### Panel de grupo de agentes

Se abre desde "Mi grupo de agentes". Por cada grupo al que pertenece el agente aparece una columna con:

- Iniciar/cerrar sesión en todos los grupos a la vez.
- Pausar/reanudar todos los grupos a la vez.
- Iniciar/cerrar sesión y pausar/reanudar ese grupo específicamente.
- El modo de gestión posterior aplicable a ese grupo (al timbrar, al contestar, o deshabilitado).

### Panel de marcación

Se abre con el botón de marcación. Permite:

- Elegir la cola de salida para la llamada.
- Ingresar el número a marcar.
- Elegir el plan de marcación o cliente virtual asociado (si aplica).
- Iniciar la llamada saliente.
- Consultar el historial reciente de llamadas entrantes y salientes.

### Panel de cola

Se abre con el botón de cola y muestra las colas a las que pertenece el agente, con controles para iniciar/cerrar sesión y pausar/reanudar cada una individualmente o todas a la vez, y el estado actual (libre, ocupado al timbrar, ocupado al contestar).

### Monitoreo y supervisión

AsterCC ofrece monitoreo en dos niveles: el administrador (o cualquier cuenta con permiso) ve el sistema completo; el **administrador del grupo de agentes** ("jefe de equipo") ve y actúa solo sobre su propio grupo.

**Vista de administrador — información en tiempo real:**

| Pantalla | Qué muestra |
|---|---|
| Monitoreo de grupos de agentes | Los agentes conectados y su estado: libre, timbrando, en llamada, en gestión posterior, o en llamada adicional (conferencia/consulta). Un administrador ve todos los grupos; un jefe de equipo solo el suyo. |
| Agentes conectados actualmente | Detalle de las sesiones activas — el sistema permite iniciar sesión desde varios navegadores a la vez. |
| Usuarios conectados actualmente | Lo mismo, para cuentas de usuario (no agentes). |
| Información de uso del sistema | Uso agregado del sistema completo y por equipo. |

En el panel de grupo de agentes de la plataforma del agente, los colores indican el estado: **amarillo** = libre, **azul claro** = timbrando, **rojo** = en llamada.

**Vista de jefe de equipo — control sobre su grupo:**

Al hacer clic sobre un agente de su grupo, el jefe de equipo puede ejecutar (según el estado de la llamada del agente):

- **Colgar:** termina todas las llamadas del agente.
- [Monitoreo, intervención, interrupción forzada y susurro](../glosario.md#monitoreo-intervencion-interrupcion-forzada-y-susurro): las cuatro acciones estándar sobre una llamada en curso.
- **Forzar ocupado:** pone al agente en pausa de inmediato, sin que pueda recibir llamadas.
- **Forzar libre:** saca al agente de pausa para que vuelva a recibir llamadas.
- **Forzar cierre de sesión:** saca al agente de la cola (no disponible si el agente está fijo en ese grupo).

Estas acciones requieren un número de extensión desde el cual se ejecutan — por defecto, la extensión del propio jefe de equipo.

El jefe de equipo también puede administrar la predevolución de su grupo (activarla, ajustar sus parámetros, ver y reciclar clientes) y acceder a la pantalla de **control de calidad** para revisar las llamadas pendientes de calificar.

### Reportes más usados

Sin necesidad de entrar al módulo avanzado de reportes, estos son los más consultados en el día a día:

| Reporte | Para qué sirve |
|---|---|
| Servicio de agentes | Parámetros de un agente en un rango de fechas — por todas sus tareas de marcación saliente, o solo una. |
| Detalle de IVR | Cada llamada que entró a un IVR: número que llama, DID, tiempo dentro del IVR, y a dónde salió. |
| Detalle de llamadas entrantes / salientes | Detalle y volumen de llamadas por agente o por extensión. |
| Servicio de grupo de agentes | Estadísticas de un grupo de agentes en un rango de fechas (solo datos de telefonía — el detalle de negocio está en el reporte del módulo correspondiente). |
| Resumen de llamadas salientes | Totales de llamadas salientes por extensión, agente o cuenta. |
| Resumen diario | Picos diarios de sesiones iniciadas, check-ins, llamadas y pausas — útil para planear turnos. |
| Estadísticas de importación de datos | Seguimiento de las tareas de importación masiva. |
| Estadísticas de DID | Volumen de llamadas entrantes por número DID. |
| Estadísticas de marcación saliente | Resultados y tasa de éxito por tarea de marcación saliente. |
| Estadísticas de predevolución | Datos de las tareas que usan predevolución — sirven de referencia para ajustar sus parámetros. |
| Registro de filtro de predevolución | Ejecución de los filtros que reciclan clientes automáticamente a la lista de predevolución. |
| Monitor de volumen de datos | Volumen de datos (importados, marcados, exitosos, pendientes) de una tarea de marcación saliente. |

## Referencia rápida

| Panel | Se abre desde |
|---|---|
| Grupo de agentes | Botón "Mi grupo de agentes" |
| Marcación | Botón de marcación |
| Cola | Botón de cola |
| Mapa | Botón de Google Maps |
| Correo / SMS | Botón de mensajería |
| Monitoreo de grupos de agentes | Panel de información en tiempo real (administrador) o plataforma del jefe de equipo |

---

## Fuentes

- `raw/zh/界面简介/管理界面.txt`
- `raw/zh/界面简介/坐席界面.txt`
- `raw/zh/界面简介/队列面板.txt`
- `raw/zh/界面简介/拨号面板.txt`
- `raw/zh/呼叫中心常用功能简介/坐席监控系统介绍.txt`
- `raw/zh/呼叫中心常用功能简介/实时监控.txt`
- `raw/zh/呼叫中心常用功能简介/班长功能.txt`
- `raw/zh/呼叫中心常用功能简介/常用报表.txt`
- `raw/en/newbie/quick_start.txt`