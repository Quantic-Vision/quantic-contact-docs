---
title: "Preguntas frecuentes"
resumen: "Preguntas conceptuales frecuentes sobre AsterCC — para errores específicos, ve a Solución de problemas."
seccion: "8. Preguntas frecuentes (FAQ)"
tipo: faq
nivel: basico
roles: [administrador, agente]
fuente: zh
obsoleto: false
relacionados: []
---

# Preguntas frecuentes

Esta sección responde preguntas conceptuales — "¿qué es X?" o "¿cuál es la diferencia entre X e Y?". Si tienes un **error específico**, ve a [Solución de problemas](../troubleshooting/index.md).

## ¿Cuál es la diferencia entre cuenta, agente y extensión?

- **Cuenta:** unidad de administración del sistema. Hay tres tipos: **administrador de sistema** (máximo permiso), **administrador de equipo** (gestiona cuentas, agentes y PBX de un equipo), y **usuario** (unidad básica de facturación, puede tener cero o más agentes y extensiones).
- **Extensión:** puede ser **interna** (SIP, IAX, DAHDI — el costo de sus llamadas salientes se factura al usuario asociado) o **externa** (un teléfono normal, solo puede recibir llamadas del sistema). Cada extensión tiene un número interno para comunicarse con otras extensiones.
- **Agente:** la unidad operativa de call center — atiende llamadas entrantes/salientes desde un grupo de agentes. Al configurar un agente se le asigna una extensión (o un número externo), con tres modalidades: **fija** (no cambia), **autoadaptable** (el sistema detecta qué teléfono IP está registrado desde la IP del agente y ajusta la extensión automáticamente), o **autoseleccionable** (el agente elige su extensión al conectarse).

## ¿Cuál es la diferencia entre iniciar/cerrar sesión y check-in/check-out?

- **Iniciar/cerrar sesión (login/logout):** entrar o salir del sistema con usuario y contraseña. El cierre puede ser voluntario o automático por tiempo de inactividad.
- **Check-in/check-out:** entrar o salir de una **cola**. Normalmente cerrar sesión implica también hacer check-out, salvo que dos sesiones usen la misma cuenta de agente simultáneamente (cerrar una no afecta el check-in de la otra), o que el agente sea de tipo **estático** (no hace check-out automático al cerrar sesión).

## ¿Para qué sirve cada uno de los cuatro niveles de tarifa?

Ver el detalle completo en [4.4 Tarifas y facturación](../modulos/tarifas-y-facturacion.md). Resumen:

| Tarifa | Para qué |
|---|---|
| Sistema | Costo real de cada troncal para el operador |
| Equipo | Lo que se le cobra a un equipo/cliente |
| Extensión | Tarifa asociada a una extensión, útil para diferenciar por número/ruta |
| Agente (llamadas entrantes) | Pago por llamada atendida — típico para liquidar agentes freelance/part-time |

## ¿Cómo elijo el modo DTMF correcto?

El modo DTMF define cómo se transmiten los tonos de tecla (usados, por ejemplo, para navegar un IVR). Se configura por troncal:

| Modo | Cuándo usarlo |
|---|---|
| `rfc2833` | El más universal — úsalo salvo que tengas una razón específica para otro |
| `auto` | Deja que el sistema negocie el modo |
| `inband` | Requiere que el códec de voz sea `ulaw` o `alaw` — necesario con algunos operadores/troncales que no soportan `rfc2833` |
| `info` | Vía SIP INFO |

El modo debe coincidir con lo que espera el proveedor del troncal — si el cliente no puede navegar un IVR con el teclado, revisa primero este parámetro.

## ¿Cuál es la diferencia entre AsterCC 0.x y la versión comercial?

La documentación original distingue entre una rama abierta (0.x) y la **versión comercial**, con funciones adicionales de multiempresa (SaaS), facturación en múltiples niveles, y los módulos de negocio descritos en [4. Módulos del sistema](../modulos/index.md). Esta wiki documenta la versión comercial.

---

*Fuentes: `raw/zh/常见问题及解答/账户_坐席和分机之间有什么区别和联系.txt`, `raw/zh/常见问题及解答/登入_登出和签入签出有什么区别.txt`, `raw/zh/常见问题及解答/费率管理下的四个费率都是做什么用的_如何使用.txt`, `raw/zh/常见问题及解答/如何选择dtmf模式.txt`.*
