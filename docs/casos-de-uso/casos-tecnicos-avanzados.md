---
title: "Casos técnicos avanzados"
resumen: "IVR con reconocimiento de voz y conexión de troncal SIP con un operador móvil (IMS)."
seccion: "5.6 Casos técnicos avanzados"
tipo: guia
nivel: avanzado
roles: [administrador, desarrollador]
fuente: zh
obsoleto: false
relacionados: [pbx-y-telefonia]
---

# Casos técnicos avanzados

## Qué es

Dos casos técnicos que van más allá de la configuración estándar de PBX: enrutar un IVR usando **reconocimiento de voz** en vez de tonos DTMF, y conectar un troncal SIP con un operador de telefonía móvil vía **IMS**.

## Cómo se usa

### IVR con reconocimiento de voz (ASR)

En vez de pedir al cliente que presione una tecla, el IVR puede pedirle que **diga** la opción y enrutar según lo reconocido:

1. Crea el flujo de [IVR](../modulos/pbx-ivr.md) con sus parámetros básicos.
2. Agrega, en orden: una acción de **respuesta**, luego una de **aviso de voz** (pidiendo al cliente que diga la opción — ej. *"diga el área con la que desea comunicarse: consultas de producto, servicio al cliente o quejas"*), y luego una acción de **reconocimiento de voz**.
3. En la acción de reconocimiento, configura:
   - **Duración máxima:** tiempo máximo que el sistema graba antes de intentar reconocer.
   - **Silencio máximo:** si detecta silencio en la línea por N segundos, da por terminada la grabación y empieza a reconocer.
   - El resultado del reconocimiento se guarda en una **variable** (ej. `ASR1`).
4. Da de alta las colas y grupos de agentes correspondientes a cada opción de enrutamiento.
5. Configura el **destino** del nodo de IVR usando la variable de reconocimiento como condición — por ejemplo, si `ASR1` = "quejas", enruta a la cola de quejas.

!!! tip
    Igual que en el enrutamiento por variables de las colas (ver [4.1](../modulos/pbx-y-telefonia.md#colas)), el mecanismo de fondo es el mismo: una variable de sistema que se compara contra un valor esperado para decidir el destino.

### Troncal SIP con operador móvil vía IMS

!!! warning "Puede estar desactualizado"
    Este caso documenta parámetros específicos de un operador (China Mobile) vigentes en 2018. Los datos de conexión (dominio, servidor, formato de usuario) deben confirmarse con el operador actual antes de usarlos — se incluyen solo como ejemplo de la estructura general de este tipo de integración.

Al conectar un troncal SIP directamente con la red de un operador móvil (servicio tipo IMS), generalmente se necesita:

- Una **línea dedicada** hacia la red del operador (acceso a su red interna).
- Datos de registro: usuario (con formato específico del operador, ej. `+<código país><número>@<dominio del operador>`), contraseña, dominio de registro, y servidor de salida.
- Configurar el modo DTMF como **inband** en el troncal — necesario en varios operadores de este tipo para evitar problemas con tonos DTMF (ver también [Solución de problemas](../troubleshooting/index.md)).
- Para las llamadas entrantes, se agrega una **cadena de registro** en el troncal con el formato `<usuario>@<dominio>:<contraseña>:<usuario>@<dominio>@<servidor>:<puerto>/<DID>` — el segmento final indica a qué DID llegan las llamadas entrantes de ese troncal.
- Un error `484` durante las pruebas suele resolverse **deshabilitando el soporte de video** en el troncal.

## Referencia rápida

| Caso | Punto de partida |
|---|---|
| IVR con voz | Acción "reconocimiento de voz" dentro del nodo de IVR |
| Troncal con operador móvil | Configuración de troncal + `dtmfmode=inband` |

---

## Fuentes

- `raw/zh/用途和案例/ivr语音识别配置示例.txt`
- `raw/zh/用途和案例/中国移动ims对接.txt`