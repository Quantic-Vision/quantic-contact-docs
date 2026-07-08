---
title: "Configurar Asterisk AMI"
resumen: "Cómo dar de alta la cuenta que usa AsterCC para operar Asterisk vía AMI."
seccion: "6.1 Configuración de Asterisk AMI"
tipo: tutorial
nivel: avanzado
roles: [administrador, desarrollador]
fuente: en
obsoleto: false
relacionados: [pbx-y-telefonia, api-y-ami]
---

# Configurar Asterisk AMI

## Qué es

AsterCC necesita acceso al **Asterisk Manager Interface (AMI)** para leer datos de llamadas y ejecutar operaciones sobre Asterisk (originar llamadas, transferir, colgar, etc.). El script de instalación (ver [Descargar e instalar AsterCC](../instalacion/descarga-e-instalacion.md)) pide usuario y contraseña de AMI durante la instalación — esta página documenta cómo se ve esa configuración por si hay que revisarla o recrearla manualmente.

## Cómo se usa

1. Abre el archivo de configuración de manager de Asterisk:
   ```bash
   vi /etc/asterisk/manager.conf
   ```
2. Confirma que AMI está habilitado:
   ```ini
   [general]
   enabled = yes
   ```
3. Agrega (o confirma) la cuenta que usa AsterCC:
   ```ini
   [astercc]
   secret = astercc
   deny = 0.0.0.0/0.0.0.0
   permit = 127.0.0.1/255.255.255.0
   read = call
   write = system,call,agent,user,config,command,reporting,originate
   ```
   !!! warning
       Usa una contraseña propia en `secret` — el valor `astercc` es solo un ejemplo de la documentación original. `permit` debe restringirse a la IP real desde donde AsterCC se conecta al AMI (aquí, localhost).
4. Recarga la configuración desde la consola de Asterisk, sin reiniciar el servicio completo:
   ```bash
   asterisk -r
   ```
   ```
   config reload /etc/asterisk/manager.conf
   ```

## Referencia rápida

| Campo | Qué controla |
|---|---|
| `enabled` | Activa el AMI |
| `secret` | Contraseña de la cuenta AMI |
| `permit` / `deny` | Desde qué IPs se puede conectar esta cuenta |
| `read` / `write` | Qué categorías de eventos/acciones puede leer o ejecutar |

---

*Fuente: `raw/en/asterisk_ami_username_password.txt`.*
