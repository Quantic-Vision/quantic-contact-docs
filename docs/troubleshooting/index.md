---
title: "Solución de problemas"
resumen: "Errores específicos y su solución, indexados por síntoma — para preguntas conceptuales, ve a FAQ."
seccion: "9. Solución de problemas"
tipo: troubleshooting
nivel: intermedio
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: []
---

# Solución de problemas

Esta sección resuelve **síntomas y errores concretos**. Si tu pregunta es conceptual, ve a [Preguntas frecuentes](../faq/index.md).

## "can not found license file" al iniciar los demonios de AsterCC

Es solo un aviso, no un error — el sistema sigue funcionando con la licencia de prueba por defecto. Ver detalle en [Licencias y errores comunes de inicio](../instalacion/licencias-y-errores-comunes.md).

## Error al iniciar sesión con `admin`/`admin` justo después de instalar

Revisa el valor de `error_reporting` en `php.ini`:

```ini
error_reporting = E_ALL & ~E_DEPRECATED
```

Reinicia el servicio de PHP tras el cambio:

```bash
service php-fpm restart
```

## No se puede guardar una extensión o un agente nuevo

Confirma que existe al menos un **equipo** creado en el sistema — sin equipo, el sistema no permite guardar extensiones ni agentes.

## La extensión marca normal, pero con marcación predictiva el número destino no timbra

Síntoma típico de un troncal que exige **verificación del número que llama** (caller ID). Dos soluciones posibles:

1. **Configura el número que llama en la tarea de campaña:** edítala, entra a configuración avanzada, y define el número.
2. **Fuerza el número saliente en el troncal:** edítalo, entra a configuración avanzada, y activa "forzar uso de número que llama".

## Un cliente navega mal el IVR (no reconoce las teclas)

Revisa el modo DTMF del troncal — ver [FAQ: ¿Cómo elijo el modo DTMF correcto?](../faq/pbx-y-telefonia.md#como-elijo-el-modo-dtmf-correcto). Si usas `inband`, confirma que el códec de voz sea `ulaw` o `alaw`.

## Error `484` al registrar un troncal con un operador móvil (IMS)

Deshabilita el soporte de video en la configuración del troncal. Ver [Casos técnicos avanzados](../casos-de-uso/casos-tecnicos-avanzados.md#troncal-sip-con-operador-movil-via-ims).

## Problemas de tres vías / conferencia que cuelga sola

Confirma que Asterisk tiene cargado el módulo `app_meetme.so` (usado para salas de conferencia).

## Clic para llamar falla (click-to-call)

Dos causas comunes:
- Confirma que el modo clúster **no** está activado en `astercc.conf` si no lo estás usando intencionalmente.
- Confirma que el proceso `astcc_dialer` está corriendo.

## Error de mysqldump al hacer backup de la base de datos

Si al ejecutar `mysqldump -uroot -p astercc10` aparece el error:

```
mysqldump: Got error: 2002: Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```

El proceso de MySQL no está escuchando por el socket local esperado. Usa la conexión por TCP a `127.0.0.1` en su lugar:

```bash
mysqldump -h127.0.0.1 -uroot -p astercc10 | gzip > astercc_db.sql.gz
```

Ver el procedimiento completo de respaldo en [Casos técnicos avanzados](../casos-de-uso/casos-tecnicos-avanzados.md#respaldo-del-sistema-backup).

## Referencia rápida — dónde revisar cada síntoma

| Síntoma | Revisar |
|---|---|
| Licencia / arranque de demonios | [Licencias y errores comunes de inicio](../instalacion/licencias-y-errores-comunes.md) |
| Login admin falla tras instalar | `php.ini` → `error_reporting` |
| No se puede guardar extensión/agente | Existencia de un equipo |
| Predictivo no timbra al destino | Configuración de número que llama (tarea o troncal) |
| IVR no reconoce teclas | Modo DTMF del troncal |
| Conferencia se cuelga sola | Módulo `app_meetme.so` cargado en Asterisk |
| Click-to-call falla | Modo clúster / proceso `astcc_dialer` |
| `mysqldump` no conecta al hacer backup | Usar `-h127.0.0.1` en vez de socket local |

---

## Fuentes

- `raw/zh/常见问题及解答/安装完毕后使用默认的admin账户登录astercc时总是显示错误.txt`
- `raw/zh/常见问题及解答/为什么无法保存分机_坐席.txt`
- `raw/zh/常见问题及解答/分机呼叫正常_使用预拨号时目标号码不振铃.txt`
- `raw/zh/常见问题及解答.txt`
- `raw/en/why_i_get_can_not_found_license_file_when_start_astercc_daemons.txt`
- `raw/en/use_case/how_to_perform_system_backup.txt`