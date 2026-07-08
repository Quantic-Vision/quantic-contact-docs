---
title: "Configurar AsterCC después de instalar"
resumen: "Qué configurar la primera vez que accedes a AsterCC tras la instalación."
seccion: "2.4 Configuración post-instalación"
tipo: tutorial
nivel: intermedio
roles: [administrador]
fuente: zh
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

## Referencia rápida

| Paso | Valor |
|---|---|
| URL de acceso | `http://<ip-del-servidor>` |
| Usuario inicial | `admin` / `admin` |
| Navegadores recomendados | Firefox, Chrome |

---

*Fuente: `raw/zh/新手上路/快速配置手册.txt` (primera sección).*
