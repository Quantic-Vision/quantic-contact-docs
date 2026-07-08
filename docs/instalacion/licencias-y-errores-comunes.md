---
title: "Licencias y errores comunes de inicio"
resumen: "Cómo funciona la licencia por defecto de AsterCC y qué significa el aviso de licencia no encontrada al iniciar."
seccion: "2.5 Licencias y errores comunes de inicio"
tipo: troubleshooting
nivel: intermedio
roles: [administrador]
fuente: zh+en
obsoleto: false
relacionados: [descarga-e-instalacion, configuracion-post-instalacion]
---

# Licencias y errores comunes de inicio

## Qué es

AsterCC funciona con un esquema de licencia por número de agentes. Si no se ha cargado una licencia comercial, el sistema arranca igualmente con una **licencia por defecto de prueba, limitada a un número reducido de agentes** (la instalación estándar trae, por ejemplo, una licencia de prueba de 5 agentes).

## Cómo se usa

### "can not found license file" al iniciar los demonios de AsterCC

Este mensaje aparece en los logs al iniciar los procesos (`asterccdaemons`) cuando el sistema no encuentra un archivo de licencia comercial.

**Esto es solo un aviso, no un error.** Si no se encuentra ningún archivo de licencia, AsterCC sigue funcionando normalmente usando la **licencia por defecto** (limitada a un número reducido de agentes, típicamente 4). No es necesario tomar ninguna acción salvo que necesites más agentes de los que permite la licencia por defecto — en ese caso, corresponde cargar una licencia comercial válida.

## Referencia rápida

| Situación | Qué significa | Acción |
|---|---|---|
| `can not found license file` en el log de arranque | No hay licencia comercial cargada | Ninguna, salvo que necesites más agentes — el sistema usa la licencia de prueba por defecto |
| Sistema recién instalado | Trae licencia de prueba limitada (ej. 5 agentes) | Contactar al proveedor para licencia comercial si se necesita más capacidad |

---

*Fuentes: `raw/en/why_i_get_can_not_found_license_file_when_start_astercc_daemons.txt`, `raw/zh/新手上路/快速配置手册.txt`.*
