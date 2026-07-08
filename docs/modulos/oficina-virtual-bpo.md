---
title: "Oficina virtual / BPO"
resumen: "Cómo un mismo grupo de agentes atiende a varias empresas cliente manteniendo sus datos y conocimiento aislados."
seccion: "4.9 Oficina virtual / BPO"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia, cuentas-equipos-permisos, oficina-virtual]
---

# Oficina virtual / BPO

## Qué es

Este módulo permite que un mismo equipo de agentes atienda, de forma indistinta, las llamadas de **varias empresas cliente** ("usuarios virtuales"), manteniendo la información, el conocimiento y las reglas de negocio de cada una completamente separadas. Es el mecanismo típico para ofrecer servicios de call center tercerizado (BPO) o de oficina virtual.

## Cómo se usa

### Caso de referencia

Una empresa A opera el call center para tres empresas clientes (B, C y D). Cada una tiene su propio número de atención. Cuando un cliente llama a B, la llamada se desvía hacia el sistema de A; A identifica —por el DID que recibió la llamada— que se trata de un cliente de B, y muestra al agente la pantalla, el saludo y la base de conocimiento correspondientes a B, sin que el agente necesite saber de memoria el negocio de cada empresa cliente.

### 1. Crear la cola y el grupo de agentes

Igual que en cualquier otro flujo entrante (ver [4.1 PBX y telefonía](pbx-y-telefonia.md#colas)): se crea una cola y un grupo de agentes que la atienda.

### 2. Crear el DID que identifica a cada usuario virtual

Cada empresa cliente (usuario virtual) recibe su propio DID, para que el sistema pueda distinguir de cuál empresa proviene cada llamada entrante.

### 3. Dar de alta el usuario virtual (empresa cliente)

En **Oficina virtual → Gestión de usuarios entrantes**, cada usuario virtual define:

| Campo | Qué define |
|---|---|
| Nombre del usuario virtual | Identifica a la empresa cliente |
| Enlace de pantalla del agente | Página que se muestra al agente cuando entra una llamada de este usuario |
| Enlace de administración | Página de gestión del negocio de este usuario virtual |
| Encuesta asociada | Si esta empresa cliente requiere encuesta |
| Grupo de agentes | Qué grupo atiende a este usuario virtual |
| Descripción del negocio | Notas para orientar al agente |
| Saludo | Frase de apertura que el agente debe usar al contestar |
| IPs de confianza | Requeridas si un sistema externo va a invocar eventos de este call center |

Un mismo usuario virtual puede tener **distintos enlaces de pantalla por grupo de agentes** — útil si ese negocio, a su vez, se subdivide en líneas (ej. soporte técnico, verificación, comercial) enrutadas por IVR a distintos grupos.

### 4. Base de conocimiento por usuario virtual

Se organiza en categorías de uno o dos niveles (ej. Categoría → Subcategoría → Artículo), igual que en [4.6 Base de conocimiento](base-conocimiento-work-orders.md#base-de-conocimiento), pero acotada al usuario virtual correspondiente — así el agente solo ve el conocimiento relevante para la empresa que está atendiendo en ese momento.

### 5. Que el agente entre directo a la pantalla de oficina virtual (opcional)

Para que un grupo de agentes, al iniciar sesión, entre directamente a la vista de oficina virtual (en vez de la vista por defecto del grupo):

1. Edita el grupo de agentes y activa "Mostrar página de oficina virtual por defecto".
2. En el usuario virtual, agrega el enlace de grupo y activa "Mostrar este enlace en el menú de configuración de la plataforma del agente" — así el agente puede acceder manualmente al negocio de esa empresa cliente en cualquier momento, no solo cuando recibe una llamada.

### Cuentas BPO

Cuando terceros (las propias empresas B, C, D del ejemplo) necesitan ver sus propios reportes y tareas sin acceder al resto del sistema, se les crea una **cuenta BPO**:

- Se define a qué **tareas de campaña** y a qué **usuarios virtuales (oficina virtual)** tiene acceso esa cuenta.
- Se le asigna un **rol** que controla qué puede ver y hacer.
- Las cuentas BPO inician sesión desde una URL separada (`<servidor>/bpologin/`), distinta del login administrativo normal.

## Referencia rápida

| Tarea | Dónde |
|---|---|
| Crear usuario virtual (empresa cliente) | Oficina virtual → Gestión de usuarios entrantes |
| Configurar enlaces por grupo de agentes | Dentro del usuario virtual → Enlaces de grupo |
| Base de conocimiento por usuario virtual | Oficina virtual → Base de conocimiento / Categorías |
| Crear cuenta BPO para el cliente final | BPO → Gestión de cuentas BPO |
| Login de cuentas BPO | `<servidor>/bpologin/` |

---

*Fuentes: `raw/zh/用途和案例/为客户提供虚拟呼叫中心服务.txt`, `raw/zh/模块使用说明/bpo/bpo帐号管理.txt`.*
