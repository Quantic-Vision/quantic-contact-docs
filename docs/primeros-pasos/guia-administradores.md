---
title: "Guía rápida para administradores"
resumen: "De cero a la primera llamada funcionando: cuentas, extensiones, troncal, ruta entrante y grupo de agentes."
seccion: "3.1 Guía rápida para administradores"
tipo: tutorial
nivel: basico
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [configuracion-post-instalacion, guia-agentes, pbx-y-telefonia, cuentas-equipos-permisos]
---

# Guía rápida para administradores

## Qué es

Esta guía cubre el camino más corto entre una instalación recién inicializada y la primera llamada funcionando: crear cuentas y extensiones en lote, agrupar agentes en un grupo con cola, configurar un softphone, dar de alta un troncal, y enrutar una llamada entrante hacia la cola.

## Cómo se usa

### 1. Crear cuentas, extensiones y agentes en lote

1. Ve a **Cuentas y permisos → Configuración rápida**.
2. Esta pantalla genera en una sola operación cuentas de sistema, extensiones y agentes. Define:
   - **Cantidad a generar** (ej. 5).
   - **Prefijo de usuario** (ej. `astercc`).
   - **Extensión inicial** (ej. `5000` — las siguientes se numeran consecutivamente).
   - **Número de agente inicial** (ej. `5000`).
   - **Longitud de contraseña** (ej. 7 caracteres).
   - **Prefijo de contraseña** (ej. `temp12` — si el prefijo y la longitud coinciden, todas las cuentas comparten la misma contraseña).
3. Haz clic en **Vista previa** para revisar lo que se va a crear, ajusta si hace falta, y luego en **Guardar**.
4. El sistema pregunta si quieres exportar el resultado a CSV — útil para no perder las contraseñas generadas.
5. Aparecerá una barra de **recarga** en la parte superior: haz clic en ella para que los cambios tomen efecto.

### 2. Crear un grupo de agentes (cola)

Un agente necesita pertenecer a un [grupo de agentes](../glosario.md#cola-grupo-de-agentes) para poder trabajar.

1. Ve a **Cuentas y permisos → Gestión de grupos de agentes** y haz clic en **Agregar**.
2. Agrega los agentes creados en el paso anterior al grupo (puedes usar "Seleccionar todos").
3. Designa a uno de los agentes como **administrador del grupo** (jefe de equipo).
4. Al guardar, el sistema pregunta si quieres crear automáticamente una cola asociada — acepta. Un grupo de agentes y su cola tienen relación uno a uno.
5. Recarga el sistema (barra de recarga) para aplicar el cambio.

### 3. Configurar un softphone

1. Descarga un softphone compatible con SIP 2.0 (X-Lite, Zoiper o eyeBeam).
2. Configura la cuenta SIP usando el formato `<equipo>-<extensión>` como usuario (ej. `astercc-5000`, **no** `5000` solo), y la contraseña generada en el paso 1.
3. Puedes confirmar usuario/contraseña de registro en **Módulos → PBX → Gestión de extensiones**.
4. Si el registro falla, los códigos de error más comunes son:
   - **403 Forbidden:** usuario o contraseña incorrectos — confirma el formato `equipo-extensión`.
   - **408 Request Timeout:** el softphone no encuentra el servidor — revisa firewall y red.

### 4. Configurar un troncal

1. Ve a **PBX → Troncales** y haz clic en **Agregar**.
2. Completa los datos según lo que te dé tu proveedor SIP (ITSP). Configuración típica por usuario/contraseña:
   ```
   username=<usuario>
   fromuser=<usuario>
   host=<ip-del-troncal>
   fromdomain=<ip-del-troncal>
   secret=<contraseña>
   port=5060
   ```
   Configuración típica por IP (sin registro):
   ```
   host=<ip-del-troncal>
   fromdomain=<ip-del-troncal>
   port=5060
   ```
3. Al guardar, si el equipo no tiene un troncal saliente por defecto, el sistema pregunta si quieres asignar este troncal como predeterminado para las llamadas salientes del equipo.
4. Recarga el sistema. Si todo está bien, la columna **Estado** del troncal se muestra en verde.
5. Prueba una llamada saliente desde el softphone. Códigos de error comunes:
   - **486 Not Acceptable Here:** códec de voz incompatible entre el troncal y el softphone (revisa soporte de g729 si aplica).
   - **603 Declined:** normalmente autenticación del troncal — revisa si el troncal exige verificación del número que llama.

### 5. Configurar una ruta entrante

1. Ve a **PBX avanzado → Rutas entrantes** y haz clic en **Agregar**.
2. Define el destino de transferencia (por ejemplo, transferir a la cola creada en el paso 2) y un nombre descriptivo para esa transferencia.
3. Guarda y recarga. A partir de ahora, las llamadas que entren por el DID configurado se enrutan a esa cola.

### 6. Instalar un módulo de negocio

1. Inicia sesión como administrador y entra a **Sistema → Gestión de módulos**.
2. Elige el módulo que necesites (por ejemplo, Atención al cliente) y haz clic en **Instalar**.
3. Confirma la instalación; al terminar, haz clic en **Finalizar**.
4. Configura el módulo (por ejemplo, en Atención al cliente: crea una tarea y asígnale el grupo de agentes del paso 2).
5. En **Cuentas y permisos → Grupos de agentes**, confirma que el grupo tenga vinculada la aplicación de negocio recién configurada como su flujo por defecto para llamadas entrantes/salientes.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear cuentas/extensiones/agentes en lote | Cuentas y permisos → Configuración rápida |
| Crear grupo de agentes (cola) | Cuentas y permisos → Gestión de grupos de agentes |
| Configurar troncal | PBX → Troncales |
| Configurar ruta entrante | PBX avanzado → Rutas entrantes |
| Instalar módulo de negocio | Sistema → Gestión de módulos |
| Formato de usuario SIP | `equipo-extensión` (ej. `astercc-5000`) |

---

*Fuente: `raw/zh/新手上路/快速配置手册.txt`.*
