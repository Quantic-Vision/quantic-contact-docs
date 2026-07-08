---
title: "Cuentas, equipos y permisos"
resumen: "Estructura de equipos, cuentas de usuario, agentes, roles y permisos en AsterCC."
seccion: "4.3 Cuentas, equipos y permisos"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, guia-administradores]
---

# Cuentas, equipos y permisos

## Qué es

AsterCC organiza el acceso en cuatro niveles: **equipo** (la organización, útil en modo multiempresa), **cuenta** (usuario del sistema), **agente** (quien atiende llamadas) y **rol** (el conjunto de permisos que se asigna a cuentas o agentes).

## Cómo se usa

### Equipos

Un equipo representa una organización independiente dentro del mismo AsterCC — el mecanismo que permite el modo multiempresa. Cada equipo tiene sus propias cuentas, agentes, troncales y configuración, sin interferir con otros equipos del mismo sistema.

### Cuentas y agentes

- **Cuenta:** usuario que accede al sistema — puede ser de administración, operación, o estar asociado a un agente.
- **Agente:** unidad que atiende llamadas; se agrupa en [grupos de agentes](../glosario.md#cola-grupo-de-agentes) (colas).
- **Configuración rápida:** genera en lote cuentas, extensiones y agentes de una sola vez (ver [Guía rápida para administradores](../primeros-pasos/guia-administradores.md)).
- **Edición rápida:** permite modificar varias cuentas/agentes a la vez sin entrar uno por uno.
- **Finanzas de usuario:** gestión de saldo o costos asociados a una cuenta, cuando el sistema se usa en modo de facturación por cliente.

### Roles

Un **rol** es un conjunto de permisos reutilizable. El sistema trae dos roles por defecto:

| Rol | Permisos |
|---|---|
| Para agentes | Editable — se ajusta según necesidad |
| Para administradores | Todos los permisos, no editable |

Al crear un rol nuevo, se define:
- **Tipo de rol:** *usuario* (aplica a cuentas) o *agente* (aplica a agentes) — cada tipo solo puede operar sobre su propio tipo de objeto.
- **Configuración de permisos:** qué módulos puede ver, y dentro de cada uno, qué acciones puede hacer (agregar, editar, ver, eliminar, exportar).

### Permisos por módulo

La pantalla de **gestión de permisos** lista todos los módulos del sistema; solo el administrador de sistema puede modificarla. Cambios aquí afectan qué permisos están disponibles para asignar en la gestión de roles — es decir, primero se define el universo de permisos posibles por módulo, y luego los roles seleccionan un subconjunto de ese universo.

### Grupos de cuentas y grupos de agentes

- **Grupo de cuentas:** agrupa cuentas para asignarles un [grupo de troncales](pbx-y-telefonia.md#troncales-y-grupos-de-troncales) específico — por ejemplo, ventas puede marcar cualquier destino, mientras que otro grupo solo puede marcar localmente.
- **Grupo de agentes:** ver [4.1 PBX y telefonía](pbx-y-telefonia.md#colas) — cada grupo de agentes se corresponde uno a uno con una cola.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear cuentas/agentes en lote | Cuentas y permisos → Configuración rápida |
| Editar varias cuentas a la vez | Cuentas y permisos → Edición rápida |
| Gestionar equipos | Cuentas y permisos → Gestión de equipos |
| Gestionar roles | Cuentas y permisos → Gestión de roles |
| Definir permisos por módulo | Cuentas y permisos → Gestión de permisos (solo admin de sistema) |
| Gestionar grupos de agentes | Cuentas y permisos → Gestión de grupos de agentes |

---

*Fuentes: `raw/zh/模块使用说明/账户和权限管理/角色管理.txt`, `raw/zh/模块使用说明/账户和权限管理/权限管理.txt`.*
