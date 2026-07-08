---
title: "Recorrido por la interfaz"
resumen: "Los tres paneles principales de la interfaz de administración y los elementos clave de la interfaz del agente."
seccion: "3.3 Recorrido por la interfaz"
tipo: tutorial
nivel: basico
roles: [administrador, agente]
fuente: zh
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

## Referencia rápida

| Panel | Se abre desde |
|---|---|
| Grupo de agentes | Botón "Mi grupo de agentes" |
| Marcación | Botón de marcación |
| Cola | Botón de cola |
| Mapa | Botón de Google Maps |
| Correo / SMS | Botón de mensajería |

---

*Fuentes: `raw/zh/界面简介/管理界面.txt`, `raw/zh/界面简介/坐席界面.txt`, `raw/zh/界面简介/队列面板.txt`, `raw/zh/界面简介/拨号面板.txt`.*
