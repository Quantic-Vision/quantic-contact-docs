---
title: "Marketing outbound / televentas"
resumen: "Caso de uso completo: de cero a una campaña de televenta funcionando, con reportes de cierre."
seccion: "5.2 Marketing outbound / televentas"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [marcador-y-campanas, reportes-y-estadisticas]
---

# Marketing outbound / televentas

## Qué es

Caso de uso de referencia para montar una operación de televenta desde cero: extensión, agente, softphone, paquete de clientes, tarea de campaña, y cómo se ve el trabajo diario del agente hasta llegar a los reportes de cierre.

## Cómo se usa

### 1. Preparar extensión, agente y softphone

Sigue los pasos 1–3 de la [Guía rápida para administradores](../primeros-pasos/guia-administradores.md): crear la extensión, el agente, y configurar el softphone. Confirma en la lista de extensiones que el estado muestre el retardo de conexión (a menor retardo, mejor calidad de audio).

### 2. Crear el paquete de clientes

En **Marketing outbound → Gestión de paquetes de clientes**, crea un [paquete de clientes](../glosario.md#paquete-de-clientes-para-marcacion-saliente) con el segmento a contactar. Cada paquete genera automáticamente su propia tabla de datos, separada de la tabla general — así el paquete no se ve afectado por cambios posteriores en la base general, y viceversa.

### 3. Definir los resultados de llamada

En **Marketing outbound → Gestión de resultados de llamada**, define las opciones que el agente podrá elegir tras cada llamada — típicamente separadas en resultados para llamadas contestadas (ej. "no coopera", "sin tiempo", "coopera", "número equivocado") y para no contestadas (ej. "apagado", "fuera de servicio", "no existe").

### 4. Crear la tarea de campaña

Sigue [4.2 Marcador y campañas](../modulos/marcador-y-campanas.md) para crear la tarea, apuntando al grupo de agentes y al paquete de clientes de los pasos anteriores.

### 5. Trabajo diario del agente

1. El agente inicia sesión y se conecta al grupo de trabajo saliente.
2. Selecciona la tarea de campaña en el panel lateral — se muestra el detalle de la tarea y la lista de clientes pendientes.
3. Al hacer doble clic en un cliente se abre su ficha con los campos configurados para ser visibles.
4. El agente marca (según el modo configurado: manual, preview o automático — ver [4.2](../modulos/marcador-y-campanas.md#2-elegir-el-modo-de-marcacion)).
5. Al colgar, registra el **resultado de la llamada**, el **estado de procesamiento**, y notas adicionales — el sistema puede exigir que haya habido conexión real antes de permitir guardar (configurable en la tarea).

### 6. Ver los reportes de cierre

Al terminar la sesión de trabajo, en **Reportes y estadísticas** se puede consultar, para la tarea o el periodo elegido:

| Indicador | Qué mide |
|---|---|
| Volumen de datos | Cuántos clientes se marcaron |
| Tasa de contactación | Clientes contestados ÷ volumen de datos |
| Tasa de éxito de marcación | Llamadas contestadas ÷ llamadas realizadas |
| Sin guardar por el agente | Llamadas donde no se registró resultado |
| En seguimiento / completados | Según el estado de procesamiento elegido por el agente |
| Aprobados en control de calidad | Cuántos casos pasaron la revisión de calidad |

## Referencia rápida

| Paso | Dónde |
|---|---|
| Extensión, agente, softphone | [Guía rápida para administradores](../primeros-pasos/guia-administradores.md) |
| Paquete de clientes | Marketing outbound → Gestión de paquetes de clientes |
| Resultados de llamada | Marketing outbound → Gestión de resultados de llamada |
| Tarea de campaña | [4.2 Marcador y campañas](../modulos/marcador-y-campanas.md) |
| Reportes de cierre | [4.8 Reportes, estadísticas y financiero](../modulos/reportes-y-estadisticas.md) |

---

*Fuente: `raw/zh/用途和案例/为企业建立一个外呼呼叫中心用于管理销售.txt`.*
