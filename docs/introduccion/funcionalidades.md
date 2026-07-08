---
title: "Funcionalidades del sistema"
resumen: "Lista de las funcionalidades principales que ofrece AsterCC, organizadas por capa."
seccion: "1.2 Funcionalidades del sistema"
tipo: referencia
nivel: basico
roles: [administrador, agente]
fuente: zh+en
obsoleto: false
relacionados: [arquitectura-general, que-es-astercc]
---

# Funcionalidades del sistema

Esta página resume las funciones disponibles en AsterCC, organizadas según las tres capas descritas en [Arquitectura general](arquitectura-general.md). El detalle de configuración de cada una vive en su artículo correspondiente dentro de [Módulos del sistema](../modulos/index.md).

## Funciones de PBX (telefonía)

- **Multiempresa:** un mismo sistema puede dar servicio a varias organizaciones sin que se afecten entre sí (típico de un call center gestionado/hosted).
- **Roles y permisos:** roles habituales — administrador, operaciones, calidad, jefe de equipo, agente — cada uno con permisos configurables (agregar, editar, ver, eliminar, exportar) y alcance (toda la organización, un grupo de agentes, o solo el propio usuario).
- **Configuración por lotes** de extensiones y troncales mediante plantillas.
- **Troncales:** SIP, IAX2, tarjetas E1/T1 y analógicas.
- **Extensiones de red y extensiones externas** (un número externo configurado como si fuera una extensión, solo puede recibir llamadas del sistema).
- **Grupos de cuentas** (asociados a distintos grupos de troncales — ej. ventas puede marcar cualquier destino, RR.HH. solo local).
- **Grupos de troncales**, con selección secuencial, rotativa o aleatoria, y baja automática de un troncal tras fallos consecutivos (con alerta al administrador).
- **Rutas entrantes y salientes**, con enrutamiento por DID, por troncal, por número que llama, o por ubicación geográfica del número que llama.
- **Grupos de timbrado**, ruteo por horario, registro y grabación de llamadas (WAV o MP3).
- **Buzón de voz**, transferencia de llamadas, retención de llamada, listas blanca/negra.
- **Restricción de número saliente** por agente, para prevenir llamadas no autorizadas.
- **Conferencias telefónicas.**
- **IVR:** soporta integración por webservice (TTS y ASR), múltiples acciones por nodo, operaciones numéricas y de texto, envío de DTMF, datos de acompañamiento (user-to-user), y transferencia por SIP REFER.
- **BLF** (indicador de estado de línea).
- **Facturación en tres niveles:** sistema, equipo y usuario — con facturación automática en los tres niveles.
- **Fax electrónico, música en espera, soporte multi-idioma.**
- **Teclas rápidas** para agentes que solo usan teléfono (sin la plataforma web): transferencia, consulta, retención, captura de llamada, grabación, check-in/check-out, activar/desactivar no-molestar, cambio de modo de llamada, buzón de voz, y más.
- **Instalación y actualización de módulos** desde la interfaz de administración, sin acceso a servidor en la mayoría de los casos.

## Funciones de call center (CTI)

- **Monitoreo en tiempo real:** estado de cada grupo de agentes (conectado, libre, timbrando, en llamada, en pausa, en gestión posterior) y clientes en espera. Desde esta vista el supervisor puede forzar check-out, forzar disponible/ocupado, y —durante una llamada activa— aplicar [intervención, monitoreo, interrupción forzada o susurro](../glosario.md#monitoreo-intervencion-interrupcion-forzada-y-susurro).
- **Agentes y troncales en línea en tiempo real.**
- **Marcación con un clic** para llamada, SMS o correo.
- **Calificación de agentes** y panel de llamadas (muestra la llamada activa y las que el agente tiene en gestión).
- **Retención, consulta y transferencia de llamadas; conferencia multipartita** (hasta 12 participantes desde la plataforma).
- **Pausa de agente**, para mejorar la estadística de su actividad.
- **Modos de agente:**
  - **Estático:** debe iniciar sesión manualmente en la cola.
  - **Dinámico:** inicia sesión automáticamente y permanece.
  - **En línea:** debe iniciar sesión vía navegador; se cierra sesión automáticamente al cerrar la plataforma. Útil cuando el agente necesita consultar/editar datos del cliente en pantalla.
  - **Fuera de línea:** inicia sesión por teléfono; no se cierra sesión al cerrar la plataforma.
  - **Externo:** puede recibir llamadas del sistema en cualquier número telefónico normal.
  - Un agente puede pertenecer a varios grupos, cada uno con su propio modo.
- **Modos de llamada:** entrante+saliente, solo entrante, solo saliente.
- **Modos de gestión posterior a la llamada (ACW):** por timbrado, por respuesta, o deshabilitado — configurable por grupo de agentes.
- **Recordatorios de agenda del agente, respaldo automático de datos, limpieza automática de grabaciones.**
- **Plantillas de SMS y correo, envío masivo de ambos.**
- **Reglas personalizadas de formato de número, gestión de ubicación geográfica por número, gestión de motivos de pausa.**
- **Mensajería interna, reportes del sistema.**
- **Cola (ACD):** múltiples estrategias de distribución, indicador de posición en espera, prioridad para clientes VIP.
- **Callback:** el sistema recolecta solicitudes de devolución de llamada por distintos canales y las asigna a un agente.
- **Soporte de mapas** vía integración con Google Maps.
- **Datos de acompañamiento:** al recibir una llamada, la plataforma del agente muestra número que llama, número llamado, nombre de la cola, etc.
- **API de grabación** para que sistemas de terceros obtengan la ubicación de una grabación mediante el identificador de la llamada.

## Funciones de negocio (tipo CRM)

- **Campañas de marketing saliente:**
  - Número que llama configurable por tarea o por agente.
  - Paquete de clientes por tarea, o uso de la tabla general.
  - Asignación de datos al agente: manual (el agente la solicita) o por el administrador.
  - Campos visibles para el agente vs. campos visibles solo para el equipo de operaciones (estos últimos se usan también al exportar).
  - **Modos de marcación:**
    - **Predictivo:** el sistema marca primero y transfiere la llamada contestada a un IVR o cola.
    - **Preview:** el agente revisa la ficha del cliente y marca manualmente.
    - **Automático:** el agente inicia su turno de trabajo y el sistema muestra la ficha y marca automáticamente, avanzando al siguiente número al terminar cada llamada.
  - Resultado de llamada configurable (global o por tarea); resultado especial "no llamar" (DNC) que bloquea automáticamente el número.
  - Horario de trabajo, enlace de pantalla emergente personalizado, números bloqueados, ranking de éxito por agente, ocultamiento de datos de contacto, monitoreo de volumen de datos.
- **Correo y SMS automáticos al finalizar llamada.**
- **Asignación automática o manual de datos**, importación de datos (por archivo o API), diccionario de datos.
- **Reciclaje y detección de duplicados de datos.**
- **Control de calidad de llamadas salientes.**
- **Campos personalizados y enlaces de pantalla emergente personalizados.**
- **Ubicación geográfica del número que llama, recordatorios de tareas de devolución de llamada.**
- **Reportes automáticos, gestión de llamadas perdidas.**
- **Base de conocimiento, gestión de tareas.**
- **Encuestas:** por agente o por voz, con plantillas, cuotas, estadísticas de distribución y exportación de resultados (SPSS o CSV).
- **Work orders (órdenes de trabajo), gestión de productos y pedidos, múltiples tareas de e-commerce.**
- **Etiquetas de cliente, clientes institucionales e individuales, tabla principal y subtablas de clientes.**
- **Agenda de agente y agenda de cliente.**

## Referencia rápida

| Capa | Ver también |
|---|---|
| PBX | [4.1 PBX y telefonía](../modulos/pbx-y-telefonia.md) |
| Call center (CTI) | [4.7 Plataforma de trabajo del agente](../modulos/plataforma-del-agente.md), [4.3 Cuentas, equipos y permisos](../modulos/cuentas-equipos-permisos.md) |
| Negocio (CRM) | [4.2 Marcador y campañas](../modulos/marcador-y-campanas.md), [4.5 Encuestas](../modulos/encuestas.md), [4.10 Atención al cliente, mensajería y e-commerce](../modulos/atencion-cliente-mensajeria-ecommerce.md) |

---

## Fuentes

- `raw/zh/呼叫中心系统功能列表.txt`
- `raw/en/astercc_call_center_quick_feature_list.txt`