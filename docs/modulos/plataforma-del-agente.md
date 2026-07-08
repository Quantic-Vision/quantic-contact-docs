---
title: "Plataforma de trabajo del agente"
resumen: "Referencia completa de los controles de la plataforma del agente: check-in, pausa, marcación, llamada activa y páginas de negocio embebidas."
seccion: "4.7 Plataforma de trabajo del agente"
tipo: referencia
nivel: basico
roles: [agente]
fuente: zh
obsoleto: false
relacionados: [guia-agentes, recorrido-interfaz, marcador-y-campanas]
---

# Plataforma de trabajo del agente

## Qué es

Esta es la referencia completa de la plataforma web que usa el agente para trabajar. Para una guía paso a paso de inicio, ver [Guía rápida para agentes](../primeros-pasos/guia-agentes.md); esta página cubre cada control en detalle.

## Cómo se usa

### Inicio de sesión

- Navegadores soportados: Firefox 3.0+ (recomendado), Internet Explorer 8.0+, Chrome.
- Se elige idioma, se ingresan usuario y contraseña, y el equipo al que pertenece la cuenta.

![Pantalla de inicio de sesión de la plataforma del agente](../assets/images/plataforma-agente/login.png)

### Layout general

La pantalla se divide en: lista de páginas disponibles, botones de función, área de contenido (donde se cargan las páginas de negocio embebidas), y barra de pestañas de páginas abiertas en la parte inferior. Todos los agentes tienen un menú de **gestión básica** (datos personales, historial de llamadas propio, buzón de voz, mensajes internos y anuncios); los jefes de grupo tienen además menús de **jefe de grupo** y de **marcador predictivo**. El resto de los menús depende del rol asignado a la cuenta.

![Layout general de la plataforma del agente](../assets/images/plataforma-agente/layout-general.png)

### Check-in / check-out y posibles avisos

![Botón para iniciar sesión en el grupo de agentes](../assets/images/plataforma-agente/boton-grupo-agentes.png)
![Panel de grupos disponibles para conectarse](../assets/images/plataforma-agente/panel-grupos-disponibles.png)

Al conectarte a tus colas pueden aparecer distintos avisos según el estado de tu extensión:

| Situación | Qué significa | Qué hacer |
|---|---|---|
| El sistema corrige tu extensión automáticamente | Tu extensión configurada no está registrada desde tu IP, pero otra sí | Nada — el sistema ya ajustó la extensión por ti |
| "Extensión en uso por otro agente" | Otro agente ya está usando esa extensión | Cambia de extensión o coordina con esa persona |
| IP de login no coincide con la IP registrada del teléfono | Tu extensión es de tipo autoadaptable/autoseleccionable y no hay registro desde tu IP | Continúa el check-in o corrige la extensión — si usas un teléfono IP fijo, pide que tu extensión se configure como "fija" |
| Conexión telefónica anómala | El sistema no detecta tu dispositivo | Verifica tu teléfono; si confirmas que sí está conectado, puedes ignorar el aviso y avisar al administrador |

### Modo de trabajo y modo de gestión posterior

Se configuran por grupo de agentes (pueden venir fijados por el administrador, en cuyo caso aparecen deshabilitados para el agente):

- **Modo de trabajo:** solo entrantes, solo salientes, o ambos.
- **Modo de gestión posterior (ACW):** al timbrar, al contestar, o deshabilitado.

### Pausa y bloqueo de pantalla

Al pausar, dejas de recibir llamadas entrantes (pero puedes seguir marcando si tienes permiso). Toda pausa requiere seleccionar un **motivo** — igual que el bloqueo de pantalla, que además pide tu contraseña para desbloquear.

![Diálogo para seleccionar el motivo de pausa](../assets/images/plataforma-agente/dialogo-pausa.png)

### Panel de marcación

![Panel de marcación](../assets/images/plataforma-agente/panel-marcacion.png)

Al abrir el panel de marcación se listan tus grupos conectados; eligiendo uno se muestran su historial reciente de llamadas y sus destinos disponibles, distinguidos por prefijo:

| Prefijo | Tipo de destino |
|---|---|
| `>>` | Cliente virtual |
| `<<` | Tarea de campaña saliente |
| `<>` | Aplicación / programa |

Si el grupo tiene restricción de marcación saliente, el campo de número se deshabilita y debes elegir un número desde el historial de llamadas.

### Estado de la llamada

El panel de estado usa un código de color por cada número involucrado en la llamada:

| Color | Significado |
|---|---|
| Rojo | Timbrando |
| Verde | En conversación con el agente |
| Amarillo | Dentro de una sala de conferencia |
| Gris (parpadeo breve) | Colgó y sale de la llamada |

![Panel de estado de la llamada](../assets/images/plataforma-agente/estado-llamada.png)

### Controles durante una llamada activa

| Control | Disponible cuando | Qué hace |
|---|---|---|
| Retener / Continuar | Llamada en curso | Pone al cliente en espera con música; retoma la conversación al continuar |
| [Consulta](../glosario.md#consulta-transferencia-recuperar-y-conferencia) | En llamada, sin consulta activa | Llama a otro agente o a un número externo mientras el cliente espera |
| Recuperar | Con consulta timbrando o activa | Cuelga al tercero y retoma con el cliente |
| Conferencia | 3 o más participantes en línea | Une a todos en una sala |
| Transferencia | En consulta con cliente + tercero | Deja al cliente hablando con el tercero y libera al agente |

![Consultar a otro agente](../assets/images/plataforma-agente/consulta-agente.png)
![Consultar un número externo](../assets/images/plataforma-agente/consulta-numero.png)

### Recordatorios, mapa y mensajería

- **Recordatorios:** siempre visible; muestra anuncios, mensajes, tareas y agenda — las últimas 5 entradas de cada categoría.

  ![Panel de recordatorios](../assets/images/plataforma-agente/panel-recordatorios.png)

- **Mapa:** integración con Google Maps para ubicar direcciones y calcular rutas (requiere una clave de API de Google Maps configurada en Sistema → Configuración del sistema).

  ![Panel de mapa](../assets/images/plataforma-agente/panel-mapa.png)

- **Mensajería:** envío de SMS o correo a un destino desde la misma plataforma.

  ![Envío de SMS desde la plataforma](../assets/images/plataforma-agente/enviar-sms.png)

### Menú de mantenimiento

- **Actualizar telefonía:** sincroniza el estado del teléfono/llamada si la pantalla queda desincronizada del estado real.
- **Procesar datos de llamada con error:** limpia registros de llamada "atascados" (llamadas activas o recién colgadas hace más de 1 minuto con datos inconsistentes) — requiere permiso o autorización de un jefe de grupo.
- **Procesar errores de marcación:** igual que el anterior, pero para números que quedaron atascados en la lista de marcación sin haberse llegado a marcar.

### Páginas de negocio embebidas

El área central de la plataforma muestra la página de negocio configurada para el grupo o la tarea activa. Las tres páginas por defecto del sistema:

1. **Página de trabajo del grupo de agentes:** calendario/agenda, información del agente, y miembros del grupo.

   ![Página de trabajo del grupo de agentes](../assets/images/plataforma-agente/pagina-trabajo-grupo.png)

2. **Página de campaña de marketing saliente:** lista de tareas a la izquierda, detalle de clientes a la derecha (clasificados en pendientes, en seguimiento, enviado con error, enviado con éxito), y el área de encuesta abajo si la tarea tiene una asociada. Aquí también se ve si el modo de marcación es manual, preview o automático — y si el modo automático está activo, un contador de llamadas realizadas y el tiempo transcurrido en la sesión de marcado.

   ![Página de trabajo de una campaña de marketing saliente](../assets/images/plataforma-agente/pagina-campana.png)

3. **Página de oficina virtual / BPO:** al recibir una llamada enrutada desde un cliente virtual, se muestra la información de esa empresa (datos, saludo, contactos frecuentes) y su base de conocimiento específica para que el agente pueda resolver la consulta sin conocer el negocio del cliente virtual de antemano.

   ![Página de oficina virtual con datos del cliente virtual](../assets/images/plataforma-agente/pagina-oficina-virtual.png)

## Referencia rápida

| Necesito | Control |
|---|---|
| Conectarme a mis colas | Botón de check-in |
| Dejar de recibir llamadas temporalmente | Pausa (con motivo) |
| Ver mis llamadas o descargar una grabación | Historial de llamadas |
| Consultar antes de transferir | Consulta → Recuperar / Transferir / Conferencia |
| Ver mensajes y tareas pendientes | Recordatorios |

---

## Fuentes

- `raw/zh/模块使用说明/坐席平台/坐席平台基本介绍.txt`