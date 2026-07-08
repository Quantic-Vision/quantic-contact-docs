---
title: "Requisitos del sistema"
resumen: "Requisitos de sistema operativo, arquitectura y componentes que usa AsterCC."
seccion: "2.1 Requisitos del sistema"
tipo: referencia
nivel: basico
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [descarga-e-instalacion, instalar-desde-usb]
---

# Requisitos del sistema

## Qué es

AsterCC corre sobre Linux, con Asterisk como motor de telefonía. La versión soportada más reciente en la documentación original es **AsterCC 4.2**, validada sobre el siguiente stack:

| Componente | Versión |
|---|---|
| Sistema operativo | Rocky Linux 9.6 ("Blue Onyx") |
| Kernel | 5.14.0-570.58.1.el9_6.x86_64 |
| Asterisk | 13.38.3 |
| Servidor web | Nginx 1.20.2 |
| PHP | 7.4.33 |
| Base de datos | MariaDB 10.5.29 |
| Caché | Redis 6.2.20 |

Requisitos adicionales:
- **Arquitectura de 64 bits.** Las imágenes ISO de instalación solo se distribuyen para CPU de 64 bits.
- **Acceso root** al servidor antes de iniciar la instalación.
- **Navegador moderno** para administrar el sistema: Chrome o Firefox (evitar Internet Explorer).

!!! warning "Puede estar desactualizado"
    Existen referencias en la documentación original a instalaciones sobre CentOS 6, que están claramente obsoletas y no se incluyen aquí. Si tu entorno es más antiguo que Rocky Linux 9, valida la compatibilidad antes de instalar.

## Cómo se usa

Antes de instalar, confirma que el servidor (físico o virtual) cumple los requisitos de la tabla anterior y que tienes acceso root. Luego continúa con [Descarga e instalación](descarga-e-instalacion.md).

## Referencia rápida

| Requisito | Valor mínimo |
|---|---|
| Arquitectura | x86_64 |
| Acceso | root |
| Navegador de administración | Chrome o Firefox |

---

## Fuentes

- `raw/zh/下载和安装/在rocky9中进行安装.txt`
- `raw/en/download_and_install/iinstall_in_rocky9.txt`