---
title: "Configurar APC (caché de PHP)"
resumen: "Cómo instalaba APC para acelerar PHP en versiones antiguas — y con qué se reemplaza en PHP moderno."
seccion: "6.3 APC (caché de PHP)"
tipo: tutorial
nivel: avanzado
roles: [administrador]
fuente: en
obsoleto: true
relacionados: [requisitos]
---

# Configurar APC (caché de PHP)

## Qué es

**APC (Alternative PHP Cache)** es una extensión de caché de opcode para PHP, usada en versiones antiguas de PHP para acelerar la ejecución evitando recompilar el código en cada request.

!!! warning "Puede estar desactualizado"
    APC fue descontinuado y **no es compatible con PHP 5.5+**. Dado que la instalación actual de AsterCC usa **PHP 7.4** (ver [Requisitos del sistema](../instalacion/requisitos.md)), esta guía original ya no aplica directamente. En PHP 7.4, la funcionalidad equivalente la provee **OPcache**, incluida en el propio PHP — normalmente ya viene habilitada por el instalador. Verifica con `php -m | grep -i opcache` o revisando `php.ini`.

## Cómo se usa (procedimiento original — solo referencia histórica)

1. Instalar las herramientas de compilación de PHP:
   ```bash
   yum install php-pear php-devel httpd-devel
   ```
2. Instalar APC vía PECL:
   ```bash
   pecl install apc
   ```
3. Habilitar la extensión en `php.ini`, agregando debajo de la sección de extensiones dinámicas:
   ```ini
   extension=apc.so
   ```
4. Reiniciar PHP y el servidor web:
   ```bash
   /etc/init.d/php_cgi restart
   /etc/init.d/httpd restart
   ```

## Referencia rápida

| Versión de PHP | Caché de opcode a usar |
|---|---|
| PHP < 5.5 (documentación original) | APC |
| PHP 7.4 (instalación actual) | OPcache (incluido en PHP) |

---

*Fuente: `raw/en/install_apc.txt`.*
