---
title: "Glosario"
resumen: "Términos técnicos usados en la documentación de AsterCC, con su traducción estándar al español."
seccion: "Glosario"
tipo: referencia
nivel: basico
roles: [administrador, agente, desarrollador]
fuente: zh+en
obsoleto: false
relacionados: []
---

# Glosario

Este glosario define la terminología técnica de AsterCC y fija la traducción estándar que se usa en **todo** el resto del wiki. Si un término no aparece aquí y se necesita durante la redacción, se agrega primero a esta página antes de usarlo en cualquier otro artículo.

## Asterisk

Software libre que implementa una central telefónica (PBX) completa. Corre sobre Linux y provee todas las funciones esperables de una PBX —y más—, incluyendo buzón de voz, conferencias, IVR y gestión de colas. Soporta múltiples protocolos de voz sobre IP (SIP, IAX, H.323, entre otros) y puede interoperar con equipos de telefonía estándar. AsterCC es una plataforma de call center construida sobre Asterisk.

## Agente

Persona que atiende llamadas, correos, SMS o fax dentro del call center. En un call center tradicional, el agente solo atendía o realizaba llamadas; en AsterCC, un agente también puede gestionar correo, SMS y fax desde la misma plataforma. Puede usar un teléfono físico (conectado a la PBX), una línea fija, un móvil, o un softphone/teléfono IP. Cada agente se identifica por un **número de agente**.

## Sistema del agente (plataforma de trabajo)

La aplicación de escritorio o web que usa el agente para trabajar. Cuando ocurre un evento en su teléfono (timbre, llamada conectada, colgado), el sistema reacciona automáticamente (aviso visual, apertura de ficha de cliente). El agente también puede controlar su teléfono desde este sistema: originar llamadas, hacer consultas, conferencias a tres, rechazar o colgar. Normalmente se integra con el sistema de negocio (tipo CRM). En AsterCC, esta interfaz se llama **plataforma de trabajo del agente**.

## Cola / Grupo de agentes

Una **cola** es un conjunto de agentes que procesan llamadas según una estrategia de distribución. En un call center de llamadas entrantes, cuando una llamada ingresa se transfiere a una cola y esta la asigna a uno de los agentes registrados según la estrategia configurada.

Dos funciones asociadas a la cola:
- **Anuncio de número de agente:** antes de iniciar la conversación, el sistema anuncia por IVR el número del agente que va a atender.
- **Calificación del agente:** al finalizar la llamada, si el agente cuelga primero, el cliente es transferido a un IVR que le permite calificar el servicio mediante el teclado.

## ACD (Distribuidor Automático de Llamadas)

Sistema que distribuye automáticamente las llamadas entrantes a un grupo específico de agentes, según una estrategia de enrutamiento (ronda rotativa, menor tiempo en llamada, incremental, aleatoria, timbrado a todos). Se usa en organizaciones que reciben un alto volumen de llamadas donde el cliente no necesita hablar con una persona específica, sino con alguien capacitado para atenderlo.

## Iniciar / cerrar sesión en cola (check in / check out)

**Iniciar sesión en cola:** el agente se une a una cola, indicando que está listo para recibir llamadas de esa cola.
**Cerrar sesión en cola:** acción opuesta — el agente deja de recibir llamadas de esa cola.

Un agente puede pertenecer a varias colas y elegir en cuáles iniciar o cerrar sesión según lo necesite. El administrador también puede fijar a un agente permanentemente en una cola.

## Marcar como ocupado / Marcar como disponible

**Marcar como ocupado:** el agente indica temporalmente que no puede recibir más llamadas de la cola (por ejemplo, mientras termina de documentar una llamada anterior). Mientras está en este estado, la cola lo omite al asignar llamadas.
**Marcar como disponible:** acción opuesta — el agente vuelve a estar disponible para recibir llamadas.

AsterCC puede marcar automáticamente a un agente como ocupado al finalizar una llamada, dándole tiempo para completar su gestión antes de volver a marcarse como disponible.

En la mayoría de las pantallas de la plataforma del agente, esta acción se etiqueta simplemente como **Pausa** ("forzar ocupado" / "forzar libre" desde la vista de supervisor) — es el mismo concepto descrito aquí, no una función distinta. No confundir tampoco con [ACW](#acw-gestion-posterior-a-la-llamada): la pausa es una decisión manual del agente o del supervisor en cualquier momento, mientras que el ACW es un estado automático y de duración acotada que ocurre solo justo después de colgar.

## Consulta, transferencia, recuperar y conferencia

Durante una llamada activa con un cliente, el agente puede iniciar una **consulta**: una llamada hacia un tercero mientras el cliente queda en espera (normalmente escuchando música de espera). Durante esa consulta, el agente puede elegir entre tres acciones:

- **Recuperar llamada:** se cuelga la llamada con el tercero y el agente retoma la conversación con el cliente.
- **Transferencia:** el cliente queda hablando con el tercero, y el agente sale de la llamada.
- **Conferencia:** se une al cliente a la llamada, formando una conferencia de tres partes.

## Llamada multipartita

Conferencia con más de tres participantes. Se construye a partir de una llamada de conferencia (ver arriba), donde el agente sigue usando consulta y conferencia para ir sumando más participantes a la sala.

## Grabación

AsterCC soporta dos modos de grabación de llamadas:
- **Grabación por demanda:** el agente decide cuándo iniciar o detener la grabación durante la llamada.
- **Grabación obligatoria:** el sistema graba todas las llamadas sin excepción.

Además del criterio por extensión/dispositivo, la grabación puede **forzarse** a nivel de **cuenta** o de **equipo** — un nivel más general (equipo) sobrescribe el criterio individual de cada extensión que dependa de él. Las llamadas de agente, por su parte, se graban automáticamente sin necesidad de configurar nada extra. Ver [PBX y telefonía — cuatro lugares donde se controla la grabación](modulos/pbx-y-telefonia.md#extensiones-gestion-de-dispositivos).

## Marcación con un clic (click-to-dial)

Función que permite al agente iniciar una llamada haciendo clic sobre un número dentro del sistema de negocio, o ingresándolo manualmente, sin necesidad de marcar desde un teléfono físico.

## Monitoreo, intervención, interrupción forzada y susurro

Funciones disponibles para agentes con permisos elevados (normalmente supervisores), aplicables sobre una llamada en curso:

- **Monitoreo (escucha silenciosa):** escuchar la llamada sin que ninguna de las dos partes lo note.
- **Intervención:** unirse activamente a una llamada en curso.
- **Interrupción forzada:** finalizar la llamada del agente; el cliente queda hablando con quien ejecutó la acción.
- **Susurro:** hablar con el agente en plena llamada sin que el cliente pueda escucharlo (comunicación unidireccional).

## Paquete de clientes (para marcación saliente)

Conjunto de clientes extraído de la base de datos, usado como insumo para una campaña de marcación saliente. El paquete se genera antes de iniciar la campaña y agrupa a los clientes que cumplen ciertos criterios; una vez creado, no cambia automáticamente si la base de datos original se actualiza. Un paquete puede asociarse a un plan de marcación.

## Plan de marcación

Configuración que define una tarea de marcación saliente. Cada plan de marcación se asocia típicamente a un grupo de agentes y a un paquete de clientes, y opcionalmente puede incluir una encuesta a completar durante o después de la llamada.

## IVR (respuesta de voz interactiva)

Menú de voz automatizado que permite al cliente navegar opciones mediante el teclado del teléfono (tonos DTMF) antes o durante una llamada — por ejemplo, para elegir un departamento o autenticarse. En AsterCC, un IVR se compone de uno o más **flujos**: cada tecla presionada por el cliente avanza al siguiente flujo. Ver [Configurar IVR](modulos/pbx-ivr.md).

## DTMF

Sistema de tonos que genera un teléfono al presionar sus teclas (dígitos, `*`, `#`), usado para navegar IVR o enviar datos durante una llamada activa. La API de integración de AsterCC permite enviar DTMF de forma programática hacia una llamada en curso.

## Webhook / callback

**Webhook:** mecanismo por el cual AsterCC envía (hace `POST` hacia) una URL configurada por el desarrollador cada vez que ocurre un evento (una llamada, un cambio de estado) — el flujo de datos lo inicia AsterCC hacia el sistema externo.
**Callback (función de retorno):** en las interfaces JavaScript de la API de integración, una función que el desarrollador registra y que AsterCC invoca al completar una operación asíncrona, entregando el resultado (código y mensaje).

No confundir con la **devolución de llamada telefónica** (a veces también llamada "callback"): función de la API donde el sistema marca primero al agente o a un número de origen y, una vez que responde, marca al destino — ver [doble llamada / devolución](desarrollo/api-control-de-llamada.md).

## ACW (gestión posterior a la llamada)

Sigla de *After-Call Work*. Estado en el que entra un agente automáticamente al colgar, con tiempo dedicado a completar la documentación de la llamada (ficha de cliente, work order, resultado) antes de volver a estar disponible para la cola. El sistema puede forzar la salida de ACW tras un tiempo máximo configurado.

## AMI (Asterisk Manager Interface)

Interfaz de administración de Asterisk usada por AsterCC para operar la central telefónica (originar llamadas, consultar canales, recibir eventos) desde fuera del propio Asterisk. Ver [Configurar Asterisk AMI](administracion/asterisk-ami.md).

## CDR (registro de detalle de llamada)

Sigla de *Call Detail Record*. Registro que guarda los datos de cada llamada (origen, destino, duración, resultado, costo, grabación asociada) y que alimenta los reportes, la facturación y el historial de llamadas del cliente.

## DNC (lista de no llamar)

Sigla de *Do Not Call*. Lista de números a los que el marcador saliente tiene prohibido llamar — un número puede llegar a esta lista automáticamente (ej. el cliente lo solicitó) o ser agregado manualmente por un administrador.

## MOH (música en espera)

Sigla de *Music On Hold*. Audio que escucha quien queda en espera durante una consulta, transferencia o mientras aguarda en cola. Se configura como uno o varios archivos de audio agrupados en una clase de MOH, asignable por cola, IVR o troncal.

## Ficha emergente (screen pop)

Ventana o página que se abre automáticamente en la plataforma de trabajo del agente al recibir o hacer una llamada, mostrando la información del cliente o del negocio asociado a esa llamada (también referida como "pantalla emergente" o "pop-up"). Su URL puede personalizarse y recibir parámetros de la llamada.

## TTS (texto a voz)

Sigla de *Text To Speech*. Conversión automática de texto a audio, usada por ejemplo para leer en voz alta un mensaje de IVR sin grabar un archivo de audio manualmente.

## Inspector de calidad

Uno de los cuatro roles por defecto del sistema (junto con administrador de sistema, administrador de grupo de agentes y agente). Tiene acceso a las herramientas de calificación/evaluación de llamadas grabadas, sin los permisos administrativos completos de un administrador de equipo.

## Estados de agente (estático/dinámico, en línea/fuera de línea)

Un agente es **estático** cuando el administrador lo asigna de forma fija a una cola o grupo (no puede iniciar/cerrar sesión por su cuenta en esa cola), y **dinámico** cuando puede unirse o salir de la cola libremente. De forma independiente, un agente está **en línea** cuando su sesión está activa en la plataforma de trabajo, y **fuera de línea** en caso contrario — un agente puede estar asignado (estático) a una cola y a la vez fuera de línea.

## Grupo de timbrado (ring group)

Conjunto de extensiones/teléfonos que timbran juntos ante una misma llamada entrante, según una estrategia (todos a la vez, en secuencia, round robin, etc.), independiente del mecanismo de colas de agentes — se usa típicamente para escenarios simples de oficina (ej. "que timbren los tres teléfonos de recepción").

## Grupo de troncales (trunk group)

Conjunto de troncales agrupados bajo un mismo nombre para que una regla de tarifa o de enrutamiento pueda seleccionar cualquiera de ellos según disponibilidad, en vez de fijar un solo troncal.

## Encuesta posterior a la llamada

Cuestionario (por teclado en IVR, o por formulario en la plataforma del agente) que se ofrece al cliente o se le pide al agente completar justo después de finalizar la llamada, para calificar el servicio o registrar el resultado de la gestión. Es el mismo concepto detrás de términos como "evaluación de llamadas" o "encuesta IVR de evaluación al agente" usados en distintas páginas de este wiki.

## Marcado automático vs. marcador predictivo

**Marcado automático (auto dial):** el sistema disca el siguiente número de la lista tan pronto un agente queda libre, uno a uno, sin anticipar cuántas llamadas van a contestar. **Marcador predictivo:** el sistema disca varios números en simultáneo, anticipando cuántos serán contestados, para minimizar el tiempo que un agente pasa esperando — ver [Marcador predictivo — avanzado](modulos/marcador-predictivo-avanzado.md).

## Número CV (CvNumber)

Identificador técnico que vincula un DID (o número que marca el cliente) con un usuario virtual o campaña específica dentro de [Oficina virtual / BPO](modulos/oficina-virtual-bpo.md), permitiendo que el sistema sepa a qué empresa cliente pertenece cada llamada entrante.

## Marcación estadística (stat dial)

Modo de marcación desde la plataforma del agente que, además de originar la llamada, registra métricas de esa marcación (intentos, resultado) por separado del historial normal de llamadas — útil para medir el desempeño de marcación manual fuera de una tarea de campaña.

## Núcleo del sistema (core)

Componente central de AsterCC que se actualiza como unidad independiente de los módulos — una actualización de "core" (ej. `core-2.0-beta`) puede requerirse antes o junto con la actualización de módulos individuales.

## Atributos de número / ubicación geográfica del número que llama

Información de ubicación (código de área, provincia/ciudad, operador) que el sistema resuelve automáticamente a partir del número que marca un cliente, y que se muestra al agente en la ficha o formulario de alta al recibir una llamada — no requiere que el cliente ya exista en la base de datos.

## "El creador retiene" (work order)

Regla de asignación de un work order donde, aunque el caso se derive o consulte a otro grupo/agente, el creador original conserva la propiedad y el seguimiento del caso — ver [Base de conocimiento y Work Orders](modulos/base-conocimiento-work-orders.md#work-orders).

## BLF (indicador de estado de línea)

Sigla de *Busy Lamp Field*. Luz o ícono en un teléfono IP que muestra en tiempo real si otra extensión está libre, timbrando o en llamada — se configura agrupando extensiones en un **grupo BLF** para que cada teléfono del grupo pueda ver el estado de las demás.

## Extensión adaptativa (modo autoadaptable / autoseleccionable)

Extensión cuyo dispositivo físico no está fijo: el agente puede registrarse desde cualquier teléfono/softphone disponible al iniciar sesión, en vez de tener siempre el mismo aparato asignado — típico en esquemas de puesto compartido entre turnos. Se distingue del modo **fijo**, donde la extensión siempre corresponde al mismo dispositivo.

## SaaS / oficina virtual alojada (hosted)

Modalidad en la que AsterCC (o el servicio de call center construido sobre él) se ofrece como servicio alojado por un proveedor, en vez de instalado en un servidor propio del cliente — el mismo concepto que respalda a [Oficina virtual / BPO](modulos/oficina-virtual-bpo.md), donde una sola instalación atiende a varias empresas cliente.

## Cuenta, agente y extensión (las tres capas de una persona que trabaja)

Tres objetos distintos que suelen confundirse porque casi siempre se crean juntos para la misma persona:

- **Cuenta:** el usuario que inicia sesión en el sistema (usuario/contraseña, rol, permisos).
- **Agente:** la identidad operativa dentro del call center (número de agente, pertenencia a grupos de agentes, tarifas, estadísticas) — una cuenta necesita estar vinculada a un agente para poder atender llamadas.
- **Extensión (dispositivo):** el teléfono/softphone físico o virtual con el que se hacen y reciben las llamadas (SIP, IAX2, etc.) — un agente necesita una extensión para poder efectivamente hablar.

Una cuenta sin agente puede administrar el sistema pero no atender colas; un agente sin extensión asignada no puede recibir llamadas aunque esté conectado a sus colas.

## Usuario virtual

Empresa cliente atendida dentro de [Oficina virtual / BPO](modulos/oficina-virtual-bpo.md) — comparte el mismo grupo de agentes que otras empresas cliente, pero con su propia base de conocimiento, pantalla emergente, tarifa y registro de llamadas, identificada por su [Número CV](#numero-cv-cvnumber).

## Filtro de reciclaje (recuperación automática)

Regla programada que revisa periódicamente los clientes de una tarea de marcación saliente o de [predial](#predial-pre-dial) y mueve automáticamente a la lista de marcado a los que cumplen cierta condición (ej. "no contactado ayer", "cita programada ya vencida") — evita tener que reciclar manualmente cliente por cliente.

## Diccionario de coincidencia (import dictionary)

Tabla de mapeo usada al importar datos (clientes, listas negras, etc.) que traduce valores de texto libre del archivo origen a los valores enumerados que espera un campo del sistema — por ejemplo, mapear la columna "sexo" con valores "M"/"F" al campo `gender` que solo acepta `male`/`female`.

## Aplicación de negocio (business app)

Registro que vincula un módulo funcional (marketing outbound, atención al cliente, oficina virtual) con un número/DID de entrada, para que el sistema sepa a qué pantalla y a qué configuración de negocio dirigir cada llamada entrante — se administra desde **Administración avanzada del call center → Vinculación de aplicación de entrada**.

## Predial (pre-dial)

Modo de marcación saliente donde el sistema marca de antemano un lote de clientes y solo asigna un agente disponible cuando alguno contesta — así el agente nunca espera un tono de "ocupado" o "no contesta". Requiere una tarea de marcación saliente y no está disponible si la tarea usa la tabla maestra de clientes. Es el término estándar de este wiki para este mecanismo — evitar "predevolución", usado antes en algunos artículos para lo mismo.

## WSDL

Sigla de *Web Services Description Language*. Documento XML que describe las operaciones disponibles de la interfaz WebService de AsterCC — se usa para generar automáticamente el cliente de integración en la mayoría de los lenguajes de programación, en vez de armar las peticiones HTTP a mano.

## SLA / nivel de servicio

Porcentaje de llamadas entrantes contestadas dentro de un umbral de tiempo definido (ej. "80% en menos de 20 segundos") — indicador estándar de la industria de call centers, disponible en el reporte de desempeño de grupo de agentes.

## Grupo de cuentas vs. grupo de agentes

Dos agrupaciones distintas que no deben confundirse: un **grupo de agentes** determina qué agentes atienden qué colas (organización operativa del trabajo); un **grupo de cuentas** es una agrupación administrativa de cuentas de usuario (ej. para asignar una tarifa de extensión o un troncal específico a ese subconjunto de cuentas), independiente de en qué cola trabajen.

## Modo de extensión (fijo / autoadaptable / autoseleccionable)

Determina si una extensión está permanentemente ligada a un dispositivo físico (**fijo**), si el agente puede registrarse desde cualquier dispositivo disponible al iniciar sesión (**autoadaptable**), o si puede elegir entre varios dispositivos disponibles (**autoseleccionable**) — ver también [extensión adaptativa](#extension-adaptativa-modo-autoadaptable-autoseleccionable).

## Tabla maestra de clientes vs. tabla de la tarea

La **tabla maestra** es la base de datos general y compartida de clientes del equipo; una **tabla de la tarea** (o **paquete de clientes**) es un subconjunto extraído de la tabla maestra para una tarea de marcación específica, aislado para no afectar los datos originales ni verse afectado por cambios posteriores en la tabla maestra.

## Comodín (placeholder)

Marcador de la forma `##nombre##` usado en plantillas de correo, SMS o fax, que el sistema reemplaza automáticamente por el dato real del cliente o de la tarea al enviar (ej. `##taskid##`, `##teamname##`, `##param_zipcode##`).

## QC (control de calidad)

Sigla usada indistintamente con "control de calidad" — pantalla donde un supervisor revisa una muestra (o el total, según el porcentaje configurado) de llamadas grabadas de una campaña para calificarlas y, si corresponde, bloquear su edición posterior por el agente.

---

## Fuentes

- `raw/en/others/glossary.txt`
- `raw/zh/其他/名词解释.txt`