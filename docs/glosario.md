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

---

*Fuentes: `raw/en/others/glossary.txt`, `raw/zh/其他/名词解释.txt`.*
