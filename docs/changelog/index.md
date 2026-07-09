---
title: "Historial de versiones"
resumen: "Changelog completo de AsterCC, versión por versión, desde 1.1-beta1 hasta 4.2, más el parche de seguridad de login para instalaciones expuestas a internet."
seccion: "10. Historial de versiones (Change Log)"
tipo: referencia
nivel: basico
roles: [administrador, desarrollador]
fuente: zh+en
obsoleto: false
relacionados: [descarga-e-instalacion]
---

# Historial de versiones

Este historial cubre todas las versiones de AsterCC de las que existen notas de cambios en el wiki original, de la más reciente a la más antigua. Los archivos fuente no incluyen fechas de publicación, por lo que no se muestran fechas — solo el orden relativo de versiones.

## Parche de seguridad de login (aplicar si el sistema está expuesto a internet)

Existen reportes de cuentas comprometidas y datos dañados en sistemas AsterCC expuestos directamente a internet, explotando el endpoint `/login/changelogin`. Si tu servidor es accesible desde internet, aplica esto cuanto antes.

**1. Aplicar el parche de login**

1. Respalda los archivos originales:
   ```bash
   cp /var/www/html/asterCC/app/controllers/login_controller.php login_controller.php_bak
   cp /var/www/html/asterCC/app/controllers/logouts_controller.php logouts_controller.php_bak
   ```
2. Descarga el parche desde `http://download2.astercc.org/astercc_login_security_patch.tar.gz` y verifica su integridad (`md5sum`, hash esperado `e7dcf526a00e20da24866d1a3b5b61ae`).
3. Descomprime el paquete (`tar zxf astercc_login_security_patch.tar.gz`) y localiza el subdirectorio que corresponde a tu versión de sistema. Reemplaza `login_controller.php` y `logouts_controller.php` con los del paquete.
4. Si el paquete no incluye tu versión, escribe a `support@astercc.org` indicando la versión del sistema y el número de serie del producto.
5. Si tras reemplazar los archivos aparece un error 500, contacta a soporte e incluye la salida de `uname -m` y `php -v`.
6. Agrega una "sal" (salt) en `/etc/astercc.conf` para dificultar el uso indebido del endpoint de cambio de contraseña, en caso de que la contraseña almacenada en la base de datos se filtre:
   ```ini
   [system]
   changelogin_pnum_salt=1234567890abcdefghizklABCD
   ```
7. **Después del parche:** revisa los datos de equipos, cuentas, agentes y extensiones en busca de registros sospechosos, y rota contraseñas y cadenas de verificación (troncales, extensiones) que puedan haberse filtrado.

**2. Deshabilitar archivos vulnerables a inyección**

Como medida adicional, AsterCC recomienda eliminar (o renombrar con `mv` en vez de `rm` si se prefiere poder revertir) un conjunto de controladores considerados vulnerables a inyección o en desuso, entre ellos: `apac_realtimes_controller.php`, `allocate_controller.php`, `login_new_controller.php`, `unicomgd_controller.php`, `alicallback_controller.php`, `solocallback_controller.php`, `mengs_controller.php`, `account_info_controller.php`, `agent_registers_controller.php`, `api_controller.php`, `astercc_debug_controller.php`, `tmk_region_controller.php`, `tmk_monitor_controller.php`, `ucpay_controller.php`, `ucserver_controller.php`, `outbound/ucpccb_controller.php`, `asradjust_controller.php`, `ningweifs_controller.php`, `axbs_controller.php`, `huawei_controller.php`, `purviews_controller.php`, `resource_controller.php`, `short_links_controller.php`, y (si no aplican a tu implementación) `bills_controller.php` (facturación), `zkr_realtime_status_controller.php` / `zkr_realtimes_controller.php` (solo si no usas ZKR). Los directorios `bpo` y `weixin` pueden eliminarse por completo si no se usan esos módulos, y `didweb` y `kakao` (este último solo fuera de Corea) también pueden retirarse. `provisions_controller.php` y `systemevents_controller.php` deben renombrarse (no eliminarse) mientras se espera un parche definitivo.

**3. Endurecimiento adicional recomendado**

- **Restringir la IP de registro de extensiones:** en PBX avanzado → Plantillas de PBX, edita el detalle de "default sip device" para limitar la(s) dirección(es) IP permitida(s) de registro.
- **Restringir el acceso al sistema por rango de IP:** en Sistema → Configuración del sistema → pestaña de configuración avanzada, define los rangos de IP autorizados.
- **Filtrar por país/región a nivel de firewall:** usando las reglas del proveedor cloud, o combinando GeoIP/`ipset` con Nginx/`iptables`/`firewalld` para bloquear tráfico fuera de la región de operación (por ejemplo, permitir solo IPs de China en los puertos 80 y 5060 usando `ipset create china hash:net` con la lista de bloques de `ipdeny.com`).
- **Bloquear en Nginx solicitudes con palabras clave SQL sospechosas**, por ejemplo:
  ```nginx
  location / {
      if ($args ~* "(\b(union|insert|alter|truncate|executesql|DECLARE|replace)\b)") {
          return 403;
      }
  }
  ```

## AsterCC 4.2

**Notas de versión:** esta versión requiere instalarse sobre Rocky Linux 9.x. El stack de soporte más reciente es Rocky Linux 9.6 (Blue Onyx), kernel 5.14.0-570.58.1.el9_6.x86_64, Asterisk 13.38.3, Nginx 1.20.2, PHP 7.4.33, MariaDB 10.5.29 y Redis 6.2.20.

- Compatibilidad completa con el entorno de ejecución Rocky Linux 9.x + PHP 7.4.
- Se agregó la extensión `spout` para permitir la importación de archivos `.xlsx`.
- Soporte para cifrado de tablas InnoDB de MariaDB (instrucciones de uso en `inst-shell/MariaDB_InnoDB_Encrypted.md` dentro del paquete de código).
- Mejora de seguridad para evitar inicios de sesión no autorizados a través del endpoint `/login/changelogin` tras una filtración de contraseñas: se puede configurar una "sal" (números y letras, sensible a mayúsculas/minúsculas) en `/etc/astercc.conf`.
- Actualización de plugins de frontend: jQuery a la versión 1.7.2, jQuery UI a la 1.12.0, jQuery Layout a la 1.3.0-rc-30.79 y el plugin de validación jQuery a la 1.9.0.
- Correcciones en el framework CakePHP para asegurar compatibilidad con PHP 7.4.

## AsterCC 4.1

### Nuevas funcionalidades

- Soporte para Rocky Linux 9.x y PHP 7.4.
- Conexiones a Redis con autenticación por contraseña, y caché de esquema (schema cache) en Redis.
- Bloqueo de llamadas salientes para extensiones de agente en pausa.
- Nuevo campo `label` en la lista de no llamar (DNC), visible también en las opciones de la página de campañas.
- Cambio en el formato de fecha y en la presentación de la lista DNC.
- Cuando un agente recibe una notificación de recarga del grupo de agentes, su página muestra ahora una cuenta regresiva automática de recarga (la duración viene indicada en el propio evento).
- Modificar los parámetros de colgado automático de un grupo de agentes ahora dispara la recarga del archivo de configuración de colas.
- Bloqueo de inicio de sesión tras cierto número de intentos fallidos de contraseña.
- Filtros por grupo de agentes y por tarea de marcación saliente en el resumen de llamadas salientes.
- Cambio a un reproductor basado en HTML5 para anuncios y buzones de voz.
- Soporte para almacenar por separado los canales de archivos WAV estéreo (dos canales).
- Los usuarios no administradores ahora pueden importar campañas/listas masivas.
- Nueva opción de enrutamiento por sondeo (round-robin) de grupo.
- Reproducción de un mensaje de voz cuando el IVR marca hacia una línea externa.
- La importación ahora admite archivos `.xlsx`.

### Corrección de errores

- Al eliminar entradas de la lista negra de salientes, la eliminación ahora usa el ID del registro, corrigiendo el problema de números ocultos que no se podían borrar.
- Corrección de un bug en AGI donde la coincidencia contra la lista DNC ignoraba mayúsculas/minúsculas incorrectamente.
- Corrección de problemas de falta de memoria causados por listas negras excesivamente grandes.
- Exportación de grabaciones: se optimizó el empaquetado para evitar fallos de conexión a MySQL al empaquetar/exportar grandes cantidades de archivos.
- Corrección de las condiciones de consulta SQL de `campaign_dncs` en AGI.
- Corrección de las condiciones SQL usadas por AGI al buscar cuentas de entrada.
- Corrección de caídas de llamada al transferir agentes salientes al IVR.
- Corrección de un fallo al crear la tabla `bind_phone` causado por un campo `tablename` demasiado largo.
- Corrección de un problema que impedía colgar llamadas transferidas.
- Resolución de problemas de permisos para usuarios en la gestión de equipos de sub-CDR.
- Las estadísticas ahora toleran un `pause_reason` vacío sin fallar.
- Mejora en la visualización de adjuntos de la base de conocimiento.
- Corrección de un problema donde las transferencias salientes no entraban al flujo de evaluación de calidad.
- El sondeo previo a la marcación ahora llama a una API para validar el número destino.
- Corrección de fallos de autorización causados por espacio insuficiente en disco.
- Corrección de la visualización del nombre del cliente en llamadas entrantes de atención al cliente.
- Se agregó un parámetro de alcance de control de calidad y se corrigió un problema de reproducción de grabaciones.
- Corrección de un problema que impedía a los no administradores editar horarios de trabajo.
- Corrección de un problema en versiones recientes de Nginx HTTP Push donde a varios eventos les faltaba el `\r\n` final.
- Corrección de valores de estado incorrectos al agregar reglas de relevo de troncal/grupo.

## AsterCC 3.2-rc1

### Nuevas funcionalidades

- Actualización del refresco de información del cliente en ventanas existentes para llamadas entrantes; actualización de la API del plugin de Chrome; ajuste del script de reconocimiento de voz de Alibaba (ASR).
- La API de consulta de resultados de llamada ahora soporta múltiples `sessionid` a la vez, y solo ejecuta la consulta cuando el `sessionid` existe (evita consultas innecesarias).
- Nuevo campo de ID de WeChat en la cuenta; soporte de reconocimiento de una sola frase de Alibaba Cloud.
- Cifrado/descifrado del contenido de las grabaciones de llamadas.
- Soporte de WeChat en dispositivos móviles para el módulo de atención al cliente; nueva interfaz de envío de noticias/push para WeChat.
- Nuevo módulo de control de calidad con inteligencia artificial (calidad inteligente), con páginas propias para tareas, reglas y condiciones de control de calidad; soporte de reconocimiento local; página de vocabulario sensible; función de recuperación en resultados de control de calidad para volver a revisar datos; opción de revisión manual adicional; los registros de control de calidad ahora registran el número de coincidencias de condiciones, reglas y estándares; el estándar de control de calidad ganó un campo de resultado, y el script de control de calidad actualiza el resultado en el perfil del cliente al mismo tiempo que su estado.
- Reproducción de un mensaje de voz al alcanzar el límite de número de llamadas; nuevo parámetro de interruptor (`chkNoAnswerLastHour`) para no permitir llamar a números que no contestaron en la última hora.
- Búsqueda por nombre de cliente en la página de registros de llamadas (CDR) de campañas de marcación saliente.
- En el monitoreo de agentes: filtro por grupo de agentes, columna de hora de inicio de estado en el monitoreo del supervisor, y posibilidad de que el supervisor adjunte archivos desde la página de monitoreo.
- Al editar un agente se muestra su nombre; soporte de motivos de pausa personalizados, visibles tanto en el detalle de servicio del agente como en el menú desplegable de pausa de la interfaz del agente.
- Ocultar los primeros 4 dígitos del número de teléfono del cliente, incluyendo en las exportaciones a XLS/CSV.
- Nuevas validaciones de canal al hacer check-in forzado de una extensión ya en uso, y en pausa, reanudación, transferencia, recuperación, consulta, configuración de datos adjuntos a la grabación y transferencia de colgado en IVR.
- Se agregaron sub-CDR para las aplicaciones de IVR y de mensajes de voz.
- En la importación de datos del centro de llamadas, los números repetidos en el pre-marcado ahora también actualizan los datos existentes.

### Corrección de errores

- Corrección de un bug al ocultar el número telefónico del cliente.
- Corrección de bugs en el script de traducción de grabaciones, incluyendo manejo de registros cuya ruta de grabación existe pero el archivo no; se agregó registro de errores y se eliminó el timeout de 45 segundos en la subida de archivos a Alibaba Cloud.
- Corrección de un bug donde el agente entraba en espera con música (MOH) al responder una consulta.
- Corrección de fallos al exportar a XLS desde la página de tareas de control de calidad inteligente, desde la página de estándares de control de calidad y desde la página de reglas (esta última fallaba cuando el archivo exportado contenía el carácter `&`); corrección de errores ortográficos.
- Mejoras y validaciones adicionales en las páginas de tareas y condiciones de control de calidad, incluyendo que el destino de datos sea obligatorio y corrección de problemas de multi-idioma entre condiciones y reglas.
- Mejora del método de consulta SQL de la página de sub-registros de llamadas.
- Corrección de un bug en la asignación automática de marcación saliente que buscaba agentes en línea de cualquier tarea en vez de solo los de la tarea actual.
- Se agregó `act_callerid` a los eventos `callee_ring` (marcación por clic) y `agent_ring` (pre-marcado); corrección de un bug donde no se detectaban números en la lista de bloqueo que empezaban con 0.
- Corrección de un error en la construcción de la consulta SQL del reporte semanal de servicio por grupo de agentes.
- Corrección de un bug en el filtro de agentes del monitoreo de grupos de agentes.
- Eliminación de código de prueba en la página de control de calidad y corrección de un problema donde no se mostraba la calificación.
- Corrección de bugs varios de control de calidad, incluyendo un error de "modelo no encontrado".
- Corrección de una duplicación en el conteo de agentes del gráfico circular de estados de agente cuando un agente pertenece a varios grupos.
- Optimización del control de calidad: el estado de cliente que requiere revisión de calidad ahora puede configurarse por archivo de configuración (por defecto, todo estado distinto de "open").
- Mejora de compatibilidad con nombres de agente muy largos en el módulo de control de calidad.
- El monitoreo de grupos de agentes cambió de cookies a `localStorage` para evitar pérdida de memoria con muchos datos; la importación ahora permite especificar la columna de agente; se agregó atributo `title` al campo de búsqueda para textos largos; corrección de un problema que impedía abrir en Excel el registro de llamadas exportado de tareas de marcación saliente (por un atributo de columna incorrecto).
- Mejora en la interfaz de marcación: si el grupo de agentes tiene restringida la llamada saliente, el campo ya se bloquea de inmediato en vez de requerir un cambio de pantalla para verlo.
- Corrección de un error al crear la tabla de resultados tras crear una tarea de control de calidad.
- Los filtros de las tareas de control de calidad ahora se pueden modificar al editar la tarea.
- Corrección de un problema de falta de audio al escuchar (spy) una llamada que fue transferida a un agente.
- Mejora en la visualización del control de calidad; la duración de la grabación ahora se escribe al momento de la creación.
- Corrección de un problema donde los datos de `curspool` no se limpiaban tras alcanzar el límite de número de llamadas.
- Corrección de un error en el campo de tarificación al obtener el DID.
- El límite de número de llamadas ya no afecta la transferencia a línea externa.
- Correcciones pendientes de la versión 2.6-rc2: mensaje de voz de cambio de contraseña tras check-in telefónico, eliminación de datos de `curagents` que quedaban al hacer check-out del agente; corrección de que Internet Explorer no podía abrir con `window.open` una página de campo de enlace personalizado (por el guion `-` en el nombre de la ventana); el check-out forzado desde el monitoreo en tiempo real de grupos de agentes ahora registra la hora de check-out.
- Corrección de una duplicación de puerto al construir la URL de nombre de host y puerto.
- Corrección de un bug donde la página de registros de llamadas del módulo de marcación saliente no mostraba las llamadas de tareas de tipo "importar y usar de inmediato".
- Corrección de un bug donde un usuario normal usando la función de "importar y usar de inmediato" no obtenía el `team_id`.

## AsterCC 2.6-rc2

**Cuentas, equipos y permisos**

- El identificador de equipo ahora permite el punto (`.`) como símbolo, pero no al inicio ni al final.
- En [Administración de cuentas] -> [Gestión de roles] -> [Agregar], la ventana de configuración de permisos ahora se puede redimensionar y ampliar a pantalla completa con doble clic en el título.
- La vinculación de equipo y dominio (antes el parámetro `login_route` en `astercc.conf`) se movió a [Configuración del sistema] -> [Configuración avanzada del sistema].

**PBX**

- Mejora del aviso de números DID duplicados: al agregar varios DID en lote, ahora se muestra cuántos números tuvieron éxito, cuántos se repitieron y cuántos fallaron.

**Administración avanzada de PBX**

- En [Restricción de números salientes], se agregó la función de eliminación en lote.

**Marcador y campañas**

- Las tareas de marketing outbound ahora admiten clonación: copia toda la configuración de una tarea existente a una nueva (se puede cambiar el nombre y el grupo de agentes), sin clonar la encuesta vinculada.
- Mejora de permisos de campos en la interfaz de trabajo del agente: se respetan los campos configurados como "editar", "ver" y "obligatorio" en la configuración de campos del panel frontal.
- Los campos frontal/trasera de la tarea permiten configurar si el número de agente (`agentno`) se muestra, con permiso de solo lectura.
- Los datos del cliente en campañas ahora incluyen el resultado de reconocimiento (ASR).

**Administración avanzada del call center**

- En [Administración avanzada del call center] -> [Importar datos], se agregó la importación de restricciones de números salientes.
- Optimización de rendimiento en la importación de datos del sistema.

**Información en tiempo real**

- En [Monitoreo de grupos de agentes], se agregó la función "Seleccionar todo / Deseleccionar" tanto para equipos como para grupos de agentes; al seleccionar un equipo se seleccionan automáticamente todos sus grupos de agentes.
- La página de información del sistema ahora muestra la versión actual.

**Configuración del sistema**

- Mejora de retención de recordatorios de agenda y mensajes internos: el tiempo de retención de datos de agenda pasó de 30 a 7 días por defecto; se agregó el parámetro de retención de datos de mensajes, también en 7 días.

**Marcador predictivo**

- Nuevo reporte de causas de llamadas no contestadas en marcado predictivo, con gráfico circular que muestra proporción y cantidad por estado, a nivel de campaña completa.

**Atención al cliente entrante**

- Los campos mostrados en el panel frontal de la tarea de atención al cliente entrante ahora son consistentes con la configuración de campos de la tabla general.

**Interfaz de agente**

- En la página de consulta del panel de trabajo del agente se agregó un botón de actualización para refrescar el estado de disponibilidad para consulta.

**Corrección de errores**

- Corregido un error donde, si un mismo troncal pertenecía a varios grupos de troncales, al eliminar las reglas de ese troncal en un grupo se eliminaban por error también las reglas del mismo troncal en otros grupos.
- Corregido que en gestión de calidad y gestión de clientes de campañas, el buscador no mostraba los resultados de llamada compartidos por el equipo.
- Ajuste de estilo en el buscador de la página de asignación manual de tareas outbound.
- Corregido error que impedía descargar datos en la página de tareas por lotes según distintos alcances de permisos.
- Corregido error de desalineación de columnas en archivos `.csv` exportados desde el backend.
- Corregido error de idioma en campos personalizados de clientes en la configuración de cuotas de encuestas.
- Mejora en encuestas de voz: ahora se permite el salto en la última pregunta.
- Mejoras de idioma en encuestas y corrección de confusión entre número de secuencia y número de pregunta.
- Mejora del monitoreo en tiempo real: el "tiempo desde la última llamada" en el monitoreo de grupos de agentes ahora se calcula desde el fin de la llamada, no desde el inicio.
- Corregido error de paginación en la lista de la base de conocimiento.
- Corregido error de búsqueda en gestión de clientes y gestión de calidad cuando el resultado de llamada contenía comas.
- Corregido que un agente dinámico marcado como estático por el administrador todavía podía cerrar sesión.
- Corregido que, al iniciar sesión como administrador de equipo, no se podía volver a ingresar tras cambiar la contraseña en la página de información básica.
- Corregido que al quitar un agente de su grupo de salida actual no se liberaba la vinculación con ese grupo.
- Se ocultó el mensaje de error de `pcilib` (`sysfs_read_vpd: read failed: Connection timed out`) que aparecía en algunas máquinas al ejecutar `lspci`, para evitar confusión.
- Corregido que en el panel de trabajo de marcado outbound, si una tarea tenía varias encuestas, no se podía elegir cuál abrir (se recomienda usar una encuesta por tarea).
- Corregido que una desvinculación incorrecta entre una tarea outbound y e-commerce dejaba el popup de cliente en blanco en la interfaz del agente.

## AsterCC 2.6-rc1

**Nuevas funciones**

- Nuevo parámetro `ivrinputcode` en `astercc.conf`: cuando tiene valor, el sistema solo guarda en el CDR el código de entrada IVR correctamente transferido.
- Registro de la fecha de la primera llamada del agente al cliente en el módulo de campañas.
- Nueva interfaz (API) de transferencia ciega para agentes.
- Nuevos parámetros `cid_btrans` y `cid_consult` en `astercc.conf` para controlar si se usa el número original al hacer transferencia ciega o consulta hacia líneas externas de terceros.
- Soporte de TLS en el servidor SMTP.
- Auto-relleno de la MAC en el aprovisionamiento automático de dispositivos.
- Soporte de libreta de direcciones para aprovisionamiento automático de teléfonos Yealink.
- Nuevo reporte de calificación (ranking) de agentes.
- Soporte de TTS de Baidu.
- Uso de `*65` para cerrar sesión del agente vinculado a la extensión.
- Nueva opción en IVR para que el agente cambie su contraseña tras iniciar sesión por teléfono.
- Soporte para el plugin `astercc-chrome-plugin`.
- Prioridad de DID para colas.
- Al exportar órdenes de trabajo, se exportan también el identificador de llamada y el DID de las llamadas relacionadas.
- Uso de Redis para cachear el esquema de tablas de MySQL.
- Apertura automática de la orden de trabajo en el módulo de atención al cliente entrante.
- La orden de trabajo puede leer datos del cliente en el módulo de atención al cliente.
- Cierre automático del estado de trabajo posterior a la llamada (ACW) tras guardar una opción en atención al cliente.
- Cierre automático de la pestaña tras guardar una opción en atención al cliente.
- Nueva opción en campañas para recordar al agente guardar el resultado de la llamada.
- Se permite que el creador o el administrador del grupo de agentes revise órdenes de trabajo.
- Protección contra corrupción de datos causada por cortes de energía.

**Corrección de errores**

- Corregido que, al importar clientes duplicados, se perdían el estado del cliente y el agente asignado.
- Corregido que, al marcar "reasignar agente" en la importación, se reseteaba el agente de clientes duplicados; ahora, si los datos están duplicados, no se modifican.
- Corregido error de JSON al abrir la ventana de selección de agentes cuando el nombre de usuario contenía caracteres chinos de más de 6 bytes.
- Mejora de la consulta SQL de verificación de duplicados al importar múltiples números de marcado predictivo, para acelerar la importación.
- Optimización de la consulta de exportación en el detalle de servicio de atención entrante (estadísticas).
- El detalle de servicio de atención entrante y el detalle de IVR entrante ahora muestran y exportan el campo de entrada del usuario en IVR.
- Corregido que, tras transferir una llamada, el agente no podía volver a hacer consulta o transferencia hasta que finalizara la llamada transferida.
- Corregido que, si existía una llamada transferida sin colgar, una nueva consulta o transferencia del agente usaba el canal equivocado.
- Corregido error en la fecha de primera llamada: en planes que usan la tabla general de clientes, este campo no se actualizaba.
- Corregido que la tarea nocturna (`nighttask`) eliminaba directorios de tipo distinto a año al limpiar el directorio `getMonitor` cuando el nombre no era numérico.
- Nueva función de exportación del contenido de mensajes enviados; el archivo `.xls` ahora se exporta en segundo plano.
- El monitor de pantalla grande ahora permite filtrar por grupo de agentes seleccionado y se agregaron dos vistas gráficas adicionales.
- En el popup de atención al cliente entrante, si el cliente está en estado de llamada conectada, es obligatorio seleccionar un motivo de llamada antes de poder cerrar el popup.
- Corregida la imprecisión en la duración del estado del agente mostrada en el monitor de pantalla grande.
- Corregido que, al generar una orden de trabajo, el aviso en la interfaz del agente mostraba "undefined".
- Corregido que, al seleccionar grupo de agentes y agente en la página de tareas, el agente correspondiente no recibía el aviso de la tarea.
- Corregido error al agregar contactos frecuentes para usuarios de llamadas entrantes virtuales.
- Corregido error en la exportación por totales del detalle de servicio de agentes.
- Corregido que, tras una transferencia por consulta, no se podía volver a consultar; y que si la interfaz de control de sub-grabación no llamaba a `stop` antes de colgar, la siguiente llamada no podía llamar a `start`.
- Corregido error de `vartoagent` en eventos de bifurcación (`split`).
- Corregido que, en la página de tareas outbound, al hacer asignación manual, la lista de resultados de llamada en el buscador era incorrecta (no aparecían los resultados si solo se elegía el equipo sin la tarea).
- Corregido que el script de importación `asterccimport.php` solo verificaba duplicados en el campo `phone1`.

## AsterCC 2.4-rc2

**Administración avanzada de PBX**

- La calificación de agente (QC Rate) ya no está limitada al rango de 1 a 5.

**Reportes y estadísticas**

- Se agregó el botón rápido "Ayer" en la página de detalle de servicio de agentes.
- Se agregó exportación en segundo plano (tarea shell) para el detalle de servicio IVR entrante.
- Se agregó la página de reporte regional dentro de estadísticas.

**Marcador y campañas**

- En la página de asignación automática de tareas outbound, el botón "Aceptar" se renombró a "Guardar plan de asignación automática" para evitar operaciones accidentales.
- El estilo de distribución por defecto en la asignación automática de clientes ahora es "por todos los no asignados".

**Mensajería masiva**

- El proveedor de SMS ahora se puede configurar por equipo.

**Marcador predictivo**

- Nueva función para colgar a los agentes en estado de timbrado cuando no hay agentes libres; se configura en [Tareas outbound] -> [Configuración avanzada de marcado predictivo] -> "Colgar timbrado sin agente disponible".

**Configuración del sistema**

- En modo de dispositivo (extensión), el tiempo de espera para recuperar una llamada aparcada (`call-parking`) pasó de 12 a 300 segundos.

**Atención al cliente entrante**

- Se agregó el campo de grupo de agentes en la página de llamadas perdidas de atención al cliente entrante.

**Interfaz de agente**

- Al detectar datos de marcado erróneos, ahora se agrega un botón "Continuar marcado" que limpia automáticamente el dato erróneo anterior e inserta una nueva solicitud de marcado (antes solo se advertía no repetir el marcado).
- En [Mensajería masiva] -> [Gestión de anuncios] -> [Agregar anuncio], se agregó la función "Seleccionar todo" para los destinatarios.
- El formato de ocultación de números se modificó: se ocultan las posiciones 5 a 8 contando de derecha a izquierda; si el número tiene menos de 5 dígitos, se oculta por completo.

**Corrección de errores**

- Corregido que, cuando el alcance de grabación de un equipo era "todos", la generación de grabaciones fallaba en modo de dispositivo (extensión).
- Corregido que, en [Gestión de roles] -> [Agregar], tras el aviso de campos obligatorios, no se podía guardar aunque se completaran los campos.
- Corregido que el campo de detalle de extensión tenía longitudes distintas entre agregar y editar en [Gestión de extensiones].
- Corregido que el campo de número de llamada saliente en [Troncales], al configurarse con múltiples espacios vacíos, quedaba imposible de editar tras guardarse.
- Corregido que el campo de hora de fin no se podía modificar al agregar un horario de trabajo en [Horarios de trabajo].
- Corregido que los campos exportados en [Registro de llamadas] eran inconsistentes entre los formatos `.csv` y `.xls`.
- Corregido que, en el reporte gráfico de agentes, al seleccionar "acumulado de todos los grupos de habilidad" y descargar imagen o PDF, aparecía un aviso pidiendo seleccionar grupo de agentes.
- Corregido que, en tareas outbound que usan la tabla general, al buscar por "fecha de actualización" y eliminar mediante "eliminar según búsqueda", se eliminaban también datos fuera del resultado de búsqueda.
- Corregido que, al generar carpetas de archivos exportados, un nombre con espacios impedía la compresión, bloqueando la descarga del archivo exportado.
- Corregido que al exportar el registro de eventos de agente faltaban campos.
- Corregido que cuentas con alcance de permiso "sistema" tenían por defecto permiso sobre la página de configuración del marcador; ahora este permiso se controla por rol.
- Corregido que, en [Marcador predictivo] -> [Marcador] -> [Recuperar], no se podía programar la recuperación de datos para ejecución inmediata (`0000-00-00 00:00`).
- Corregido un problema al exportar datos en formato `.csv` en [Atención al cliente entrante] -> [Registro de llamadas].
- Corregido que, al desinstalar el módulo de e-commerce, el módulo de gestión de inventario en el menú lateral no se eliminaba de forma sincronizada.
- Corregido que, en el popup de tareas outbound, si el cliente no tenía nombre, la etiqueta mostraba el valor del primer campo frontal configurado; si además la tarea ocultaba el contacto y ese campo era el teléfono 1, el número no se ocultaba en la etiqueta.
- En [Mensajería masiva] -> [Gestión de anuncios] -> [Agregar anuncio], corregido que tras seleccionar un grupo de cuentas por el administrador, las cuentas no aparecían listadas.
- Corregido que, en [Marcador predictivo] -> [Causas de no contactado], cuando el rol tenía alcance de equipo, no se veían las tareas outbound del equipo propio.
- Corregido que en navegadores IE 8/9/10 el estado del agente mostraba "NAN" (el sistema ya no da soporte a IE; se recomienda Firefox o navegadores basados en Chrome).
- Corregida la cuenta regresiva de marcado automático, que siempre iniciaba en 60 segundos.
- Corregido un desbordamiento de memoria en el módulo de push HTTP del programa de fondo.
- Corregido que la tarea programada de composición de archivos no se completaba a tiempo.
- Corregido que no se podía instalar el módulo de atención al cliente entrante al instalar los datos de demostración.

## AsterCC 2.4-rc1

**Nuevas funciones**

- Soporte de motor de reconocimiento de voz (ASR) en chino (iFlytek).
- Uso del motor ASR para reconocer el estado de la llamada mediante media temprana (apagado, ocupado, en curso, número inválido, etc.).
- Al guardar un cliente en una campaña, el sistema puede enviar (POST) toda la información a una URL específica.
- Nueva información al exportar datos de clientes de campañas: hora de inicio y fin de la última llamada, y duración de la última llamada.
- Exportación de estadísticas del detalle de servicio de agentes mediante tarea en segundo plano.
- Herramienta de línea de comandos para regenerar y recargar toda la configuración.
- Nueva interfaz para llamadas de conferencia entre dos números externos, con paso de tonos DTMF.
- Protección contra corrupción de datos causada por cortes de energía.

**Corrección de errores**

- Corregido que, al activar "ocultar contacto", el número de teléfono del cliente aún era visible en algunos módulos relacionados.
- Corregido que el menú de la página de importación aparecía duplicado cuando diferentes roles tenían permisos distintos.

## AsterCC 2.3-rc2

**Cuentas, equipos y permisos**

- Ampliación del rango de grabación: la grabación de llamadas contestadas ahora comienza desde el timbrado, no desde la respuesta.
- Al quitar un agente de su grupo, se verifica si su grupo de salida actual es el mismo que se está eliminando.
- Nueva configuración de cierre automático del estado posterior a la llamada (ACW) tras N segundos por grupo de agentes.
- Nueva interfaz webservice de estadísticas de agentes por grupo del día.
- El área de búsqueda ahora ajusta su ancho de forma automática (diseño responsive).

**PBX**

- El script de procesamiento de grandes volúmenes de datos ahora también limpia los sub-CDR antiguos según el tiempo de retención histórica configurado.

**Administración avanzada de PBX**

- En [Administración avanzada de PBX] -> [Gestión de anuncios de voz], al agregar un anuncio se puede elegir motor TTS.
- Las acciones de IVR (principal y sub-IVR) incorporan una condición de tiempo (`judge_time`).
- En IVR, las acciones "Reproducir anuncio" y "Leer datos" ahora admiten archivos de voz tipo PTTS.
- Se agregó escape/traducción de caracteres especiales en la importación/exportación de datos de PBX.

**Reportes y estadísticas**

- En [Detalle de servicio de agentes] se agregaron las columnas `workmode_dialin`, `workmode_dialout` y `workmode_all` para mostrar y exportar.

**Marcador y campañas**

- En la pestaña de "Marcador predictivo" de las tareas outbound se agregó el campo `remote_fields`.
- Las páginas de edición de la tabla general de clientes (individual y organización) ahora muestran el registro de contacto relacionado, incluyendo sus campos personalizados.

**Configuración del sistema**

- Al eliminar un plan de grabación en [Gestión de archivos de grabación], se puede elegir si también se elimina el archivo de respaldo asociado.
- Se agregaron las interfaces `testConnect` y `setNode`.

**Marcador predictivo**

- En [Registro de filtros de marcado predictivo], ahora se puede copiar el SQL (antes solo se podía consultar en modo lectura).

**Interfaz de agente**

- Se agregó un botón de un clic para cambiar el estado de trabajo y modo ACW de todos los grupos de agentes a la vez.
- Al iniciar/finalizar el marcado predictivo, se reemplazó el `alert` de JavaScript por un aviso emergente en la parte superior que desaparece automáticamente sin interrumpir otras acciones.
- Al agregar un nuevo cliente desde el popup de campañas, se actualizan los campos `autocount`, `noanswernum` y `answernum` según la hora de respuesta y fin de la llamada.
- Se agregó un reloj dinámico en la esquina superior derecha de la interfaz de agente.
- Bajo el botón de estado se muestra el estado actual y su duración.
- En el módulo de campañas, al hacer clic en "Obtener cliente" la página abre automáticamente el primer registro de la lista.

**Corrección de errores**

- Corregido el botón "Seleccionar todo" al editar agentes en [Cuentas y permisos] -> [Gestión de grupos de agentes].
- Corregido que se podían ingresar letras en el campo de número de extensión en [Gestión de extensiones].
- Corregido la ruta incorrecta de lectura de la imagen de perfil (avatar por defecto) al editar administrador en [Gestión de salas de conferencia].
- Corregido que las grabaciones seguían existiendo tras eliminarlas en [Gestión de música de espera].
- Corregida una validación regex errónea que no permitía `|` ni `;` al editar contenido TTS en anuncios de voz.
- Se agregó el texto "Seleccionar equipo" antes de "Por favor seleccione" en [Detalle de servicio IVR entrante].
- Corregido que "primera hora de inicio de sesión" y "última hora de cierre de sesión" mostraban el mismo valor en [Detalle de servicio de agentes].
- Corregidos errores en [Oficina virtual] -> [Gestión de clientes]: cuando solo había un usuario, no se mostraban los campos personalizados relacionados en el buscador; y no se podía abrir el desplegable de un campo de prueba tipo "select" en la edición del registro.
- Corregido que existían dos páginas de "gestión de tareas" en administración avanzada del call center; se renombró la página de tareas por lotes (Shell Jobs) a "Gestión de tareas por lotes".
- Corregido que en [Mensajería masiva] -> [Enviar mensaje interno] la columna derecha mostraba empleados de otros equipos.
- Corregido el procesamiento de cadenas en el contenido de SMS.
- Corregido que los comodines de las plantillas de mensajería masiva no reemplazaban el contenido correspondiente.
- Corregido que, en [Mensajería masiva] -> [Servidores de SMS], varios servidores del mismo equipo podían marcarse simultáneamente como "predeterminado".
- Corregido un error de consulta de saldo en la interfaz del proveedor de SMS Xiao.
- En [Configuración del sistema] -> [Gestión de archivos de grabación] -> [Agregar plan]: corregido que había que crear manualmente el directorio si la ruta de destino no existía; y corregido que, con varios planes a la misma hora, solo se ejecutaba el primero.
- Corregido que el filtro de marcado predictivo no funcionaba tras usar "importar y ejecutar".
- Corregido que, al hacer clic en "Obtener cliente", el dato del cliente aparecía como -0.5.
- Corregido que faltaba la opción "Atención al cliente" en el tipo de objeto al buscar plantillas de Email/SMS desde la interfaz de agente.
- Corregido que la ventana del plan de marcado desaparecía al hacer clic en "Actualizar llamadas" del menú.
- Al agregar un cliente nuevo desde el popup de marcado outbound, se actualizan `autocount`, `noanswernum` y `answernum` según hora de respuesta y fin de llamada.
- Corregido que el estado mostraba "NA:NA:NA" al hacer clic en "Actualizar llamadas" del menú.

## AsterCC 2.3-rc1

**Nuevas funciones**

- Soporte para motor ASR chino.
- Uso del motor ASR para reconocer el estado de la llamada (apagado, ocupado, número inválido, etc.).
- Al guardar un cliente en una campaña, el sistema puede enviar la información mediante POST a una URL específica.
- Nueva información al exportar datos de clientes: hora de inicio, hora de fin y duración de la última llamada.
- Exportación mediante tarea en segundo plano en la página de estadísticas de detalle de agentes.
- Herramienta de línea de comandos para regenerar y recargar toda la configuración.
- Nueva interfaz de conferencia entre tres partes con paso de tonos DTMF.

**Corrección de errores**

- Corregido que, con "ocultar contacto" activado, el número de teléfono aún era visible en algunos módulos relacionados.
- Corregido el menú duplicado en la página de importación cuando distintos roles tenían permisos diferentes.

## AsterCC 2.2

**Nuevas funciones**

- En IVR, todas las acciones ahora tienen un destino de fallo configurable.
- Soporte de ASR (reconocimiento de voz) en IVR.
- Soporte de importación/exportación de IVR.
- La interfaz de agente muestra el estado de la cola a la que pertenece.
- Nuevo reporte por agente que incluye todos los grupos a los que pertenece: número de llamadas, duración, duración promedio, tiempo de sesión, tiempo en pausa, etc.
- Nuevas opciones para el panel de aviso de llamada: oculto, fijo o cierre retrasado.
- Nuevo diagrama en tiempo real del estado de llamadas: IVR, en llamada, timbrando, en espera (cola).
- Nuevo editor de texto WYSIWYG.
- Se agregó el número de extensión en la lista de extensiones.
- Las plantillas ahora usan el nombre visible del campo en lugar del nombre de columna de base de datos.
- Las campañas admiten reasignación automática del cliente si el agente no lo contacta en cierto número de días, para que otros agentes puedan obtenerlo.
- Nuevo reporte en el registro de llamadas (CDR) con llamadas entrantes, duración entrante, llamadas salientes, duración saliente, costo entrante, costo de equipo, costo de sistema y costo de usuario.
- Nuevo indicador de estado de extensión en salas de conferencia (verde = en línea, gris = fuera de línea).
- El marcador predictivo admite reintento automático configurable (por ejemplo, a 1, 3 o 12 horas).
- Algunos reportes ahora se ejecutan en segundo plano para evitar tiempos de espera con grandes volúmenes de datos.

**Corrección de errores**

- Corregido que, con contacto oculto activado, el número seguía siendo visible en el historial de contacto.
- Corregido que, al escuchar grabaciones en la página de control de calidad, los datos del cliente aparecían como nulos cuando se usaba la tabla general.
- La página de importación solo muestra la lista negra de llamadas entrantes y DID cuando el usuario es administrador de sistema o de equipo con alcance de sistema/equipo.
- Corregido error al enviar correos no-MIME desde el panel de agente.
- Corregido error de estilos (CSS) en la página de gestión del menú de WeChat.
- Corregido que la página de gestión de tareas de importación/exportación siempre regresaba a la primera página al actualizarse automáticamente.
- Corregido que las salas de conferencia no filtraban por permisos, permitiendo que distintos equipos vieran los registros de otros.
- Corregido que al eliminar un cliente en gestión de clientes de campañas no se registraba en el log.

## AsterCC 2.2-rc4

**Nuevas funciones**

- Nueva interfaz para llamar a dos números que no son dispositivos del sistema.

**Corrección de errores**

- Actualización del driver DAHDI en la ISO.
- Corregido que el tiempo de espera de timbrado del agente siempre era de 15 segundos.
- Corregido que la llamada se colgaba si el agente presionaba `#` durante la llamada.
- Corregido que la música de espera en grupos de timbrado no se podía cambiar.
- Corregido que el marcador predictivo no respetaba la opción de reintento.
- Corregido que no se creaba la tabla relacionada al crear una campaña con tabla general.
- Corregido que el registro de llamadas (CDR) no respetaba el alcance de permisos del usuario.
- Corregido que IVR no respetaba la opción de dispositivo.
- Corregido que la página de conferencias mostraba las conferencias de todos los equipos.
- Se ocultó la contraseña en la página de configuración de SMS.

## AsterCC 2.2-beta

**Funciones de llamadas**

- Los agentes en modo dispositivo ya pueden usar buzón de voz.
- El agente puede transferir llamadas con el botón del teléfono IP.
- Nueva interfaz HTTP en IVR (además de webservice).

**Funciones centrales**

- El monitoreo en tiempo real agrega datos de clientes en espera, tiempo máximo de espera y nivel de servicio.
- La página de monitoreo en tiempo real permite mostrar todos los agentes, incluidos los que no han iniciado sesión.
- Se admite un mayor volumen de datos al importar.
- Al subir un anuncio de voz, se pueden subir archivos en distintos códecs.
- Se permite personalizar las columnas y el orden de exportación (por ejemplo, en detalle de agentes y exportación de clientes).
- Se permiten reglas para troncales y grupos de troncales, como quitar el 0 en números locales o elegir troncal según los atributos del número destino.
- El administrador puede combinar anuncios desde la interfaz gráfica, permitiendo crear IVR multilenguaje usando TTS.
- Se agregó el nombre de cuenta en el reporte estadístico de llamadas salientes.
- Se puede ocultar el historial de contacto en el panel de llamadas del agente.
- El envío masivo de mensajes permite seleccionar el objeto destinatario mediante etiquetas.
- El envío masivo de mensajes permite seleccionar por paquete de clientes y estado del cliente.
- Se puede buscar por ID de importación; se agregaron íconos de ayuda visual en algunas listas y avisos sobre tareas de importación pendientes o recién completadas.
- Se agregó búsqueda rápida de resultado de llamada en campañas.

**Atención al cliente**

- Nueva página predeterminada para atención al cliente, donde el agente puede consultar y buscar su propio historial de llamadas.

**Marcador y campañas**

- Opción para que el agente escuche la grabación de su llamada desde el popup de campaña.
- Opción para mostrar el atributo del número (área/procedencia) en el popup de campaña.
- Se permite usar texto simple como guion de llamada.
- El "recordatorio rápido" (quick scheduler) admite valor vacío para indicar "sin cita".
- Se agregó un enlace directo a importación desde la lista de campañas.

**Marcador predictivo**

- La estrategia "por agente 100%" ahora es la predeterminada.

**WeChat**

- Se agregó la función de diseñar el menú de WeChat.

**Corrección de errores**

- Corregido que algunos campos personalizados no se mostraban en la orden de trabajo.
- Corregido que, con varios servidores SMS, la acción de colgar no seleccionaba el servidor correcto.
- Corregido que la creación automática de colas podía generar números de cola duplicados.
- Corregido que, con muchos campos de cliente, no se podía ajustar el orden de visualización en Chrome.
- Corregido que la configuración rápida podía crear una extensión de un solo dígito cuando el rango comenzaba en 0.

## AsterCC 2.2-alpha

**Núcleo (core-2.2-alpha)**

- Optimización de estilos CSS del sistema.
- Las listas ahora muestran 30 registros por defecto.
- Ajustes de traducción en varias páginas.
- Equipos: nuevo parámetro `Followme Accept` (aviso de aceptación de seguimiento de llamada).
- Dispositivos: nuevo parámetro `FollowMe`.
- Monitoreo en vivo: nuevo ícono junto al número de agente para iniciar sesión como ese agente.
- Tareas por lotes (Shell Jobs): actualización automática cada 5 segundos.
- Exportación de tareas: actualización automática cada 5 segundos.
- Plantillas: los valores por defecto de "Elección del agente" y "Modificar" cambian a "sí"; el administrador puede usar `##nombre_campo##` en la plantilla, que se sustituye por el dato del cliente al enviar el mensaje.
- Troncales: al usar DAHDI ya no se pide seleccionar plantilla.
- Importación: el parámetro "Restablecer agente" ya no requiere habilitar el marcador para la campaña.
- Buzón de voz: se puede acceder directamente marcando `*` + extensión; se puede entrar al buzón durante el mensaje de bienvenida presionando asterisco, y se puede acceder a la operadora del equipo presionando cero.

**Marcador y campañas**

- El administrador puede definir un número de marcado rápido: el agente lo marca para obtener un cliente de su lista, y al finalizar puede usar IVR para guardar el resultado de la llamada.
- El valor por defecto de "Cargar historial de contacto" cambia a "sí".
- El "recordatorio rápido" admite configurar minutos.
- Nuevo parámetro "Campos ocultos", usado junto con "Ocultar información de contacto".
- Resultados: el parámetro "Equipo" cambia su valor por defecto de "Predeterminado" a "Todos".
- Panel de agente: cuando no hay más números para marcar en modo automático, el sistema revisa cada minuto si hay nuevos números disponibles; se usa el primer campo mostrado como título de la pestaña; se agrega un número de prefijo para acelerar la selección del resultado de llamada.

**Oficina virtual / BPO**

- Cuenta BPO: nueva opción "Iniciar sesión como usuario BPO"; el rol pasa a ser obligatorio; se permite subir una imagen de perfil para la página personal de gestión BPO; se pueden configurar los campos visibles por campaña asociada a la cuenta.
- Página de clientes BPO: se muestra según los campos configurados en la cuenta BPO; se agregaron estadísticas de estado de clientes por campaña.

**Órdenes de trabajo**

- Se agregó un botón de actualización en la página de detalle de la orden de trabajo.

**Interfaz de trabajo del agente**

- Popup de cliente de campaña: se unificó el estilo de los mensajes de aviso; se agregó inicio de sesión automático en la cola; el ranking de agentes solo se puede consultar una vez por minuto; se agregó numeración para ordenar los resultados de llamada en el desplegable del popup de cliente.

## AsterCC 2.1

**Núcleo (core-2.1)**

- Optimización de estilos CSS del sistema.
- Si solo existe un equipo, se selecciona automáticamente por defecto.
- Corregida la imposibilidad de restaurar la vista de columnas en algunas páginas tras eliminarlas todas del título.
- La paginación se muestra flotante cuando el contenido supera la altura visible del navegador.
- Mejora de etiquetas de cliente: se pueden ingresar manualmente con autocompletado, o elegir desde una lista de etiquetas en el popup.
- Al vincular un DID a un dispositivo, si el dispositivo no está disponible, ya no se redirige a la ruta de entrada.
- Todas las extensiones ahora pueden usarse para grabación.
- Equipos: nuevos parámetros "Facturación de agente externo", "Tipo de troncal de agente externo" y "Troncal de agente externo".
- Troncales: nuevo parámetro de ganancia para aumentar el volumen al combinar grabaciones.
- Importación: optimización de estilos; auto-coincidencia de campos según el título del archivo importado; importación a lista blanca; nueva función "Importar y ejecutar" (ver documentación del módulo de importación).
- Monitoreo en vivo: los contadores de "Registrado", "Libre", "Timbrando", "En llamada", "Pausa" y "ACW" del equipo ahora se basan en el resumen real de agentes del equipo.
- IVR: eliminación automática de espacios finales.
- Llamadas salientes: se puede elegir estadística de todos los agentes.
- TTS en chino.
- Detalle de agentes: se agregó estadística total; estadística por cuenta; las cuentas con permiso de grupo de agentes solo ven la estadística de su propio grupo.

**Marcador y campañas**

- Nuevo parámetro "Orden de nueva pestaña" en "Avanzado", para controlar el orden de los datos bajo "Nuevo".
- Nuevo parámetro "Recordatorio rápido" en "Avanzado", para elegir rápidamente la hora de cita de un cliente pendiente.
- Nuevo parámetro "Colgar al enviar".
- Nuevo parámetro "Eliminar recordatorio al enviar".
- Corregido que no se podía asignar clientes por "estado" cuando la campaña usaba tabla general.
- Los parámetros "Verificar reasignación" y "Aviso de llamada" se movieron a "Avanzado".
- Mejora de la prioridad del marcado automático.
- Se permite mostrar toda la información del cliente en la ventana de asignación manual.
- Se agregó el porcentaje de resultados de llamada en la estadística de campañas.
- El panel de agente permite buscar en 5 campos de campaña personalizados.

**BPO**

- La lista lateral no muestra campañas deshabilitadas al iniciar sesión con cuenta BPO.
- Corregido que no se veían los datos en la página de registro de llamadas (CDR) tras iniciar sesión con cuenta BPO.
- Cuenta BPO: en la página de agregar/editar, ya no se pueden elegir campañas deshabilitadas.

**Interfaz de trabajo del agente**

- Popup de cliente de campaña: corregido que no se podía marcar automáticamente cuando "Ocultar información de contacto" estaba activado; al hacer clic en marcar desde el popup se finaliza el estado ACW (o pausa) del agente; el panel de marcado automático se muestra siempre, sin necesidad de elegir el modo de marcado; los clientes "pendientes" se ordenan por hora de cita programada; se puede buscar con la tecla Enter; se agregaron campos de búsqueda dinámicos según los primeros cuatro campos frontales configurados en la campaña (sin contar los campos fijos).

**Interfaces (API)**

- Nueva API de marcado por extensión.
- Nueva API de transferencia de agente a IVR.
- Inicio de sesión: se permite pasar el número de extensión como identificador de extensión para iniciar sesión en la cola.

## AsterCC 2.0

**Núcleo (core-2.0)**

- Actualización de la ISO a CentOS 6.5.
- Compatibilidad con PHP 5.4.
- Ajustes de traducción y optimización de estilos CSS.
- Mejora del selector de hora: además del selector gráfico, se puede ingresar manualmente.
- Se agregó la tecla `ESC` para cerrar rápidamente ventanas emergentes.
- Aviso de voz cuando el cliente solicita una nueva visita.
- Mejora de la función `*97`: ahora requiere ingresar contraseña.
- Mejoras en la interfaz y en las validaciones del sistema.
- Los idiomas listados en el sistema ahora solo muestran los habilitados.
- El sistema ahora gestiona dependencias entre módulos.
- Cada cuenta puede configurar su preferencia de idioma.
- El administrador puede iniciar sesión como otra cuenta.
- Optimización de la página de configuración de exportación, con casilla para controlar el envío de correo.
- Páginas nuevas: Monitoreo en tiempo real, Estado de agentes (en información en tiempo real) y Estadística de DID (en reportes).
- Monitoreo en tiempo real: permite ver llamadas entrantes y salientes por equipo.
- Estado de agentes: muestra el estado de trabajo del equipo, incluyendo total, con sesión iniciada, registrado, libre, timbrando, en pausa, ACW y en llamada.
- Equipos: en la página de edición se agregaron los botones "Recargar" (abre la gestión financiera del usuario para ese equipo) y "Exportar datos de PBX" (genera una tarea de exportación en segundo plano); se agregó el botón "Importar datos de PBX del equipo"; al crear un equipo se genera automáticamente un servidor de correo tipo "localhost".
- Cuentas: nuevo parámetro "Idioma predeterminado", aplicado a los mensajes de voz.
- Estado de cuenta (financiero): nuevo parámetro "Forma de pago" (tarjeta de crédito, PayPal, transferencia, efectivo, otro; por defecto "otro"); nuevo campo "Número de transacción".
- Plantillas: nuevo parámetro "Responder a"; el contenido admite `##NombreDeCampo##` como variable de reemplazo con los datos del cliente.
- Grupos de DID: nuevos parámetros "Tarifa mensual" y "Tarifa inicial" (costo por minuto, puede ser negativo, por defecto 0.0000).
- DID: soporte de facturación; se agregaron "Tipo de tarifa inicial", "Tarifa inicial", "Tarifa mensual" y "Costo"; se agregó "Proveedor" y "País" (opcional).
- Estadística de DID: permite ver el detalle por DID, incluyendo llamadas entrantes, llamadas contestadas, duración, duración facturable y crédito.
- Música de espera: se puede editar la música de espera predeterminada del sistema.
- Importación: soporte para importar datos de DID desde archivo.
- Servidor de correo: se ocultan parámetros innecesarios al elegir tipo "localhost"; si "Predeterminado" es "sí", el modo solo puede ser "Daemon".
- Personalización: el tipo de idioma solo permite los idiomas habilitados en el sistema.
- Configuración: nuevo parámetro "Mostrar menú de depuración del agente" para controlar la visibilidad del botón de menú en el panel de agente.

**Marcador predictivo**

- Al desinstalar el módulo de marcador predictivo, se oculta la pestaña de marcador predictivo en la creación/edición de campañas, así como el selector de configuración de marcado predictivo y el parámetro "Importar a la lista de marcado si está duplicado" en la página de importación.

**E-commerce**

- Productos: el parámetro "En el mercado" tiene valor por defecto "sí".

**Marcador y campañas**

- Nuevo parámetro "AllowManualPopCustomer" en "Avanzado" (por defecto "sí"): permite que el agente ingrese un número para mostrar el popup del cliente asociado; si no existe, se muestra un aviso; si no se ingresa número, se comporta como el marcado automático mostrando el cliente de mayor prioridad.
- Nueva opción "Prohibido" para el parámetro "Cargar historial de contacto": oculta la sección de detalle de historial.
- Nuevo parámetro "Eliminar recordatorio al enviar", para controlar si se borra la hora de reintento al guardar el estado del cliente como cerrado con éxito o cerrado con error.
- La página de asignación muestra los campos teléfono 1 y teléfono 2 en la lista.
- Lista de no llamar (DNC): si el desplegable tiene una sola opción, se marca automáticamente.
- Resultados: si la cuenta tiene permiso de equipo, puede ver los resultados de sistema, pero no editarlos.
- Monitores de datos: corregido un error que mostraba "null" en lugar de los datos correctos.
- Se agregó el recordatorio rápido (quick scheduler).

**Interfaz de trabajo del agente**

- Optimización de estilos CSS.
- Si el parámetro "Dispositivo" del agente es dinámico, ya no se valida la coincidencia entre la IP del teléfono y la IP de inicio de sesión, solo si el dispositivo está habilitado.
- Ante llamadas anómalas en el panel del agente, se puede hacer clic en el botón de colgar de la página de estado para finalizar el procesamiento de datos con error.
- Nueva combinación de teclas `Ctrl+Z` para iniciar sesión rápidamente y abrir la interfaz de marcado saliente: selecciona automáticamente el primer grupo de agentes, la primera campaña (u oficina virtual) disponible, enfoca el campo de número y permite marcar con la tecla Enter.
- Popup de cliente de campaña: muestra el ID del cliente cuando el registro ya existe; mejora del marcado automático (prioriza clientes pendientes cuya hora de reintento ya pasó, y luego clientes nuevos con menos intentos automáticos); al enviar SMS desde el popup, se reemplazan automáticamente las variables de plantilla con los datos del cliente (se elimina el reemplazo manual al usar plantilla); los campos con solo permiso de vista no pueden editarse; se permite guardar el cliente con múltiples avisos.
- Popup de cliente de atención al cliente: muestra el ID del cliente cuando el registro ya existe.

## AsterCC 2.0-beta

**Núcleo (core-2.0_beta)**

- Ajustes de traducción y optimización de estilos CSS.
- Nuevos mensajes informativos al marcar.
- Se reproduce un anuncio predeterminado cuando no hay ruta de entrada coincidente ni ruta por defecto.
- La duración en los reportes estadísticos ahora respeta el formato de hora configurado en el sistema.
- Se renombró "Importaciones" a "Tareas por lotes" (Shell Jobs) dentro de administración avanzada del call center.
- Se renombró "Calificación" (Rate) a "Registro de calificación" y se trasladó a la sección de estadísticas.
- Nueva interfaz para importación.
- Nueva función de solicitud de devolución de llamada (callback).
- Nueva función de "tarea de eliminación" (shell delete): al eliminar datos se puede elegir eliminación directa o mediante tarea, disponible en: Campañas -> Clientes; Marcador predictivo -> página de recuperación; Marcador predictivo -> listas de marcado de campaña; Clientes -> Individuos; Clientes -> Organizaciones.
- Equipos: corregido que al eliminar un equipo no se eliminaban los grupos de agentes relacionados.
- Agentes: nuevo botón "Iniciar sesión como este agente" en la página de edición.
- Grupos de agentes: nuevo parámetro "Encabezado SIP de respuesta automática", que controla colas, marcador predictivo y "clic para llamar" de forma independiente (cola por defecto "no", marcador predictivo por defecto "no", clic para llamar por defecto "sí"; el teléfono debe soportar respuesta automática); se movió "Abrir ventana de entrada" a la pestaña avanzada, renombrado a "Abrir pestaña de oficina virtual".
- Troncales: aviso informativo cuando "Forzar uso de tarifa" está activado; nuevo "Estado de colgado" que muestra las últimas 10 desconexiones; nuevo parámetro "Máximo de no disponibilidad", que deshabilita el troncal tras cierto número de errores (relacionado con "Duración de error de troncal").
- Dispositivos: la opción "Marcar todo" cambia a "Todos" y "Solo interno".
- Sonidos: mejora de los mensajes de error.
- Rutas de entrada: la opción "Coincidencia de CID" cambia a "Ninguna", "Completa", "Prefijo" y "Área/procedencia".
- Configuración: nuevo parámetro "Auto-agregar DID", que crea automáticamente un DID cuando el número entrante no coincide con ninguno existente; nuevo parámetro "Duración de error de troncal" (relacionado con "Máximo de no disponibilidad" del troncal); nuevo parámetro `rtptimeout` en la configuración general SIP (valor por defecto 120); nueva función para editar la zona horaria del sistema.
- Códigos de función: nuevo código `*73` para reproducir/devolver la llamada al último número contactado.
- Configuración rápida: los prefijos de usuario y contraseña dejan de ser obligatorios, con avisos informativos.
- Importación: optimización de estilos; nuevos parámetros de importación; nuevo parámetro "Restablecer estado de cliente" (solo disponible al importar a un paquete de clientes con campaña asociada, marcado por defecto); si el sistema tiene un solo equipo o el usuario pertenece a uno, se selecciona automáticamente.
- Tareas por lotes: la página se dividió en dos secciones, arriba las tareas de importación y abajo las tareas de eliminación.
- Planes de respaldo: se agregó el parámetro de dirección de base de datos, para poder respaldar la base de datos cuando esta no está en el mismo servidor que el núcleo (usar `127.0.0.1` si están en el mismo servidor, o la IP del servidor de base de datos si están separados).

**Marcador y campañas**

- Nuevo parámetro "Actualizar estado de cliente", que controla el permiso de edición de datos del cliente: "Agente asignado" (solo el agente propietario puede editar) o "Cualquier agente".
- Nuevo parámetro "Llamada prioritaria" (opciones: desactivado, agente actual, último agente de contacto): al recibir una llamada entrante, prioriza al agente correspondiente según la configuración; si no hay agente disponible, la llamada va a la cola (requiere que la campaña use la tabla general de clientes).
- En la lista de campañas, las que usan la tabla general de clientes se muestran en color rojo.
- Nuevo botón "Agregar evento de colgado" en la edición de campaña, para enviar correo o SMS automáticamente tras colgar según el evento: "Agente no contestó", "Abierto", "Pendiente", "Cerrado con éxito" o "Cerrado con error" (estos últimos cuatro solo aplican durante la llamada o inmediatamente después de colgar).
- Estadísticas: nuevos reportes "Reporte de llamadas" y "Reporte de contacto", visibles solo si se elige "Cliente de tabla general".
- Llamadas perdidas: las que solicitan devolución de llamada se muestran en color azul.

**Oficina virtual**

- Clientes: nuevo botón "Gestión de contactos frecuentes" en la edición, para agregar contactos habituales del cliente.

**Atención al cliente**

- Nuevo parámetro "Llamada prioritaria" (desactivado, agente actual, último agente de contacto), igual que en campañas.
- Nuevo botón "Agregar evento de colgado": "Agente no contestó" y "Agente contestó", cada uno con envío de correo/SMS configurable.

**E-commerce**

- Nuevo parámetro "Origen", personalizable con múltiples valores separados por coma; el agente puede usarlo como origen del pedido.
- Productos: al crear o editar, se pueden asociar uno o más productos relacionados, visibles para el agente al armar un pedido.

**Interfaz de trabajo del agente**

- En el popup de cliente se combinaron los paneles "Historial de contacto" y "Compras recientes" en uno solo, mostrando por defecto el historial.
- En "Compras recientes" se puede abrir el detalle de un pedido desde su número; si el pedido no ha sido despachado, se puede cancelar con confirmación previa.
- Popup de cliente de campaña y de atención al cliente: se agregó la vista de cancelación de pedido descrita arriba.

## AsterCC 1.2

**Core**

- Se agrega la interfaz del marcador (dialer) y una plantilla de troncal IAX.
- Nuevo módulo de comercio electrónico (E-Commerce).
- Control de privilegios por rango para equipos, grupos de agentes e individuos.
- Pausa automática cuando una llamada no es contestada.
- Nueva página de registro de contactos para ver el historial de contacto de cada equipo.
- Nueva página para controlar los privilegios de campos de la tabla maestra (individuos u organizaciones) por equipo.
- Mejoras en la codificación de errores del sistema.
- En la barra de búsqueda: se agrega el operador `!=` y la opción `Otros` para búsquedas de tipo selección.
- Los módulos del sistema ahora se pueden desinstalar.
- El sistema permite la existencia de un solo equipo (team); si solo hay un equipo, el selector de equipo no muestra la opción "seleccionar".
- Se corrige la incompatibilidad del plugin de horario con Chrome.
- Aviso en la página de mensajes del sistema cuando vence la licencia de un módulo.
- Se pueden agregar varios correos en copia (CC) separados por punto y coma.
- Correcciones en varias traducciones (po).

**Agente**

- Nuevos parámetros `CIDNum` y `CIDName` para mostrar el nombre y número que llama al marcar; si están configurados, se usan salvo que la campaña fuerce su propio identificador de llamada.

**Grupo de agentes**

- En la selección de agentes se agregan los modos `detallado` y `simple` para controlar cómo se listan los agentes.
- La lista de agentes no asignados se divide en dos paneles: agentes sin ningún grupo y agentes fuera del grupo actual.
- El selector de equipo ahora filtra la búsqueda según el equipo elegido.

**Roles**

- Los roles de tipo agente pueden configurar el privilegio de la página de búsqueda de clientes del módulo de atención al cliente.

**Edición rápida**

- Se corrige un error de parámetros que no mostraba el aviso correspondiente.
- Se corrige que, al editar un dispositivo de tipo distinto a mgcp o dahdi, no se actualizaba el campo `Username`.

**Dispositivos**

- Se ocultan los parámetros relacionados con el buzón de voz cuando este está deshabilitado.
- El campo `Connect Status` cambia de posición; si el estado es "reachable" se muestra en verde con los milisegundos de conexión, y en negro para otros valores.
- Se optimiza la actualización del valor de `Username` al modificar el número de extensión.

**Grupos de timbrado (Ringgroups)**

- Se corrige que no timbraban cuando había un anuncio configurado y la estrategia de timbrado era "Hunt" o "Hunt-next".
- Se corrige que un IVR dirigido a un grupo de agentes sin anuncio no podía usar estrategia "Hunt" o "Hunt-next".

**Troncal**

- En Avanzado: se agrega el parámetro `Custom Dial String` y se eliminan `CIDNum AddPrefix`, `CIDNum RemovePrefix` y `CIDName AddPrefix`.
- En la edición de reglas se agrega la opción `Callerid Name` para el parámetro `Object`.
- El estado de registro (`reg. status`/`peer status`) se reubica a la izquierda; si es "reachable" se muestra en verde junto con los milisegundos.

**Importación**

- Se agrega manejo de datos duplicados mediante los parámetros `Customer Duplicate` (modos `skip`/`update`) y `Duplicate Customer Import Diallist` (modos `Ignore Duplicate`, `All`, `Ignore Success`) para controlar cómo se insertan clientes duplicados en la lista de marcación al importar.

**Lotes de contactos (Batchcontacts)**

- Se agrega el campo de búsqueda `Archivetype`.

**Monitor en vivo**

- Se corrige que el conteo de check-in por equipo mostraba "NaN".
- El administrador de grupo de agentes puede monitorear agentes con una nueva función.

**Servidor de correo (antes SMTP Servers)**

- Se renombra a "Mail Server". Se agrega un servidor de correo local por defecto al instalar o actualizar el sistema si no existe ninguno, permitiendo enviar correo mediante ese servidor local.

**Configuración**

- El parámetro `Current PbxCdr Table Data` cambia su unidad de meses a días.
- Se agrega el parámetro `srvlookup` en `GENERAL SIP SETTINGS`.

**Personalización (Customization)**

- Para campos de tipo "relacionado" ahora se puede llenar las opciones por texto libre o subiendo un archivo .txt.
- Aviso al usuario si ya existen paquetes de clientes al agregar un campo.
- Se corrige un error que mostraba campos duplicados al usar mayúsculas en el nombre del campo.

**Clientes individuales y Organizaciones**

- Nuevas funciones: elegir etiquetas (tags), eliminación por lotes, asignación por selección (`Assign By Check`) y asignación por condiciones de búsqueda (`Assign By Conditions`) hacia paquetes de clientes.
- En la asignación se agregan dos casillas: `Keep Agent` (conserva al agente asignado si pertenece al grupo de agentes de la campaña del nuevo paquete) y `Keep Status` (conserva el estado del cliente); además se guarda un registro (log) de cada asignación.
- Se puede asignar el cliente a un paquete directamente al crearlo, y buscar por lista de etiquetas o de paquetes de clientes.

**Registro de contactos (Contact Log)**

- Página nueva que muestra el historial de contacto por equipo.

**Campo de cliente (Customer Field)**

- Página nueva para configurar el privilegio de campos de clientes individuales u organizaciones por equipo.

**Módulo de Work Order (workorder-1.1)**

- Se agrega registro de contacto para las órdenes de trabajo.
- Solo el propietario de la orden o quien la creó puede cambiar su estado.
- Nuevo parámetro `Edit Limit` (`everyone`/`owner`) que controla quién puede editar la orden de trabajo.
- Se agregan los campos `Customer Name` y `Contact Memo`.

**Marcador / Dialer (dialer-1.4)**

- Las páginas relacionadas con el marcador ahora se controlan por rol.
- En la lista de marcación de campaña se agrega el campo `memo`, que guarda la condición SQL usada por el filtro.
- Se optimiza la página de configuración del marcador.

**Campaña (campaign-1.4)**

- Los resultados de llamada pueden vincularse con una orden de trabajo si el módulo está instalado; se agrega ventana emergente al consultar (pop en consulta).
- Las campañas sin grupo de agentes se muestran con fondo gris en la lista.
- En Avanzado se agrega `blacklist direct` (`Team`/`Current Campaign`) para controlar el alcance de la lista negra (DNC).
- Al crear una campaña se puede elegir crear un nuevo paquete de clientes, usar la tabla maestra de individuos/organizaciones, o reutilizar un paquete existente (mostrando si usa la tabla maestra).
- Se puede ordenar y marcar como requeridos los campos mostrados al agente o al back office; se agrega el indicador `Use Main Table`.
- En "Asignación manual de clientes" el campo de búsqueda respeta la configuración de campos del back office.
- Un paquete que usa la tabla maestra comparte los mismos clientes que dicha tabla, y un cliente de tabla maestra solo puede pertenecer a un paquete a la vez; se agrega el botón `Select from main database` para agregar clientes desde la tabla maestra.
- En Clientes: se corrige que la lista no se refrescaba tras un borrado por condiciones; se agrega el campo `CallPath` (también visible y buscable en CDRs).
- En Resultados: se agrega vínculo con la orden de trabajo y un resultado `DNC` que envía automáticamente el número del cliente a la lista de no llamar.
- En Control de calidad: se corrige una anomalía al escuchar grabaciones históricas.
- En la lista DNC: se reduce de tres campos de entrada a uno, se agrega función de vaciado (truncate) y de alta de números, y se optimiza la interfaz.

**Atención al cliente (customerservice-1.1)**

- Nuevo parámetro `Add Customer Priority` (`Only Individual`, `Individual Priority`, `Only Organization`, `Organization Priority`).
- Nuevo botón para configurar los campos de búsqueda de clientes individuales/organizaciones, con modos `Disabled Search`, `Partial Matched` y `All Matched`.
- En CDR: clic en `Src`/`Dst` para marcar desde el portal del agente; las llamadas entrantes no contestadas se resaltan en rojo y las salientes no contestadas en verde oscuro.
- En Llamadas perdidas: los registros sin seguimiento se resaltan en rojo.

**Plataforma de trabajo del agente**

- El parámetro `Device` del agente pasa a autodetección (`Self-adapting`).
- Si el agente usa softphone y este se desconecta, se hace check-out automático de la cola.

**Pantalla emergente de campaña (Campaign Pop Page)**

- En modo Preview/Automático, si el primer número no contesta se marca el siguiente automáticamente; el número marcado se resalta en rojo.
- Se puede asignar el resultado DNC directamente desde la pantalla emergente del cliente.
- Se permite fusionar dos clientes (A y B): B queda combinado con A y no puede editarse ni eliminarse por separado.

**Pantalla emergente de atención al cliente**

- Nueva página de búsqueda de clientes.
- Nueva pantalla emergente de cliente nuevo, controlada por el parámetro `Add Customer Priority`: según la prioridad configurada se puede cambiar entre ficha de individuo y de organización.

## AsterCC 1.2.2

**Core**

- Se agrega el tipo de campo "link" en la personalización de campos.
- Se corrige que un memo con saltos de línea impedía abrir la página de control de calidad (qcpage).
- En los gráficos estadísticos, la unidad de "Hora" cambia a formato "hh:mm:ss".
- Se mejoran los mensajes de error del sistema.
- Se agrega un aviso en amarillo (arriba a la derecha) que muestra usuario, rol y hora local.
- Nuevo calendario del cliente en la tabla maestra: al reasignar un cliente, su calendario se reasigna también al nuevo agente.
- Se agrega el privilegio de rol "Mis órdenes de trabajo" para que el agente vea solo sus propias órdenes.
- Al consultar o transferir una llamada, al agente consultado/receptor se le muestra automáticamente la ficha del cliente, con botón de actualización inmediata.
- Se corrige que un dispositivo externo no podía transferir a una extensión.
- Se agrega soporte de BLF en los teléfonos.
- Se corrige la exportación de archivos que no incluía los campos correctamente.
- Se corrige el estilo (CSS) incorrecto del cuadro de búsqueda.
- Al exportar, ahora se puede indicar un correo destino para recibir el archivo exportado; aplica a: PBX → CDRs, Campaña → exportar clientes desde edición de paquete, Campaña → Clientes, Campaña → CDRs, Campaña → Control de calidad, Marcador → listas de marcación, Atención al cliente → CDR, Atención al cliente → Llamadas perdidas, y Encuestas → exportación de cuotas.
- Cuentas: aparece barra de desplazamiento en las páginas de lista negra/blanca cuando hay muchos datos.
- Agentes: desde "Ver grupo de agentes" se puede quitar al agente del grupo.
- Grupo de agentes: al editar el campo ACW aparece el aviso de reiniciar sesión.
- Personalización: los saltos de línea se unifican al estándar unix; el campo `Display As` ahora es editable.
- Troncal: al editar `Registry String` aparece el aviso de recarga.
- Rutas salientes: se agrega la opción `Sip Refer` en el campo `Transfer` de la regla.
- IVR: se corrige que se podían guardar datos vacíos.
- Base de conocimiento: se revisan traducciones y se optimiza el CSS.
- Dispositivo: el campo `ExternalNumber` no puede coincidir con `Ext. No.`.
- Configuración: se agregan los parámetros SIP TCP (`tcpenable`, `tcpbindaddr`, `transport`) en `GENERAL SIP SETTINGS`.
- Respaldo de archivos: se optimiza el CSS de la paginación.
- Troncal en vivo: se corrige que no se mostraban troncales sin equipo asignado.
- Grupo BLF: los dispositivos pueden unirse a un grupo BLF para ver en el teléfono el estado de las demás extensiones del grupo.

**Página de inicio de sesión**

- Se corrige que no se podía entrar al sistema presionando Enter tras llenar el correo.
- El acceso ahora admite identificar el equipo por URL, de dos formas: `http://IP_SERVIDOR/identificadorDeEquipo` o mediante dominio propio (`http://www.identificador.xxx` o `http://identificador.xxx`); con este método ya no se muestra el selector de equipo, útil para operaciones multi-equipo. Para activarlo se agrega `login_route = team` bajo `[system]` en `/etc/astercc.conf` (quitando el `;` si ya existía comentado).

**Campaña**

- Las campañas que usan la tabla maestra de clientes ya pueden trabajar con el marcador (dialer).

**Marcador**

- Al reciclar clientes, se usa el valor del campo `Schedule` del cliente como horario de re-marcado, en dos casos: cuando el cliente reciclado tiene `Schedule` propio posterior al del reciclado, o cuando la operación de reciclado no define `Schedule` y el cliente sí lo tiene.
- Nueva opción para controlar si se vacía el número de agente (`agentno`) del cliente al reciclar.
- En la lista de marcación de campaña se deshabilita la edición del cliente en la vista "Campaign Customer".

**Plataforma de trabajo del agente**

- Se agrega la columna `status` en la lista de pedidos al ver el historial de compras.
- Aparece barra de desplazamiento cuando la cola es demasiado larga para la pantalla.
- Se corrige que no se obtenían los datos de clientes pendientes bajo la pestaña `Pending` en la pantalla de trabajo de campaña.

## AsterCC 1.2.1

**Core**

- Se agrega control del modo de aviso en la pantalla de trabajo del agente: ventana emergente o parpadeo.
- Al consultar a un agente, se muestra la ficha del cliente en la pantalla emergente del agente consultado.
- Correcciones de traducción.
- Se optimiza la consulta SQL de reciclado de clientes, ordenando por fecha de marcado e ID ascendente.
- Se corrige que no se actualizaba el correo del administrador al iniciar sesión.
- Equipo: se corrige que no se validaba la duplicidad del identificador al editar; se corrige que no se podía actualizar el número máximo de agentes al valor real ya existente en el equipo.
- Agente: se corrige que no se guardaba el rol al agregar un agente.
- Monitor en vivo: el estado del agente ahora es consistente entre distintos grupos de agentes; se corrige que no funcionaban las funciones "Call Barge", "Call Spy" y "Whisper".
- Códigos de función: se agrega `*54` para consultar a un agente; `*55` queda reservado para consultar un número telefónico.

**Campaña (campaign-1.5)**

- Se corrige que el número de agente (agentno) no aparecía en la búsqueda de la página de asignación manual.

**Atención al cliente (customerservice-1.2)**

- Se corrige que el campo de agente podía quedar nulo.

## AsterCC 1.2-beta

**Core**

- Se actualiza Google Maps a la versión 3.
- Se agrega el módulo de órdenes de trabajo (Work Order), integrado con el módulo de atención al cliente.
- Se agrega el módulo de Base de Conocimiento (Knowledge).
- Se agrega la función de identificación de área telefónica (número de origen), disponible en la administración avanzada del call center.
- El modo de agente en los dispositivos queda habilitado por defecto.
- Los nombres de horario laboral (worktime) y paquete de horario admiten espacios en blanco.
- Al crear un plan de importación o exportación, la hora de ejecución por defecto es la hora actual.
- Se corrige que el sistema mostraba el módulo de marcador aunque no estuviera instalado.
- Los campos personalizados de "clientes individuales salientes" y "clientes empresariales salientes" se trasladan al módulo de gestión de clientes, agregando además búsqueda por campo personalizado.
- Se corrige un error de un solo dígito en el número de agente.
- Se corrige el título incorrecto del reporte de estadísticas de llamadas entrantes al exportar.
- El "enlace de nombre de identificador de llamada" se renombra a "vinculación de aplicaciones entrantes" (App Binding).
- Cuando una página de selección no tiene opciones no consulta la base de datos, y si solo tiene una opción la selecciona automáticamente; aplica a clientes individuales/empresariales salientes, Oficina Virtual → Clientes y CDR, Campaña → CDRs y Clientes, y Marcador → lista de marcación.
- Correcciones de traducción y de CSS.
- Exportación: se agrega empaquetado en sub-archivos cuando el volumen de datos es grande, comprimiendo cada N registros y empaquetando todo en un único archivo descargable.
- Mensajería interna: al elegir remitente se combina el número de agente con la cuenta (ej. astercc0(5000)); se agrega búsqueda por número de agente.
- Se agrega descarga automática del paquete de actualización.
- Se corrige que no se registraba el número de agente al enviar SMS o correo desde la plataforma del agente.
- Si el parámetro `Device` del agente está en autodetección y no se ingresa número, el sistema intenta conectar primero al teléfono con la misma IP; si falla, solicita ingresar la extensión.
- Los resultados de llamada se listan por fecha de actualización descendente, para controlar cuál queda seleccionado por defecto.
- Se optimiza el reproductor de grabaciones en línea, alargando la barra de progreso para facilitar el avance rápido en llamadas largas.
- Correcciones en varios plugins JS.
- Equipo: los equipos sin troncal o grupo de troncal asignado se muestran en amarillo en la lista; al editar por doble clic se ofrece asignar foco al campo de troncal; al crear un equipo se selecciona por defecto una troncal global disponible; en el alta de equipo, los máximos de cuentas/agentes/dispositivos/colas/salas de conferencia son 5 por defecto, y el idioma se preselecciona según el idioma del sistema.
- Cuenta: nombre y apellido dejan de ser obligatorios; se agrega visualización y búsqueda de `accountcode`.
- Grupos de cuenta: al eliminar un grupo se vacían el ID de grupo y el indicador de administrador en las cuentas asociadas.
- Edición rápida: se corrige el guardado por lotes del estado del agente.
- Grupos de agentes: los grupos sin cola asignada (o con cola eliminada) se muestran en rojo; el permiso de salida (`Outbound`) cambia a "sin restricción" por defecto; se corrige que al quitar un agente del grupo no se eliminaba su cola de check-in en Asterisk; se pueden editar en lote parámetros de los agentes ya seleccionados al crear/editar el grupo; el parámetro `Portal` inicia en `Default`; se agregan los parámetros `Current Application Type` y `Current Application`; la página de edición muestra la vinculación de aplicación entrante asociada; se gestiona automáticamente el campo `Current Agent Group` del agente al entrar, salir o eliminarse un grupo; si una aplicación se asocia al grupo sin tener aplicación de salida actual, se crea la vinculación automáticamente.
- Agente: en el alta, el desplegable de número destino se puede ocultar con un clic en cualquier parte de la página; si el dispositivo del agente tiene DND activo, se muestra en rojo junto al nombre; se agrega y permite editar el parámetro `Current Agent Group`; al hacer doble clic, si el grupo asociado ya no existe se actualiza automáticamente a otro grupo válido (o se limpia si no pertenece a ninguno); se muestra aviso al actualizar `Device`.
- Dispositivo: el "modo agente" queda habilitado por defecto.
- Cola: soporta anunciar periódicamente la posición en la cola, permitir teclas para pasar a IVR o buzón de voz durante la espera, reproducir un menú IVR antes de entrar a la cola (configurable según el número de personas en espera, incluyendo 0), reproducir un IVR cuando la cola no tiene agentes disponibles, anunciar la posición en la cola, y usar tono de timbre en lugar de música de espera en la música en espera.
- Extensión: se agrega función de verificación de extensiones que muestra los resultados de la comprobación.
- Listas negras: el campo `Account` deja de ser obligatorio.
- PBX → CDR: se modifican las opciones de búsqueda por disposición de llamada.
- Salas de conferencia (Meetmes): aviso si no se elige ninguna cuenta invitada; ajustes de traducción.
- Anuncios: los anuncios sin archivo de audio asignado se muestran en rojo en la lista.
- IVR: se corrige que no se podía seleccionar `Follow Action` en "Set IVR Dests"; `Max. Digits` es "No" por defecto y se ajusta automáticamente cuando el destino usa código de entrada por defecto; se optimiza el diseño de alta/edición.
- DID: se pueden dar de alta varios números DID usando un guion entre dos números; la edición muestra la aplicación entrante vinculada.
- Grupos de DID: la edición muestra la aplicación entrante vinculada.
- Troncal: al elegir protocolo dahdi (grupo de canal o canal único) se ocultan las plantillas y el detalle; la edición muestra la aplicación entrante vinculada; se elimina el `* *` sobrante del campo de detalle.
- Mensajes → Plantillas: se corrige un error al editar plantillas de tipo correo; se corrige la pérdida de sesión al subir imágenes desde Internet Explorer.
- Monitor en vivo: se puede filtrar por equipo o grupo de agentes; al pasar el mouse sobre una pausa "otro" se muestra el motivo completo; se optimiza el estilo; en la selección de grupo, el grupo con agentes conectados se resalta en rojo; se corrige la falta de sincronía entre los totales por equipo y por grupo de agentes.
- Importación: se agrega selector de equipo para elegir clientes individuales/empresariales salientes, paquetes de clientes y clientes de oficina virtual por equipo; se puede importar a la lista negra de campaña y a datos de área telefónica; al importar clientes se insertan también en la lista de marcación de la campaña correspondiente (si un cliente ya existe, se actualizan su prioridad y horario en la lista de marcación con los nuevos datos).
- Personalización: los campos nuevos de un paquete de clientes ya asociado a una campaña tienen privilegio de edición por defecto; el tipo de idioma coincide con el idioma del navegador.
- Sonidos: se optimiza el estilo de la página de subida de archivos.
- Paquete de horario laboral: se corrige que la edición no mostraba el mensaje completo.
- Horario laboral: los campos `Start` y `End` incorporan segundos.
- Vinculación de aplicaciones (App Binding): se elimina la aplicación por defecto del sistema; se agregan los parámetros `Agent Group` y `Trunk Match`.
- Trabajos de importación (Shell Import Jobs): se muestra la hora del servidor y el número de duplicados detectados.
- Códigos de función: se agregan tres atajos (`*69` modo normal, `*71` modo solo saliente, `*72` modo solo entrante) y el parámetro `parking_key` (por defecto 700) junto con diez extensiones de recuperación de aparcado (701-710 por defecto).
- Mensajes del sistema: se elimina la vista de uso de memoria.
- Configuración: el límite de exportación queda desactivado por defecto (límite de tiempo en 0); se agrega la opción "100" al límite de registros por página; se agrega el menú de configuración general de SIP; se agrega restricción de acceso por rango de IP.
- DAHDI: al crear o editar un DID se inserta automáticamente en la tabla de DID.

**Campaña (campaign-1.3)**

- Las campañas sin paquete de clientes se muestran en gris en la lista, con aviso en rojo al abrir la edición; si la cuenta de marcador (`Dialer Account`) vinculada fue eliminada, la campaña se muestra en rojo con foco automático en ese campo.
- Al guardar, los campos del cliente quedan con privilegio de edición.
- Al eliminar una campaña de la papelera se pone en inactiva la encuesta vinculada, se eliminan sus resultados y se eliminan sus cuotas de encuesta asociadas.
- Se agregan `dialer recoverdate` y `dialer recovercount`.
- El selector `Event URL` incluye la opción "por favor seleccione".
- Los clientes con menos llamadas realizadas se asignan primero (tanto en asignación automática como en asignación manual desde el portal del agente).
- Nuevo parámetro `Default Search Cdr`: si está activo, la pantalla emergente del cliente muestra automáticamente el historial de contacto; si no, debe consultarse manualmente.
- Se agrega alias de campo por paquete de clientes, usado como encabezado al exportar desde Control de Calidad y Clientes.
- Paquetes de clientes: se muestran en gris si la campaña asociada fue eliminada; al eliminar un paquete se deshabilita la campaña asociada (sin permitir cambiar su estado); se agrega un ID de importación por lote para identificar el plan de importación de origen de cada cliente.
- Clientes: se puede eliminar por búsqueda (los clientes con estado distinto de "abierto" no se pueden eliminar); se optimiza el rendimiento del borrado masivo.
- Control de calidad (Qcpage): se optimiza el estilo de la página de escucha; el encabezado se puede personalizar y exportar datos desde la misma página.
- Resultados: el administrador de equipo puede ver los resultados a nivel de sistema.
- Monitores de datos: se agrega el total de éxitos.
- CDRs: se agregan campos relacionados con el marcador.

**Oficina virtual (virtualoffice-1.4)**

- Personalización: se agregan cuatro tipos de campo (subida de archivo, fecha, fecha y hora, enlace); se corrige que no se podían guardar campos personalizados para varios clientes virtuales a la vez; al eliminar un campo personalizado se elimina también de la tabla correspondiente.

**Marcador (dialer-1.3)**

- Se corrige un error de búsqueda por fecha de marcado en la página de reciclado; se corrige que el marcador no funcionaba al reciclar clientes mediante filtro.
- Se agrega el campo `Dial Time` (visible y buscable); se corrige que aparecía invertido respecto a `Callee Answer`.
- Al pasar el mouse sobre el nombre de la campaña se muestra su horario laboral; las campañas fuera de horario se muestran en gris.
- Configuración del marcador: se agregan avisos adicionales.
- Lista de marcación de campaña: se pueden mostrar y buscar los campos configurados por la campaña; se puede eliminar por selección o por búsqueda.
- Registro de filtros: se agrega la hora de finalización.

**Fax (fax-1.3)**

- Al enviar un fax, si ya hay uno en curso, no se reinicia el mensaje de estado de la operación del usuario.

**Plataforma de trabajo del agente**

- El agente puede cambiar su grupo de uso por defecto (mediante radio button), disponible solo si el grupo tiene vinculación de aplicación entrante; si solo existe un grupo, ese es el grupo por defecto (sin radio button visible).
- La opción "Mis órdenes de trabajo" del menú básico se traslada al módulo de gestión de órdenes de trabajo, controlada por permisos de rol.
- Para pausar o gestionar llamadas con error ya no se requiere el usuario/contraseña del líder de grupo; basta con usuario+contraseña o número de agente+contraseña.

**Pantalla emergente de campaña**

- Se corrige que guardar un cliente duplicado no mostraba aviso.
- Se agrega un menú de estado de trabajo del agente con el total de éxitos en la campaña actual.
- Se elimina el límite de caracteres del memo de contacto.
- Se corrige el conteo total mostrado bajo las pestañas "Nuevo", "Pendiente", "Fallido" y "Éxito".
- Se migran los estilos de elementos a clases CSS.

**Pantalla emergente de oficina virtual**

- Se corrige que el textarea no se podía editar; se optimiza el estilo.

**Pantalla emergente de atención al cliente**

- Mejoras en la identificación de área telefónica del número de origen.

**Calendario**

- Se corrigen textos multilingües en la gestión de horarios/calendario.

## AsterCC 1.1

**Core**

- Los campos de texto eliminan automáticamente los espacios al inicio/final en alta y edición.
- Al eliminar o deshabilitar un agente se verifica si tiene sesión de cola activa.
- Se usa `phone1` como clave única en los paquetes de clientes.
- Se corrige que no se podían eliminar registros con guion en el listado.
- Correcciones de traducción, de plugins JS y de estilos varios.
- Se corrige que algunas páginas no mostraban correctamente la barra de progreso de carga.
- Se corrige que no se podían recuperar extensiones desde la papelera.
- Al eliminar una campaña, aplicación o cliente virtual se eliminan también sus números de identificación de llamada (cvnumbers) asociados.
- Equipo: al editar los máximos (cuentas, dispositivos, agentes, colas, salas de conferencia) el valor no puede ser menor al total ya existente.
- Cuenta: el límite de tiempo de exportación queda desactivado por defecto.
- Rol: se agrega función de plegado de módulos en la ventana de permisos de alta/edición.
- Configuración rápida (Quick Setup): el tiempo de espera por defecto es 45; al previsualizar se muestra el uso actual del equipo; si el prefijo de usuario termina en número, los siguientes se incrementan correlativamente (ej. Astercc01, Astercc02...).
- Edición rápida: se agrega función de restablecer contraseña al editar un dispositivo.
- Grupo de agentes: se muestra el grupo actual del agente al agregarlo/editarlo; al actualizar la cola del grupo se actualiza también la extensión de entrada de la campaña (si el módulo está instalado); la cola creada automáticamente inicia en estado nuevo; se puede definir la prioridad (`penalty`) de cada agente en el grupo.
- Dispositivo: el buzón de voz queda habilitado por defecto y su contraseña es obligatoria; no se muestran usuario/clave de registro cuando el tipo es externo; se agrega mensaje de instrucciones del buzón de voz.
- Troncal: se muestra la cadena de registro en la lista; el estado de la regla pasa a tener las opciones Habilitado/Deshabilitado/Rechazar (rechazar impide la llamada cuando la regla coincide).
- Grupo de DID: se agrega tipo de coincidencia (número o prefijo), heredado por los DID del grupo.
- Cola: el "autofill" inicia en "sí" por defecto; el equipo de la cola no se puede editar tras creada.
- Ruta entrante: el equipo es obligatorio; se agrega la opción "Coincidencia automática" para la transferencia (permite elegir una cuenta directamente en vez de un ID de acción); se puede buscar por número DID.
- Extensión: no se puede editar la extensión si su destino es una cola; si el destino es un IVR, al editar se actualiza la extensión de entrada de la campaña (si el módulo está instalado); una cola con extensión ya asignada no admite otra.
- Grupo de troncales: se agrega configuración de reglas de grupo, verificando duplicados al guardar.
- Lista blanca: se puede guardar sin elegir equipo ni cuenta.
- CDRs: se agrega visualización y búsqueda por duración.
- IVR: al editar la extensión del IVR se actualiza la extensión de entrada de la campaña (si aplica); el tipo de obtención de datos queda vacío al cambiar a tipo normal; en "Edit IVR Dest", si `Follow Action` es "No", el tipo de acción de seguimiento queda vacío.
- DAHDI: ajustes de estilo.
- Monitor de grupo de agentes: se puede forzar pausa (con motivo) o forzar disponibilidad, y editar la prioridad del agente (reordena automáticamente); se corrige la duplicación de filas iguales; un agente en modo "solo saliente" se muestra como "libre (solo saliente)"; se corrige que se podían ejecutar escucha, intrusión, corte forzado y susurro sin ingresar número telefónico.
- Configuración: se agregan parámetros para el formato de visualización de duración y de segundos; el límite de tiempo de exportación por defecto pasa a las 18:00.
- Contraseña del sistema: admite a-z, A-Z, números y los símbolos `_ \ / , . * ! @ # $ %`.
- Cuadro de búsqueda: el campo de fecha/hora admite entrada manual además de selector.
- Importación: coincidencia automática del nombre de campo con el encabezado (primera fila); si el cliente ya existe en el paquete, se usa como cliente de la lista de marcación de campaña; el administrador de equipo puede importar clientes al paquete de su propio equipo.
- Usuarios en línea: ya no se puede forzar el cierre de la propia sesión.
- Códigos de función: se agrega "Consultar agente", por defecto `*55`.
- Plataforma de trabajo del agente: se corrige que, con una sola campaña deshabilitada, la pestaña "Pendiente" mostraba la barra de carga indefinidamente; se optimizan los estilos de la página de consulta en Chrome, de alta de tareas, y de las páginas de "procesamiento de datos con error" y colas de cursor.

**Marcador (dialer-1.2)**

- Se agrega indicador `Online` para mostrar el inicio de sesión del agente por grupo.
- Se corrige que en algunos casos los datos no se mostraban correctamente.
- Al reciclar un cliente sin indicar prioridad, se usa la prioridad ya guardada en el registro.
- Se puede buscar por fecha de creación en la página de reciclado.
- En "Recycle" y "Diallist": se ajusta el formato de duración, se muestra el total de datos y de páginas, y se puede ocultar/mostrar el cuadro de búsqueda.
- Si un campo tiene el foco, no se sobrescribe con la actualización automática.
- Correcciones de estilo.
- Lista de marcación de campaña: al reciclar sin prioridad se usa la ya guardada; se agrega visualización y búsqueda por agente y por número de intentos (`autocount`).
- Se agrega una página de estadísticas del marcador.

**Campaña (campaign-1.2)**

- El grupo de agentes es obligatorio; se corrige el guardado incorrecto de `Dial-in Exten.`; `Agent Max. Own` inicia en 100; el estado del marcador para la campaña queda habilitado; en la configuración de campos se puede reordenar el orden de visualización arrastrando; se permite agregar/editar `Average Answered Ringing Time`, `Average Talking Time`, `Average Answered Rate` y `Average Followup`; se agregan `ShortCallSec`, `ShortCallRate`, `ShortCallAcwSec` y `CalleeWaitSec`; se permite editar `DialerCap` y agregar `Dialerval`; al eliminar de la papelera se eliminan también los registros en `campaign_diallists` y `campaign_cdrs`; se agrega `Default Status` para la pantalla emergente del cliente; `check reassign` inicia en "no"; al guardar la primera campaña se verifica si el equipo tiene un DID vinculado y, si no, se ofrece asignarlo como pantalla emergente entrante por defecto.
- CDRs: se agrega el nombre del agente; el formato de duración sigue la configuración general.
- Campos personalizados: se agregan los tipos `date`, `datetime` y `upload`; se valida duplicidad al guardar; se permite cambiar el tipo entre "input" y "select".
- Clientes: se agrega búsqueda por número de agente; en el alta solo se muestran los campos editables configurados por la campaña, y en la edición todos los campos configurados; se agrega visualización y búsqueda por agente y por `autocount`; se corrige un error de JS cuando no existe ninguna campaña.
- Control de calidad (Qc): la lista de campos sigue la configuración de la campaña; el administrador de equipo puede ver los datos del equipo "0"; al escuchar una grabación se puede ver la información del cliente y de la encuesta.

**Oficina virtual (virtualoffice-1.2)**

- Ajustes de estilo en la página de clientes.

**Encuestas (survey-1.2)**

- Ajustes de estilo en algunas ventanas emergentes de la página de encuestas.

## AsterCC 1.1-beta2

**Core**

- Se agregan modos de trabajo del agente: solo saliente, solo entrante y ambos; en modo saliente el agente no recibe llamadas distribuidas por el grupo, en modo entrante no puede marcar por su cuenta, y en modo "ambos" puede marcar y también recibir llamadas del grupo al estar libre; se puede controlar si el agente elige su propio modo.
- Se agrega el estado de procesamiento posterior a la llamada (ACW), con modos: al timbrar (incluye llamadas no contestadas), al finalizar una llamada contestada, y con posibilidad de que el agente elija su modo de ACW libremente.
- Se mejora la función de pausa del agente: se puede elegir un motivo de pausa (útil para analizar el comportamiento del agente) y se agrega función de bloqueo de pantalla.
- Se agrega la pantalla emergente de aplicación y extensión por defecto: al configurarse una aplicación por defecto por equipo, las llamadas no asociadas a cola (por ejemplo entrantes por DID) o las llamadas salientes directas también disparan la pantalla emergente correspondiente.
- Mejoras en la interfaz del agente: además del control de ACW, se agrega inicio y cierre de sesión con un clic.
- Identificador de llamada del cliente: al marcar por saliente o predictivo, el nombre del cliente se muestra como nombre de quien llama en el teléfono del agente.
- Sala de conferencias: se muestra el estado de los invitados mientras están siendo llamados.
- Encuestas/calificación: se agrega soporte de calificación en llamadas salientes; en la página de calificación se agregan botones para escuchar y descargar la grabación.
- Se corrige el orden incorrecto de algunos parámetros especiales al recargar el archivo de configuración.
- Se agrega plantilla de fax en el envío masivo de mensajes.
- La API de JS agrega interfaces de corte forzado y de susurro (whisper).
- Se mejora el soporte de importación de datos multilingües, incluyendo la selección de hora de marcado y prioridad al importar a la lista de marcación.
- Se agrega límite de horario de ejecución de exportación: solo cuentas con permiso pueden exportar en cualquier momento; el resto solo puede hacerlo después de la hora configurada en el sistema.
- La función de líder de grupo se muestra por separado en un menú propio en la interfaz del agente.

**Marcación saliente (outbound-1.1)**

- Se agrega envío de fax con un clic (requiere el módulo de fax instalado): permite enviar una plantilla o subir un PDF.
- Filtro de lista negra: permite verificar contra decenas de millones de registros de lista negra y depurar los paquetes de clientes de una campaña; los coincidentes se guardan en un archivo aparte para analizar la calidad del origen de los datos.
- Se agrega función de detección de duplicados en la gestión de clientes.
- El historial de llamadas de campaña se muestra separado por tarea.
- Se corrige que, en Firefox 10.0.x, tras guardar un cliente nuevo desde la pantalla emergente, la encuesta no podía iniciarse.

**Marcador (dialer-1.1)**

- El marcador predictivo ya puede marcar directamente a un IVR.
- Se agregan los eventos `PDDIALER-callcallee`, `PDDIALER-calleeanswer`, `PDDIALER-calltarget`, `PDDIALER-agentanswer` y `PDDIALER-hangup`.
- Se agrega un menú independiente del marcador, controlable también en modo de sesión por cuenta.
- Nueva página de lista de marcación: permite gestionarla y crear filtros (planes de filtrado que agregan clientes que cumplen la condición a la lista).
- Nueva página de configuración del marcador: permite definir el máximo de concurrencia por equipo y el modo de concurrencia.

**Oficina virtual (virtualoffice-1.1)**

- Se agrega función de detección de duplicados en la gestión de clientes.
- Se ajustan los campos de búsqueda y los campos mostrados por defecto en el historial de llamadas.

**Fax (fax-1.1)**

- Se corrige que la interfaz de envío manual de fax no se mostraba en la versión en inglés de la página de envío de fax.

**Encuestas (survey-1.1)**

- Se mejora el método de exportación de cuotas y se agrega límite de horario de ejecución para la exportación.

**BPO (bpo-1.1)**

- Se corrigen problemas de estilo en las páginas de control de calidad y gestión de clientes.

**Financiero (financial-1.1)**

- La función de facturación se traslada del módulo de reportes al módulo financiero.

## AsterCC 1.1-beta1

**Parche 1 (asterCC-1.1-beta1-patch1)**

- Se corrige que el marcador no limpiaba la tarea correspondiente cuando fallaba el intento de marcado.
- Se corrige que la música de espera por defecto no se mostraba como seleccionada en la cola.
- En Configuración rápida (creación de extensión, o de extensión y agente) se agrega la opción de elegir el tono de retorno de llamada (Music Ring Back Tone) mediante el botón de configuración detallada.
- En Edición rápida se puede modificar el tono de retorno de llamada de la extensión.
- En la página de horario laboral se agregan nombre, fecha de inicio y fecha de fin; en la página de paquete de horario, la selección ahora muestra el nombre del horario en vez de su detalle.
- Se agrega búsqueda de valores vacíos por campo.
- Se corrige que el CDR de campaña o de cliente virtual no registraba el número de destino en llamadas entrantes o del marcador.
- La página de actualización de módulos de asterCC permite elegir el servidor espejo (mirror) de descarga.
- En el módulo de estadísticas, la página de agente agrega las métricas "Duración total entrante" y "Duración total saliente" (timbrado + conversación).
- Se agregan botones de actualización manual del estado del dispositivo y del estado de la llamada en la plataforma del agente (agentdesk).
- Se corrige un `model_id` incorrecto de la función de marcado en la API de JS.

**Parche del marcador (asterCC-1.1-beta1-dialer-1.0-patch1)**

- Se corrige que el marcador no obtenía correctamente el número de la cola.
- Se corrige que en algunos casos el marcador no podía iniciarse.

**Parche de marcación saliente (asterCC-1.1-beta1-outbound-1.0-patch1)**

- Se corrige que en algunos casos no se podía limpiar la cuota de encuesta en la plataforma del agente.

**Parche de llamadas entrantes (asterCC-1.1-beta1-inbound-1.0-patch1)**

- Se corrige que el número que llama y el número llamado (src/dst) aparecían invertidos en el CDR de llamadas entrantes.

---

## Fuentes

- `raw/zh/change_log/astercc_login_security_patch.txt`
- `raw/en/change_log/astercc-4.2_changelog.txt`
- `raw/zh/change_log/astercc-4.2_changelog.txt`
- `raw/en/change_log/astercc-4.1_changelog.txt`
- `raw/zh/change_log/astercc-4.1_changelog.txt`
- `raw/en/change_log/astercc-3.2-rc1_changelog.txt`
- `raw/zh/change_log/astercc-3.2-rc1_changelog.txt`
- `raw/en/change_log/astercc-2.6-rc2_changelog.txt`
- `raw/zh/change_log/astercc-2.6-rc2_changelog.txt`
- `raw/en/change_log/astercc-2.6-rc1_changelog.txt`
- `raw/zh/change_log/astercc-2.6-rc1_changelog.txt`
- `raw/en/change_log/astercc-2.4-rc2_changelog.txt`
- `raw/zh/change_log/astercc-2.4-rc2_changelog.txt`
- `raw/en/change_log/astercc-2.4-rc1_changelog.txt`
- `raw/zh/change_log/astercc-2.4-rc1_changelog.txt`
- `raw/en/change_log/astercc-2.3-rc2_changelog.txt`
- `raw/zh/change_log/astercc-2.3-rc2_changelog.txt`
- `raw/en/change_log/astercc-2.3-rc1_changelog.txt`
- `raw/zh/change_log/astercc-2.3-rc1_changelog.txt`
- `raw/en/change_log/astercc-2.2_changelog.txt`
- `raw/zh/change_log/astercc-2.2_changelog.txt`
- `raw/en/change_log/astercc-2.2-rc4_changelog.txt`
- `raw/zh/change_log/astercc-2.2-rc4_changelog.txt`
- `raw/en/change_log/astercc-2.2-beta_changelog.txt`
- `raw/zh/change_log/astercc-2.2-beta_changelog.txt`
- `raw/en/change_log/astercc-2.2-alpha_changelog.txt`
- `raw/zh/change_log/astercc-2.2-alpha_changelog.txt`
- `raw/en/change_log/astercc-2.1_changelog.txt`
- `raw/zh/change_log/astercc-2.1_changelog.txt`
- `raw/en/change_log/astercc-2.0_changelog.txt`
- `raw/zh/change_log/astercc-2.0_changelog.txt`
- `raw/en/change_log/astercc-2.0-beta_changelog.txt`
- `raw/zh/change_log/astercc-2.0-beta_changelog.txt`
- `raw/en/change_log/astercc-1.2_changelog.txt`
- `raw/zh/change_log/astercc-1.2_changelog.txt`
- `raw/en/change_log/astercc-1.2.2_changelog.txt`
- `raw/zh/change_log/astercc-1.2.2_changelog.txt`
- `raw/en/change_log/astercc-1.2.1_changelog.txt`
- `raw/zh/change_log/astercc-1.2.1_changelog.txt`
- `raw/en/change_log/astercc-1.2-beta_changelog.txt`
- `raw/en/change_log/astercc-1.2_beta_changelog.txt`
- `raw/zh/change_log/astercc-1.2-beta_changelog.txt`
- `raw/en/change_log/astercc-1.1_changelog.txt`
- `raw/zh/change_log/astercc-1.1_changelog.txt`
- `raw/en/change_log/astercc-1.1-beta2_changelog.txt`
- `raw/zh/change_log/astercc-1.1-beta2_changelog.txt`
- `raw/en/change_log/astercc-1.1-beta1_changelog.txt`
- `raw/zh/change_log/astercc-1.1-beta1_changelog.txt`
