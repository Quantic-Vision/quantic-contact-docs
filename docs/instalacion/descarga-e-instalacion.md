---
title: "Descargar e instalar AsterCC"
resumen: "Cómo instalar AsterCC mediante el script de instalación automática sobre Rocky Linux 9."
seccion: "2.2 Descarga e instalación (ISO / manual)"
tipo: tutorial
nivel: basico
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [requisitos, instalar-desde-usb, configuracion-post-instalacion]
---

# Descargar e instalar AsterCC

## Qué es

El método recomendado para instalar AsterCC hoy es el **script de instalación automática sobre Rocky Linux 9**, que instala y configura Asterisk, Nginx, PHP, MariaDB y Redis en el orden correcto. Existe también un método por **ISO autoinstalable** para versiones anteriores del sistema — se documenta como referencia, pero se recomienda usar el script sobre Rocky 9 salvo que tengas una razón específica para usar la ISO.

## Cómo se usa

### Método recomendado: script sobre Rocky Linux 9

1. Confirma que cumples los [requisitos del sistema](requisitos.md) y que tienes acceso **root** al servidor.
2. Descarga el script de instalación:
   ```bash
   cd /usr/src/
   wget http://download2.astercc.org/install_asterCC_Commercial_Rocky9_php74_lastest.sh
   ```
3. Dale permisos de ejecución:
   ```bash
   chmod +x install_asterCC_Commercial_Rocky9_php74_lastest.sh
   ```
4. Ejecuta el script por primera vez:
   ```bash
   ./install_asterCC_Commercial_Rocky9_php74_lastest.sh
   ```
   Elige el sitio de descarga de dependencias cuando el script lo solicite. Esta primera ejecución actualiza el kernel e instala las dependencias necesarias.

   ![Selección del sitio de descarga de dependencias](../assets/images/instalacion/astercc-4.2_install-1.png)

5. Al finalizar, el script pedirá reiniciar el servidor:
   ```bash
   reboot
   ```

   ![Aviso de instalación de dependencias completada](../assets/images/instalacion/astercc-4.2_install-2.png)

6. Después de reiniciar, ejecuta el script **por segunda vez**:
   ```bash
   cd /usr/src/
   ./install_asterCC_Commercial_Rocky9_php74_lastest.sh
   ```
7. Durante esta segunda ejecución, el script pedirá:
   - Una contraseña para la base de datos.
   - Usuario y contraseña para el [Asterisk AMI](../administracion/asterisk-ami.md).

   ![Solicitud de contraseña de base de datos y credenciales de AMI](../assets/images/instalacion/astercc-4.2_install-3.png)

8. Espera a que termine (el tiempo depende de tu conexión y del rendimiento del servidor). Al finalizar, verás un mensaje de instalación completada.

   ![Instalación en progreso](../assets/images/instalacion/astercc-4.2_install-4.png)
   ![Mensaje de instalación completada](../assets/images/instalacion/astercc-4.2_install-5.png)

9. Abre un navegador y entra a la IP externa del servidor. Inicia sesión con `admin` / `admin` y **cambia la contraseña inmediatamente**.
10. Sigue las instrucciones en pantalla para completar la inicialización, y continúa con [Configuración post-instalación](configuracion-post-instalacion.md).

### Método alternativo: ISO autoinstalable

!!! warning "Puede estar desactualizado"
    Este método corresponde a versiones anteriores de AsterCC y usa un instalador basado en ISO. Antes de usarlo, confirma con el proveedor si sigue siendo la vía soportada para tu versión.

1. Descarga el archivo ISO de 64 bits desde el sitio oficial de AsterCC.
2. Graba la ISO en un disco (o móntala en una máquina virtual para pruebas).
3. Arranca el servidor desde el disco/ISO. Verás la pantalla inicial del instalador:

   ![Pantalla inicial del instalador ISO](../assets/images/instalacion/iso_init.png)

4. Sigue el asistente: selección de red (IPv4 es suficiente; la instalación inicial solo soporta DHCP — configura IP fija después de instalar):

   ![Selección de red durante la instalación](../assets/images/instalacion/iso_network.png)

   zona horaria:

   ![Selección de zona horaria](../assets/images/instalacion/iso_timezone.png)

   y contraseña de `root`:

   ![Configuración de la contraseña de root](../assets/images/instalacion/iso_password.png)

   Si la contraseña elegida es débil, el sistema lo advierte antes de continuar:

   ![Aviso de contraseña débil](../assets/images/instalacion/iso_weak_password.png)

5. La instalación toma unos 10 minutos y reinicia el servidor una vez — asegúrate de que el segundo arranque sea desde el disco duro, no desde el disco de instalación.

   ![Progreso de instalación de paquetes](../assets/images/instalacion/iso_rpm.png)

6. Al finalizar verás la pantalla de inicio de sesión de la consola:

   ![Pantalla de login tras la instalación](../assets/images/instalacion/iso_login.png)

   Inicia sesión como `root` con la contraseña configurada; el sistema mostrará la IP del servidor:

   ![Consola mostrando la IP del servidor tras iniciar sesión](../assets/images/instalacion/iso_logged.png)

7. Abre esa IP en el navegador para llegar a la pantalla de login de AsterCC.

## Referencia rápida

| Método | Cuándo usarlo |
|---|---|
| Script sobre Rocky Linux 9 | Instalaciones nuevas (recomendado) |
| ISO autoinstalable | Solo si tu versión de AsterCC lo requiere explícitamente |

| Dato | Valor |
|---|---|
| Usuario inicial | `admin` / `admin` |
| Ruta de dependencias (script) | `/usr/src/` |

---

## Fuentes

- `raw/zh/下载和安装/在rocky9中进行安装.txt`
- `raw/en/download_and_install/iinstall_in_rocky9.txt`
- `raw/zh/下载和安装/安装.txt`