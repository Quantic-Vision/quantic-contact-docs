---
title: "Integrar el envío de SMS"
resumen: "Cómo conectar AsterCC con una plataforma de SMS de terceros por HTTP, o con un módem GSM por puerto serie, para el envío de mensajes."
seccion: "7.10 API de integración — Envío de SMS"
tipo: guia
nivel: avanzado
roles: [desarrollador]
fuente: zh
obsoleto: true
relacionados: [introduccion-api-integracion, api-y-ami]
---

# Integrar el envío de SMS

## Qué es

AsterCC almacena los SMS que un agente redacta desde la [plataforma de trabajo](../glosario.md#sistema-del-agente-plataforma-de-trabajo) en tablas propias, pero **no los envía directamente** — el envío real requiere una integración externa. Hay dos caminos según el hardware/proveedor disponible:

- **Plataforma de SMS de terceros por HTTP:** un script propio lee los mensajes pendientes de la base de datos y los entrega a la API HTTP del proveedor de SMS.
- **Módem GSM por puerto serie:** conectar un módem GSM físico (con tarjeta SIM) al servidor, y que AsterCC use ese módem directamente como pasarela de envío.

## Cómo se usa

### Opción A — Plataforma de SMS de terceros (script propio)

1. **Flujo:** el agente escribe el SMS y pulsa "Enviar" en la plataforma de trabajo; AsterCC guarda el mensaje en las tablas `cc10_batchcontacts` (metadatos: destinatario, remitente, estado) y `cc10_batchcontact_archives` (contenido). Un script propio debe leer los mensajes pendientes, entregarlos al proveedor externo, y actualizar el estado según la respuesta.

2. **Campos relevantes de `cc10_batchcontacts`:**

   | Campo | Uso |
   |---|---|
   | `batchcontact_archive_id` | Relaciona con `cc10_batchcontact_archives` (contenido del mensaje) |
   | `target` | Número de teléfono destinatario |
   | `status` | `new` (pendiente — tu script debe tomarlo), `pending` (en envío — márcalo así al iniciar el envío), y al terminar: `success`, `failed` o `error` según la respuesta del proveedor |
   | `schedulertime` | Hora programada de envío; `0000-00-00 00:00:00` significa enviar inmediatamente — tu script debe filtrar por este campo menor a la hora actual |
   | `contacttime` | Hora en que se entregó el mensaje al proveedor externo — actualízala junto con `status` |
   | `creby` / `created` | Cuenta y fecha de creación del mensaje |
   | `error_msg` | Detalle del error, si el envío falló |
   | `responsenote` | Respuesta del destinatario, si el proveedor la reenvía |

3. **Campos relevantes de `cc10_batchcontact_archives`:** `archivetype` (`email` o `sms`), `content` (el texto del mensaje).

4. **Patrón de implementación:** un script (ej. `sms.php`) que: (a) consulta los mensajes con `status='new'` y `schedulertime` vencido, (b) los entrega a la API HTTP del proveedor, (c) actualiza `status`/`contacttime`/`error_msg` según la respuesta. Puede ejecutarse por `crontab` (ej. cada minuto) o como un proceso en bucle continuo en el servidor.

### Opción B — Módem GSM por puerto serie (gnokii)

1. **Hardware:** conectar el módem al puerto serie 1 del servidor, insertar la SIM y encenderlo.

2. **Instalar y configurar `minicom`** (para verificar la comunicación serie):
   ```bash
   yum -y install minicom
   minicom -s
   ```
   En el menú de configuración de puerto serie: cambiar **Serial Device** a `/dev/ttyS0` (si el módem está en el primer puerto serie), y la velocidad (baud rate) según lo que requiera el módem (ej. `115200`). Guardar como configuración por defecto y salir.

3. **Instalar `gnokii`** (driver que AsterCC usa para hablar con el módem):
   ```bash
   wget http://www.gnokii.org/download/gnokii/gnokii-0.6.31.tar.gz
   yum -y install intltool gettext glib2 glib2-devel mysql-devel
   ./configure && gmake && gmake install
   ln -s /usr/local/bin/gnokii /usr/bin/
   ```
   !!! warning
       Instalar `mysql-devel` puede actualizar y reiniciar automáticamente MySQL en el servidor — planifica esta instalación fuera de horario productivo.

4. **Configurar `gnokii`** en `/root/.config/gnokii/config`:
   ```ini
   [global]
   port = /dev/ttyS0
   model = AT
   initlength = default
   connection = serial
   use_locking = no
   serial_baudrate = 115200
   smsc_timeout = 10
   ```

5. **Probar el envío manual** antes de integrarlo con AsterCC:
   ```bash
   echo "test" | /usr/bin/gnokii --config /root/.config/gnokii/config --sendsms <número-destino-sin-0-inicial>
   ```

6. **Configurar AsterCC** — en `/etc/astercc.conf`, sección `[smsman]`, agregar:
   ```
   device=gnokii,ttyS0,/root/.config/gnokii/config,5,,0
   ```
   Parámetros (separados por coma): tipo de dispositivo (`gnokii`), puerto serie, ruta al archivo de configuración de `gnokii`, intervalo (segundos) entre envíos consecutivos por este dispositivo, prefijo a agregar al número destino (vacío en el ejemplo), prefijo a quitar del número destino (`0` en el ejemplo, para eliminar el `0` inicial).

7. **Reiniciar el proceso de SMS de AsterCC:**
   ```bash
   /opt/asterisk/scripts/astercc/astcc_smsman -k
   /opt/asterisk/scripts/astercc/astcc_smsman -d
   ```

### Verificar el envío (aplica a ambas opciones)

Desde la plataforma de trabajo, botón de mensajes → completar destinatario y texto → **Enviar**. Los mensajes pendientes o fallidos se revisan en **Gestión de mensajería masiva → Gestión de mensajes por enviar**; los enviados con éxito, en **Gestión de mensajería masiva → Gestión de mensajes enviados**.

## Referencia rápida

| Necesito | Opción |
|---|---|
| Enviar SMS a través de un proveedor con API HTTP | Opción A — script propio contra `cc10_batchcontacts` |
| Enviar SMS usando una SIM física conectada al servidor | Opción B — módem GSM + `gnokii` |
| Revisar mensajes pendientes o con error | Gestión de mensajería masiva → Gestión de mensajes por enviar |
| Confirmar que un mensaje se envió | Gestión de mensajería masiva → Gestión de mensajes enviados |

---

## Fuentes

- `raw/zh/二次开发者指南/如何使用第三方短信平台发送短信.txt`
- `raw/zh/二次开发者指南/如何将串口短信猫与astercc集成.txt`
