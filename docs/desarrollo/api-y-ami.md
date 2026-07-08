---
title: "API y AMI"
resumen: "Referencia de la API HTTP de acciones (asterccinterfaces) y del acceso a AMI que usa AsterCC."
seccion: "7.1 API y AMI"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh
obsoleto: true
relacionados: [asterisk-ami, guia-desarrolladores]
---

# API y AMI

## Qué es

AsterCC expone una **API HTTP simple** (endpoint `asterccinterfaces`) para que sistemas de terceros disparen acciones — originar una llamada, enviar correo/SMS, o buscar una dirección en el mapa — pasando parámetros por query string. Por debajo, AsterCC usa el [Asterisk AMI](../administracion/asterisk-ami.md) para ejecutar las acciones de telefonía.

!!! warning "Puede estar desactualizado"
    Esta referencia proviene de la guía de desarrollo original (v2.0, ~2018). Antes de integrar en producción, valida contra el manual de API vigente de tu versión de AsterCC — la lista de acciones puede haber cambiado.

## Cómo se usa

### Parámetros comunes a toda acción

| Parámetro | Qué es |
|---|---|
| `EVENT` | Nombre de la acción a ejecutar (obligatorio) |
| `FROM` | Origen del número: `Campaign` (tarea de campaña) o `Virtualcustomer` (usuario virtual / oficina virtual) |
| `FROM_ID` | ID de esa tarea o usuario virtual |
| `AN` | Número de agente que origina la solicitud |
| `APW` | Contraseña de ese agente |
| `AGENT_GROUP_ID` | ID del grupo de agentes del solicitante (requerido en algunas acciones) |

### Acciones disponibles

| `EVENT` | Qué hace | Parámetro adicional |
|---|---|---|
| `DIAL_OUT` | Origina una llamada saliente | `TARGET` (número destino) |
| `EMAIL_SMS` | Abre la interfaz de envío de correo/SMS | — |
| `GMAP` | Busca una dirección en el mapa | `ADDRESS` |

### Ejemplo — originar llamada

```html
<iframe
  src="http://<servidor>/asterccinterfaces?EVENT=DIAL_OUT&TARGET=041139735857&AGENT_GROUP_ID=10&FROM=Virtualcustomer&FROM_ID=27&AN=9000&APW=9000"
  style="display:none;">
</iframe>
```

El patrón general es: un botón o evento en el sistema externo inyecta un `<iframe>` oculto apuntando a esta URL con los parámetros correspondientes; el iframe dispara la acción del lado de AsterCC.

### Ejemplo — enviar correo/SMS

```
EVENT=EMAIL_SMS&FROM=Campaign&FROM_ID=8&AN=admin&APW=123456
```

### Ejemplo — buscar en el mapa

```
EVENT=GMAP&ADDRESS=Dalian&FROM=Virtualcustomer&FROM_ID=11&AN=2000&APW=2000
```

### AMI (nivel más bajo)

Para integraciones que necesitan eventos de telefonía en tiempo real (no solo disparar acciones), la vía es conectarse directamente al [Asterisk AMI](../administracion/asterisk-ami.md) — requiere una cuenta con los permisos `read`/`write` adecuados, ya documentados en esa página.

## Referencia rápida

| Necesito | Usar |
|---|---|
| Originar una llamada desde un sistema externo | API HTTP → `EVENT=DIAL_OUT` |
| Recibir eventos de llamada en tiempo real | Conexión directa a AMI |
| Enviar correo/SMS desde un botón externo | API HTTP → `EVENT=EMAIL_SMS` |

---

*Fuente: `raw/zh/二次开发者指南/方法.txt`.*
