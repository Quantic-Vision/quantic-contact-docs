---
title: "Marcación predictiva"
resumen: "Cómo activar el marcador predictivo sobre una tarea de campaña y monitorear la sesión en vivo."
seccion: "5.5 Marcación predictiva"
tipo: guia
nivel: avanzado
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [marcador-y-campanas, reportes-y-estadisticas]
---

# Marcación predictiva

## Qué es

El marcador predictivo marca automáticamente por el agente, aplicando una estrategia que intenta que, en cuanto un cliente contesta, siempre haya un agente libre esperando — sin que el agente pierda tiempo buscando números o esperando que timbre.

## Cómo se usa

### 1. Crear la tarea de campaña y su lista de marcación

Sigue [4.2 Marcador y campañas](../modulos/marcador-y-campanas.md) para crear la tarea. Si no se especifica un paquete de clientes existente, el sistema crea automáticamente uno con el mismo nombre de la tarea. Importa los números a marcar según [Atención al cliente](../modulos/atencion-cliente-mensajeria-ecommerce.md) → carga de datos, o usando la función de importación de datos del módulo de campañas.

### 2. Iniciar la sesión de marcado

El jefe de grupo entra al **marcador**, donde ve la tarea con su cantidad de **clientes pendientes de marcar**, y elige una de dos estrategias:

| Estrategia | Cómo calcula cuántas llamadas lanzar |
|---|---|
| Por concurrencia máxima | Un número fijo de llamadas simultáneas para la tarea (ej. 50: si ya hay 30 en curso y 10 timbrando, lanza 10 más para completar 50) |
| Por porcentaje de agentes disponibles | Agentes libres × porcentaje configurado, menos las llamadas que ya están timbrando (ej. 40 agentes libres × 120% − 10 timbrando = 36 nuevas llamadas) |

Al hacer clic en **iniciar**, el marcador comienza a marcar automáticamente los números de la lista.

### 3. Monitorear la sesión en vivo

Mientras la campaña corre, el panel del marcador muestra en tiempo real:

- **Timbrando:** clientes cuya llamada está en curso, esperando respuesta.
- **En conversación:** clientes ya conectados con un agente.
- **Esperando agente:** clientes que contestaron pero aún no hay agente libre asignado — este número debe mantenerse lo más bajo posible; si crece mucho, hay que bajar la agresividad de la estrategia de marcado.
- Duración de timbrado, tiempo de espera, y tiempos entre respuesta del cliente y asignación al agente.

### 4. Recuperar números no completados

Si la lista de marcación se agota antes de terminar la tarea, se puede **recuperar** clientes desde el paquete completo de la tarea de vuelta a la lista de marcación, para reintentarlos.

### 5. Cerrar y revisar resultados

Al finalizar, consulta en [4.8 Reportes](../modulos/reportes-y-estadisticas.md) el desempeño de agente y de grupo para esa sesión — volumen marcado, tasa de contactación, y tiempos promedio.

## Referencia rápida

| Parámetro | Se configura en |
|---|---|
| Límite de concurrencia por equipo | Marcador → Configuración del marcador |
| Estrategia de marcado (concurrencia / % agentes) | Panel del marcador, al iniciar la sesión |
| Destino al contestar (cola / IVR) | Configuración avanzada de predial, dentro de la tarea de campaña |

---

*Fuente: `raw/zh/用途和案例/如何为在外呼任务中使用预拨号功能.txt`.*
