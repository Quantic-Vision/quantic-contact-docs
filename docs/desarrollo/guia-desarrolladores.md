---
title: "Guía para desarrolladores"
resumen: "Cómo integrar un sistema propio con AsterCC vía pantalla emergente (pop-up) por eventos JavaScript."
seccion: "7.2 Guía para desarrolladores"
tipo: guia
nivel: avanzado
roles: [desarrollador]
fuente: zh
obsoleto: true
relacionados: [api-y-ami]
---

# Guía para desarrolladores

## Qué es

El caso de integración más común es la **pantalla emergente (pop-up)**: cuando entra o sale una llamada, el sistema del tercero necesita enterarse para mostrar la ficha del cliente correspondiente. AsterCC soporta dos modelos de integración:

- **Embebido:** el agente inicia sesión en AsterCC, y el sistema externo se muestra dentro de un iframe de la plataforma.
- **Independiente:** el agente inicia sesión en el sistema del tercero, sin ver nada de AsterCC directamente (el administrador sí necesita acceder a AsterCC para configuración).

## Cómo se usa

### Integración embebida en el mismo dominio

Aplica cuando el agente entra por la interfaz de AsterCC y la página de negocio vive en el mismo dominio (por ejemplo, alojada en el propio servidor de AsterCC).

1. Sube dos páginas al servidor de AsterCC (ej. en `/var/www/html/asterCC/app/webroot`):
   - Una página que **recibe eventos** de llamada.
   - Una página de **pop-up** que se abre cuando corresponde.
2. Registra la página receptora como enlace de trabajo de una tarea de campaña (o servicio de atención al cliente), usando **Gestión de enlaces** para crear un enlace de tipo "enlace de plan de marcación" apuntando a tu archivo.
3. Asigna esa tarea como el flujo por defecto entrante/saliente del grupo de agentes correspondiente.
4. En la página receptora, implementa una función JavaScript que reciba el evento de llamada (parámetros separados por `&`, ej. `source=AGENT&event=ringing&calleridnum=...`) y, si el evento es un timbrado de agente, abra una nueva pestaña con la URL de la página de pop-up, pasando el número de teléfono como parámetro.

```javascript
function sonAccept(msgStr) {
  var eventAll = msgStr.split('&');
  var aryEvent = {};
  for (var i = 0; i < eventAll.length; i++) {
    var pair = eventAll[i].split('=');
    aryEvent[pair[0]] = pair[1];
  }
  if (aryEvent['source'] == 'AGENT' && aryEvent['event'] == 'ringing') {
    var popupUrl = 'popup.html?phone=' + aryEvent['calleridnum'];
    window.top.addTab('tab_' + aryEvent['calleridnum'], popupUrl, aryEvent['calleridnum'], 'yes');
  }
}
```

5. Prueba marcando desde un softphone de agente — la página de pop-up debería recibir el número por parámetro de URL.

### Integración cross-domain (sistema propio fuera del servidor de AsterCC)

Sigue el mismo principio, pero la comunicación entre el iframe de AsterCC y tu dominio requiere mecanismos cross-domain (`postMessage` u otro puente JS), en vez de acceso directo al DOM del padre como en el ejemplo de arriba. La API HTTP de [acciones](api-y-ami.md) es la vía complementaria para que tu sistema, del otro lado, dispare acciones hacia AsterCC (originar llamada, etc.).

## Referencia rápida

| Necesito | Enfoque |
|---|---|
| Mostrar mi CRM cuando entra una llamada | Página receptora de eventos + pop-up, registrada como enlace de trabajo |
| Que mi sistema externo origine llamadas | [API HTTP de acciones](api-y-ami.md) |
| Recibir eventos de llamada en tiempo real fuera del navegador | Conexión directa a [AMI](../administracion/asterisk-ami.md) |

---

## Fuentes

- `raw/zh/二次开发者指南/如何将第三方系统与astercc集成.txt`