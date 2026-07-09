---
title: "Configurar AsterCC después de instalar"
resumen: "Qué configurar la primera vez que accedes a AsterCC tras la instalación."
seccion: "2.4 Configuración post-instalación"
tipo: tutorial
nivel: intermedio
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [descarga-e-instalacion, guia-administradores]
---

# Configurar AsterCC después de instalar

## Qué es

Después de instalar AsterCC, el primer acceso al sistema dispara un asistente de inicialización antes de poder usar la plataforma normalmente.

## Cómo se usa

### 1. Primer acceso

1. Abre un navegador (se recomienda Firefox o Chrome) y entra a la IP del servidor, por ejemplo `http://192.168.1.110`.
2. Inicia sesión con el usuario y contraseña iniciales: `admin` / `admin`.
3. El sistema ejecuta una inicialización — espera a que termine.

### 2. Asistente de inicialización

1. Selecciona el **idioma por defecto** del sistema.
2. Cuando pregunte si quieres importar datos de demostración, decide según tu caso: importarlos ayuda a explorar el sistema rápido, pero para un entorno de producción normalmente se elige **no importar**.
3. Ingresa un **correo del administrador** — el sistema lo usa para notificaciones.

Con esto termina la inicialización. A partir de aquí, el sistema queda listo para la configuración funcional: cuentas, extensiones, troncales y agentes, cubierta en [Guía rápida para administradores](../primeros-pasos/guia-administradores.md).

!!! tip
    Cambia la contraseña del usuario `admin` inmediatamente después del primer acceso — no la dejes en el valor por defecto.

### 3. Preparar archivos de música en espera (opcional)

Antes de subir archivos de música en espera desde la interfaz (ver [Gestión de música en espera](../modulos/pbx-funciones-avanzadas.md#gestion-de-musica-en-espera)), conviene normalizarlos en el servidor para que suenen bien y en el formato correcto (8000 Hz, 16 bits, mono):

1. Convierte los archivos de audio a `.wav` (por ejemplo con Audacity, agregando el plugin LAME si el origen es MP3).
2. En el servidor, instala `sox`: `yum install sox`.
3. Ejecuta un script que recorra los `.wav` y normalice volumen y formato:
   ```bash
   for i in *.wav; do
       val=${i%.wav}
       ampl=$(sox "$i" -t wav /dev/null stat -v 2>&1 | grep -v sox:)
       sox -v "$ampl" "$i" -t wav -r 8000 -b 16 -c 1 -s -t wav "$val.converted.wav"
       sox -v .5 "$val.converted.wav" "$val.wav"
       rm -f "$val.converted.wav"
   done
   ```
4. Copia los archivos resultantes a `/var/lib/asterisk/moh/` en el servidor.
5. Aplica el cambio sin reiniciar Asterisk: `asterisk -r`, luego dentro de la consola `moh reload`.

Una vez copiados los archivos al servidor, defínelos como música en espera reutilizable desde la interfaz en [Gestión de música en espera](../modulos/pbx-funciones-avanzadas.md#gestion-de-musica-en-espera).

## Referencia rápida

| Paso | Valor |
|---|---|
| URL de acceso | `http://<ip-del-servidor>` |
| Usuario inicial | `admin` / `admin` |
| Navegadores recomendados | Firefox, Chrome |

---

## Fuentes

- `raw/zh/新手上路/快速配置手册.txt`
- `raw/en/installation_guideline_and_setup/setup_moh.txt`