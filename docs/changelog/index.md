---
title: "Historial de versiones"
resumen: "Resumen de las versiones principales de AsterCC y un parche de seguridad crítico para instalaciones expuestas a internet."
seccion: "10. Historial de versiones (Change Log)"
tipo: referencia
nivel: basico
roles: [administrador, desarrollador]
fuente: zh
obsoleto: false
relacionados: [descarga-e-instalacion]
---

# Historial de versiones

## ⚠️ Parche de seguridad de login (aplicar si el sistema está expuesto a internet)

Existen reportes de cuentas comprometidas y datos dañados en sistemas AsterCC expuestos directamente a internet, explotando el endpoint `/login/changelogin`.

**Si tu servidor es accesible desde internet, aplica esto cuanto antes:**

1. Respalda los archivos originales:
   ```bash
   cp /var/www/html/asterCC/app/controllers/login_controller.php login_controller.php_bak
   cp /var/www/html/asterCC/app/controllers/logouts_controller.php logouts_controller.php_bak
   ```
2. Descarga el parche desde `http://download2.astercc.org/astercc_login_security_patch.tar.gz` y verifica su integridad (`md5sum`).
3. Reemplaza `login_controller.php` y `logouts_controller.php` con los del paquete, según tu versión.
4. Agrega una "sal" (salt) en `/etc/astercc.conf` para dificultar el uso indebido del endpoint de cambio de contraseña:
   ```ini
   [system]
   changelogin_pnum_salt=1234567890abcdefghizklABCD
   ```
5. **Después del parche:** revisa datos de equipos, cuentas, agentes y extensiones en busca de registros sospechosos, y rota contraseñas y cadenas de registro que puedan haberse filtrado.
6. Si el sistema no usa ciertos módulos (BPO, WeChat), elimina o renombra los controladores correspondientes para reducir superficie de ataque — contacta a `support@astercc.org` si necesitas la lista completa vigente para tu versión.
7. Endurecimiento adicional recomendado:
   - Restringe la IP de registro permitida por extensión (plantilla de PBX).
   - Restringe el acceso al sistema por rango de IP (Sistema → Configuración avanzada).
   - Filtra por país/región a nivel de firewall si tu operación es local (`ipset` + `iptables`/`firewalld`).
   - Bloquea en Nginx requests con palabras clave SQL sospechosas.

## Versiones principales

| Versión | Punto destacado |
|---|---|
| **4.2** (más reciente) | Adaptación completa a Rocky Linux 9 + PHP 7.4, cifrado de tablas InnoDB en MariaDB, salt de seguridad para login |
| **4.1** | Soporte inicial de Rocky Linux 9 y PHP 7.4, redis con contraseña, bloqueo de cuenta tras intentos fallidos de login, importación de `.xlsx` |
| **3.2** | Ver detalle en el archivo original si necesitas esta versión específica |
| **2.6 / 2.4 / 2.3** | Iteraciones sobre el módulo de campañas y reportes |
| **2.0** | Migración a CentOS 6.5, monitoreo de llamadas y estado de agentes en tiempo real, facturación de DID, mejoras en marcación automática |
| **1.1 – 1.2** | Versiones fundacionales de la línea comercial |

!!! tip
    El historial línea por línea de cada versión (23 changelogs individuales) está disponible en `raw/zh/change_log/` y `raw/en/change_log/` si necesitas el detalle exacto de una versión específica — esta página resume solo los hitos más relevantes para no duplicar contenido de bajo valor de consulta.

---

## Fuentes

- `raw/zh/change_log/astercc_login_security_patch.txt`
- `raw/zh/change_log/astercc-4.2_changelog.txt`
- `raw/zh/change_log/astercc-4.1_changelog.txt`
- `raw/zh/change_log/astercc-2.0_changelog.txt`