---
title: "Códigos de retorno y codificación de idioma"
resumen: "Tabla de referencia de los códigos de error (BackMsg_NN) devueltos por la API de integración, y de los códigos de idioma soportados."
seccion: "7.4 API de integración — Códigos de retorno e idiomas"
tipo: referencia
nivel: avanzado
roles: [desarrollador]
fuente: zh+en
obsoleto: true
relacionados: [introduccion-api-integracion, api-autenticacion-y-sesion, api-control-de-llamada, api-supervision-y-control-de-agente, api-datos-y-grabaciones]
---

# Códigos de retorno y codificación de idioma

## Qué es

Cuando una operación de la [API de integración](introduccion-api-integracion.md) falla, el `message` de la respuesta no siempre es un texto legible: en muchos casos es un **código `BackMsg_NN`** que hay que traducir usando esta tabla. Esta página también documenta los **códigos de idioma** (`cn`, `en`, etc.) usados en parámetros de idioma de otras partes del sistema.

## Cómo se usa

### Códigos de idioma

| Código | Idioma |
|---|---|
| `cn` | Chino simplificado |
| `en` | Inglés |
| `jp` | Japonés |
| `kr` | Coreano |
| `ru` | Ruso |
| `fr` | Francés |
| `de` | Alemán |
| `es` | Español |

### Tabla de códigos de retorno (`BackMsg_NN`)

| Código | Significado |
|---|---|
| BackMsg_01 | Los parámetros no pueden estar vacíos |
| BackMsg_02 | Identificador de organización incorrecto o inexistente |
| BackMsg_03 | Número de agente inexistente o contraseña incorrecta |
| BackMsg_04 | Inicio de sesión exitoso |
| BackMsg_05 | La cuenta del agente está deshabilitada |
| BackMsg_06 | La cuenta del agente no existe |
| BackMsg_07 | Contraseña incorrecta |
| BackMsg_08 | Cierre de sesión exitoso |
| BackMsg_09 | El número de agente indicado no existe |
| BackMsg_10 | Error al cambiar el estado de la cola |
| BackMsg_11 | El ID de grupo de agentes indicado no existe |
| BackMsg_12 | Este agente no existe |
| BackMsg_13 | El parámetro `type` es incorrecto |
| BackMsg_14 | Cambio de estado de cola exitoso |
| BackMsg_15 | La cuenta no existe |
| BackMsg_16 | Llamada fallida: el agente no ha iniciado sesión en la cola |
| BackMsg_17 | Llamada fallida: el agente está en un estado que lo impide (si viene vacío, ver BackMsg_16) |
| BackMsg_18 | Llamada fallida: el agente tiene restringida la marcación saliente |
| BackMsg_19 | Llamada exitosa |
| BackMsg_20 | Llamada fallida |
| BackMsg_21 | Error en la operación de consulta |
| BackMsg_22 | No repita la solicitud de marcado mientras hay una en curso |
| BackMsg_23 | El agente no tiene extensión configurada, no se puede marcar |
| BackMsg_24 | Agente no encontrado, no se puede marcar |
| BackMsg_25 | El agente a consultar no ha iniciado sesión en la cola |
| BackMsg_26 | Error al crear los datos de la parte consultada |
| BackMsg_27 | Operación de consulta exitosa |
| BackMsg_28 | Parámetro incorrecto |
| BackMsg_29 | Transferencia fallida |
| BackMsg_30 | El grupo de agentes no existe |
| BackMsg_31 | Transferencia exitosa |
| BackMsg_32 | Recuperar llamada: operación exitosa |
| BackMsg_33 | Recuperar llamada: operación fallida |
| BackMsg_34 | Conferencia exitosa |
| BackMsg_35 | Conferencia fallida |
| BackMsg_36 | Error al colgar |
| BackMsg_37 | Colgado exitoso |
| BackMsg_38 | El agente no tiene una cuenta asociada |
| BackMsg_39 | Intervención exitosa |
| BackMsg_40 | Intervención fallida |
| BackMsg_41 | Monitoreo exitoso |
| BackMsg_42 | Monitoreo fallido |
| BackMsg_43 | Consulta de datos exitosa |
| BackMsg_44 | Consulta fallida, sin datos coincidentes |
| BackMsg_45 | La llamada actual no admite interrupción forzada |
| BackMsg_46 | Interrupción forzada exitosa |
| BackMsg_47 | Interrupción forzada fallida |
| BackMsg_48 | Susurro exitoso |
| BackMsg_49 | Susurro fallido |
| BackMsg_50 | Este grupo de agentes no existe en el equipo actual |
| BackMsg_51 | Retención de llamada: operación fallida |
| BackMsg_52 | Retención de llamada: operación exitosa |
| BackMsg_53 | Reanudar llamada: operación fallida |
| BackMsg_54 | Reanudar llamada: operación exitosa |
| BackMsg_55 | Número de agente incorrecto o inexistente |
| BackMsg_56 | No se puede consultar: el agente está en un estado que lo impide |
| BackMsg_57 | No hay grupos de agentes disponibles para iniciar sesión |
| BackMsg_58 | No ha iniciado sesión en ningún grupo de agentes |
| BackMsg_59 | Cambio de modo de trabajo posterior a la llamada (ACW) exitoso |
| BackMsg_60 | El grupo no tiene sesión iniciada, o el agente no pertenece a él |
| BackMsg_61 | Fin del modo de trabajo posterior a la llamada exitoso |
| BackMsg_62 | Cambio de modo de trabajo exitoso |
| BackMsg_63 | Se llamó con `usertype=account` pero la cuenta no existe o la contraseña es incorrecta |
| BackMsg_64 | El canal de la llamada no existe |
| BackMsg_65 | Este agente no es supervisor del grupo |
| BackMsg_66 | El agente ya está en estado de pausa |
| BackMsg_67 | ID de tarea de marketing outbound incorrecto |
| BackMsg_68 | No es supervisor del grupo |
| BackMsg_69 | Importación de datos al predial completada |
| BackMsg_70 | Los parámetros `modeltype` o `model_id` están mal definidos |
| BackMsg_71 | El parámetro `context` no puede estar vacío |
| BackMsg_72 | El parámetro `source` está mal definido |
| BackMsg_73 | La tarea de marketing outbound no existe |
| BackMsg_74 | El encabezado del archivo no coincide con la estructura de la tabla |
| BackMsg_75 | El parámetro `context` es incorrecto, no se pudo construir la consulta |
| BackMsg_76 | Falta un campo obligatorio en el archivo |
| BackMsg_77 | Reinicio del estado del cliente exitoso |
| BackMsg_78 | Actualización de datos del cliente exitosa |
| BackMsg_79 | Liberación del agente asignado exitosa |
| BackMsg_80 | Inserción en la lista de predial exitosa |
| BackMsg_81 | Datos duplicados |
| BackMsg_82 | Número de teléfono duplicado |
| BackMsg_83 | Datos importados al paquete de clientes e insertados en el predial correctamente |
| BackMsg_84 | Datos importados al paquete de clientes correctamente |
| BackMsg_85 | Error al almacenar los datos |
| BackMsg_86 | Solo se admite la importación de archivos CSV |
| BackMsg_87 | Error al crear la tarea de importación |
| BackMsg_88 | Error al subir el archivo |
| BackMsg_89 | Error al obtener el archivo remoto |
| BackMsg_90 | El agente no está en modo posterior a la llamada, no es necesario finalizarlo |
| BackMsg_91 | Cambio de modo de trabajo fallido (grupo sin sesión, inexistente, o agente no pertenece a él) |
| BackMsg_92 | No hay ninguna llamada relacionada |
| BackMsg_93 | No hay ningún agente en el grupo o equipo |
| BackMsg_94 | No hay agentes con ese estado |
| BackMsg_95 | Ya está en estado de consulta, no se puede iniciar otra |
| BackMsg_96 | No se puede retener/reanudar: no es una llamada exclusiva entre agente y cliente |
| BackMsg_97 | El parámetro `dtmf` solo admite números, `*` y `#` |
| BackMsg_98 | Envío de DTMF fallido |
| BackMsg_99 | Envío de DTMF exitoso |
| BackMsg_100 | Error de conexión con el núcleo (Asterisk) |
| BackMsg_101 | `varname` solo admite mayúsculas, números, `-` y `_`, y debe empezar con mayúscula o número |
| BackMsg_102 | Configuración de datos adjuntos (`setvar`) exitosa |
| BackMsg_103 | Configuración de datos adjuntos fallida |
| BackMsg_104 | No se permite transferir a IVR durante una consulta |
| BackMsg_105 | No se permite la transferencia con liberación durante una conferencia |
| BackMsg_106 | El IVR principal no existe, verifique el parámetro `ivrexten` |
| BackMsg_107 | Flujo de IVR incorrecto, verifique el parámetro `ivrflow` |
| BackMsg_108 | Transferencia del agente a IVR exitosa |
| BackMsg_109 | Transferencia del agente a IVR fallida |
| BackMsg_110 | La extensión no existe |
| BackMsg_111 | Debe cerrar sesión en la cola antes de configurar la extensión |
| BackMsg_112 | Configuración de extensión completada |
| BackMsg_113 | Error al crear los datos de la cuenta |
| BackMsg_114 | Error al crear los datos del agente |
| BackMsg_115 | Se superó el número de licencias de agente autorizadas |
| BackMsg_116 | Error de licencia del servidor actual |
| BackMsg_117 | Solicitud de marcado desde la app fallida |
| BackMsg_118 | El agente no tiene extensión configurada |
| BackMsg_119 | No se pudo obtener el estado de registro de la extensión |
| BackMsg_120[ip] | Solicitud enviada al teléfono Yealink en la IP indicada |
| BackMsg_121 | Esta extensión ya está en uso por otro agente con sesión iniciada |
| BackMsg_122[tipo] | Modelo de teléfono Yealink no soportado |
| BackMsg_123 | El agente no pertenece a ningún grupo |
| BackMsg_124 | Eliminación de datos del agente exitosa |
| BackMsg_125 | El agente está en una llamada, no se puede eliminar del grupo |
| BackMsg_126 | El agente fue eliminado del grupo correctamente |
| BackMsg_404 | El archivo destino no existe |

## Referencia rápida

| Necesito | Usar |
|---|---|
| Traducir un código de error devuelto por la API | Buscar el `BackMsg_NN` en la tabla de arriba |
| Saber qué código enviar para pedir contenido en español | `es` |

---

## Fuentes

- `raw/zh/二次开发者指南/接口开发手册_v2.0/语言编码.txt`
- `raw/zh/二次开发者指南/接口开发手册_v2.0/返回信息编码对照.txt`
- `raw/en/custom_development_guide/apis/language_codes.txt`
- `raw/en/custom_development_guide/apis/return_messages.txt`
