---
title: "PBX y telefonía"
resumen: "Extensiones, troncales, DID, colas, rutas, IVR y demás configuración de la central telefónica."
seccion: "4.1 PBX y telefonía"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [cuentas-equipos-permisos, guia-administradores, marcador-y-campanas]
---

# PBX y telefonía

## Qué es

Este grupo de módulos configura la central telefónica (PBX) propiamente dicha: cómo se conectan los teléfonos al sistema (extensiones), cómo el sistema se conecta al exterior (troncales), y cómo se enruta cada llamada entre ambos mundos (rutas, colas, IVR).

## Cómo se usa

### Extensiones (gestión de dispositivos)

Cada teléfono o softphone que se conecta al sistema es una **extensión**. AsterCC soporta cuatro tipos: **SIP, IAX2, MGCP** (todos por red) y **DAHDI** (línea física), además de las **extensiones externas** (un número de teléfono normal usado como si fuera una extensión — solo puede recibir llamadas del sistema, no puede originarlas).

Campos clave al crear una extensión:

| Campo | Qué define |
|---|---|
| Número de interno | Número de marcación interna — único dentro del equipo |
| Cuenta de registro | Generada automáticamente como `equipo-interno` (ej. `astercc-5000`) — es el usuario que se configura en el softphone |
| Contraseña de registro | Contraseña del dispositivo |
| Tipo de extensión | SIP / IAX2 / MGCP / DAHDI / externa |
| Plantilla | Permite aplicar parámetros predefinidos a varias extensiones a la vez |
| Permitir llamadas salientes | Si la extensión puede marcar fuera del sistema |
| Troncal de salida | Fuerza qué troncal usa esta extensión al llamar afuera (opcional) |
| Buzón de voz | Activación, contraseña y correo de destino |
| Grabación | Si esta extensión graba sus llamadas |
| Lista blanca / negra | Restringe qué números pueden o no pueden llamar a esta extensión |

Tras guardar, aparece una barra de **recarga** — es necesaria para que el cambio tome efecto.

### Troncales y grupos de troncales

Un **troncal** es la conexión del sistema hacia el exterior (proveedor SIP, gateway, tarjeta E1/T1 o analógica). Los troncales se agrupan en **grupos de troncales**, que permiten:

- Definir reglas de enrutamiento de salida por grupo.
- Elegir estrategia de uso: **secuencial** (por prioridad), **rotativa**, o **aleatoria**.
- **Deshabilitar automáticamente** un troncal tras varios fallos consecutivos, avisando al administrador por correo — así el grupo sigue funcionando con los troncales restantes.

### DID y rutas entrantes/salientes

- **DID (número de entrada):** se agrupan en **grupos de DID** para reutilizar reglas de enrutamiento entre varios números.
- **Ruta saliente:** decide qué grupo de troncales usa una llamada según prefijo o longitud del número marcado; puede agregar o quitar prefijos antes de enviar la llamada al troncal.
- **Ruta entrante:** enruta por DID, por troncal, por número que llama, o combinaciones de las anteriores — incluyendo enrutar según la **ubicación geográfica** del número que llama (útil cuando distintos equipos de agentes atienden distintas regiones).

### Colas

La cola es el corazón de la distribución de llamadas entrantes. Un [grupo de agentes](../glosario.md#cola-grupo-de-agentes) sin una cola asociada no sirve de nada — al guardar un grupo sin cola, el sistema ofrece crear una automáticamente.

Parámetros más relevantes de una cola:

| Campo | Qué define |
|---|---|
| Estrategia de timbrado | Más tiempo sin recibir llamada, menos llamadas atendidas, aleatorio, rotativo por memoria, rotativo por configuración |
| Anuncio de número de agente | Antes o después del mensaje de bienvenida al agente |
| Música en espera | Personalizada, por defecto, o tono de llamada |
| Destino de fallo | A dónde va la llamada si se agota el tiempo máximo de espera (colgar, IVR, otra cola, extensión, grupo de timbrado, buzón de voz, tono ocupado) |
| Tiempo de espera del agente | Segundos que timbra antes de pasar al siguiente agente |
| Intervalo de reintento | Espera mínima antes de volver a ofrecer la llamada a un agente |
| Tiempo máximo de espera | Tras el cual se aplica el destino de fallo |
| Permitir cola vacía | Si los clientes pueden esperar aunque no haya ningún agente conectado |
| Autocompletado | Si se asignan varias llamadas en espera a varios agentes libres simultáneamente, o una por una |
| Condición de entrada automática | Enruta según variables de sistema (por ejemplo, el idioma elegido en un IVR previo) |
| Multipartita | Si permite conferencia dentro de la cola |
| Tecla de función | Permite que el cliente en espera salga de la cola hacia un buzón de voz o un IVR con una tecla |

### IVR (menú de voz)

Para armar un IVR básico:

1. Sube los archivos de audio en **PBX avanzado → Gestión de archivos de voz** (formato 8000 Hz, 16 bits, mono).
2. Da de alta la voz de llamada en **PBX avanzado → Gestión de voz de llamada**, asociando el archivo al idioma correspondiente.
3. Crea el IVR en **PBX avanzado → Telefonía por computadora (IVR)**.
4. Configura la **acción** — por ejemplo, "reproducir y capturar dígitos", indicando la voz a reproducir y cuántos dígitos esperar.
5. Configura el **destino** para cada posible entrada del usuario — puede apuntar a una cola, extensión, u otro nodo de IVR (permitiendo menús anidados).
6. Prueba marcando la extensión asignada al IVR y revisa el log de Asterisk si el sistema no reacciona como se espera.

### Otras funciones de PBX avanzado

- **Grupos de timbrado:** timbran varias extensiones a la vez o en secuencia.
- **Salas de conferencia**, con opción de grabación.
- **Restricción de número saliente**, para evitar llamadas no autorizadas.
- **Lista blanca / negra de llamadas entrantes.**
- **Horarios de trabajo** (y paquetes de horarios), usados por rutas y colas para comportarse distinto según el horario.
- **Plantillas de PBX**, para aplicar configuración estándar a extensiones o troncales en lote.
- **Gestión de tarjetas** (E1/T1, analógicas) para conexiones físicas.

## Referencia rápida

| Tarea | Dónde configurarlo |
|---|---|
| Extensiones | PBX → Gestión de extensiones |
| Troncales / grupos de troncales | PBX → Troncales |
| DID / grupos de DID | PBX avanzado → DID |
| Rutas entrantes / salientes | PBX avanzado → Rutas |
| Colas | PBX avanzado → Gestión de colas |
| IVR | PBX avanzado → Telefonía por computadora |
| Archivos y voces de llamada | PBX avanzado → Gestión de archivos de voz / voz de llamada |
| Salas de conferencia | PBX avanzado → Salas de conferencia |
| Horarios de trabajo | PBX avanzado → Horarios de trabajo |

---

*Fuentes: `raw/zh/模块使用说明/pbx管理/*.txt`, `raw/zh/模块使用说明/pbx高级管理/*.txt`, `raw/zh/模块使用说明/ivr/设定一个语音菜单ivr.txt`.*
