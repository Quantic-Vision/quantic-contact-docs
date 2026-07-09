---
title: "Administración avanzada"
resumen: "Configuración de infraestructura de soporte: AMI, VPN, caché de PHP y correo saliente."
seccion: "6. Administración avanzada"
tipo: concepto
nivel: avanzado
roles: [administrador]
fuente: en
obsoleto: false
relacionados: []
---

# Administración avanzada

!!! warning "Contenido con partes desactualizadas"
    Tres de los artículos de esta sección documentan procedimientos de infraestructura de 2018 (OpenVPN, APC, Mailman) que ya no aplican tal cual sobre la instalación actual (Rocky Linux 9 / PHP 7.4). El artículo de configuración y mantenimiento del sistema también usa rutas de ejemplo de una instalación de referencia antigua. Cada artículo indica específicamente qué cambió.

| Artículo | Contenido | Vigente |
|---|---|---|
| [Configurar Asterisk AMI](asterisk-ami.md) | Cuenta AMI que usa AsterCC para operar Asterisk | Sí |
| [Configurar OpenVPN](openvpn.md) | Acceso remoto para teléfonos IP fuera de la oficina | Conceptos sí, comandos no |
| [Configurar APC (caché de PHP)](apc.md) | Caché de opcode — reemplazado por OPcache en PHP 7.4 | No (ver equivalente) |
| [Configurar Mailman / correo saliente](mailman.md) | Dependencias Perl para envío de correo masivo | Parcial |
| [Diagnóstico de red y VoIP](diagnostico-red-voip.md) | ngrep, tcpdump/Wireshark, SIP sobre TLS, Samba, replicación MySQL | Comandos base sí, vías/paquetes a confirmar |
| [Configuración y mantenimiento del sistema](configuracion-y-mantenimiento-sistema.md) | Respaldos, comandos y logs del núcleo, red, servidores PBX, planes de grabación, configuración general, códigos de función, menú lateral, instalación de módulos | Conceptos sí, rutas/comandos de ejemplo de instalación de referencia antigua |
| [Documentación histórica — AsterCC 1.2 beta](historial-documentacion-1.2-beta.md) | Resumen de referencia de los 41 documentos del wiki original sobre la versión 1.2 beta (PBX, outbound, clientes, mensajería, encuestas, predial, cuentas, sistema) | No |

## Nota histórica: fax por IAXmodem + HylaFax

!!! warning "Contenido obsoleto"
    El envío/recepción de fax en AsterCC hoy se gestiona como un módulo propio (ver [Fax — dispositivos y envío](../modulos/mensajeria-wechat-fax.md#fax-dispositivos-y-envio)). El siguiente procedimiento documenta una vía de infraestructura de bajo nivel —anterior a ese módulo— para dar salida/entrada de fax a través de Asterisk usando un módem virtual sobre IAX2 y el software HylaFax. Se conserva por completitud histórica; no es la vía recomendada actualmente.

El procedimiento original (sobre CentOS antiguo) consistía en: compilar e instalar **IAXmodem** (`libiax2` y `spandsp`) desde código fuente, crear un dispositivo de módem virtual (`/dev/ttyIAXn`) configurado con su propio archivo en `/etc/iaxmodem/`, registrar ese módem como un "friend" IAX2 en `/etc/asterisk/iax_modem.conf` e incluirlo desde `iax.conf`, recargar IAX2 desde la consola de Asterisk (`iax2 reload`), arrancar el proceso `iaxmodem` para el dispositivo, y finalmente instalar **HylaFax** (vía RPM) y ejecutar `faxsetup` para completar la configuración del lado de fax.

## Fuentes

- `raw/en/others/iaxmodem_and_hylafax.txt`
