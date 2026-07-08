---
title: "Reportes, estadísticas y financiero"
resumen: "Reportes de desempeño por agente/grupo, monitoreo en tiempo real y facturación."
seccion: "4.8 Reportes, estadísticas y financiero"
tipo: referencia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [plataforma-del-agente, tarifas-y-facturacion]
---

# Reportes, estadísticas y financiero

## Qué es

Este grupo de módulos cubre tres necesidades distintas: **reportes históricos** de desempeño (por agente, grupo o llamada), **monitoreo en tiempo real** del estado del sistema, y **facturación** (cuentas de sistema, equipo y usuario).

## Cómo se usa

### Reportes de desempeño

Disponibles por **equipo**, **grupo** o **agente**, y agregables por año, mes, semana, día u hora — exportables a Excel o CSV.

Indicadores más relevantes del reporte de desempeño de agente:

| Indicador | Qué mide |
|---|---|
| Llamadas entrantes atendidas / salientes conectadas | Volumen de trabajo |
| Duración total / promedio de llamada | Incluye entrantes y salientes |
| Tiempo promedio de gestión posterior (ACW) | Tiempo total de ACW ÷ número de llamadas gestionadas |
| Tiempo promedio de manejo | (Tiempo en llamada + tiempo de ACW) ÷ llamadas atendidas |
| Tiempo promedio de timbrado | Diferencia entre inicio y respuesta (o fin, si no contestó) |
| Cantidad y duración promedio de consultas, retenciones, conferencias, transferencias | Uso de funciones de llamada activa |
| Tiempo total conectado / en espera / en pausa | Desglosado incluso por motivo de pausa |
| Tasa de ocupación | (Timbrado + en llamada) ÷ tiempo conectado |
| Tasa de efectividad | (Timbrado + en llamada + ACW) ÷ (conectado − pausado) |
| Tasa de retención | Retenciones ÷ (entrantes + salientes atendidas) |

### Reporte de desempeño de grupo — niveles de servicio (SLA)

El reporte por **grupo de agentes** agrega, además de indicadores equivalentes a los de agente (tasa de contactación, duración promedio, ACW, consultas, conferencias, retenciones), los **niveles de servicio estándar de la industria** — el porcentaje de llamadas entrantes contestadas dentro de cierto umbral de tiempo:

| Indicador | Fórmula |
|---|---|
| Nivel de servicio ≤10s | Contestadas en ≤10s ÷ total de llamadas contestadas |
| Nivel de servicio ≤15s | Contestadas en ≤15s ÷ total |
| Nivel de servicio ≤20s | Contestadas en ≤20s ÷ total |
| Nivel de servicio ≤30s | Contestadas en ≤30s ÷ total |
| Nivel de servicio ≤60s | Contestadas en ≤60s ÷ total |
| Nivel de servicio >60s | Contestadas después de 60s ÷ total |

Otros indicadores exclusivos del reporte de grupo: **tasa de abandono** (clientes que colgaron esperando ÷ llamadas entrantes totales), **velocidad promedio de respuesta** ((timbrado + espera en cola) ÷ contestadas), y **tiempo promedio de manejo del grupo** ((tiempo en llamada + ACW) ÷ contestadas).

### Reportes con salida gráfica

Los reportes de **agente** y de **grupo de agentes** tienen una variante gráfica (barras o líneas), exportable a HTML, imagen o PDF (estos dos últimos no soportados en Internet Explorer). El sistema pre-calcula estos datos por la noche para no consumir recursos durante el horario de operación. Se puede agregar por: total, año, mes, semana, día, hora, o media hora.

!!! tip
    Cada indicador de tiempo tiene dos variantes: **(O)** cuenta el evento en el bloque de tiempo donde *comenzó*, y **(P)** lo cuenta en el bloque donde *estaba en curso*. Por ejemplo, una llamada de 10:59:48 a 11:00:32: para las 10:00, (O)=44s y (P)=12s; para las 11:00, (O)=0s y (P)=32s. Si se necesitan columnas que no vienen por defecto, se puede armar una **plantilla de columnas personalizada** (nombre solo en inglés) para reutilizar esa selección después.

### Reportes de llamadas detalladas

| Reporte | Qué muestra |
|---|---|
| Detalle de servicio entrante | Por llamada: agente, números, tiempo en IVR, tiempo en cola, timbrado, conversación, y el evento final que la cerró |
| Detalle de servicio saliente | Por llamada: agente, números, timbrado, conversación, evento final |
| Resumen de salientes | Por agente: cantidad de marcaciones, cantidad contestadas, duración total, costo — agregado, no línea por línea |
| Detalle de IVR | Por paso de IVR: duración, estado del IVR, número que llama/llamado, y cómo terminó (colgó, transfirió, error) |

### Estadísticas operativas del sistema

- **Estadísticas de importación de datos:** por rango de fecha, cuántos registros se importaron en total, y cuántos resultaron exitosos, fallidos o duplicados — complementa a [Marcador y campañas](marcador-y-campanas.md).
- **Estadísticas de datos del sistema:** serie de tiempo de cuentas conectadas, agentes conectados, agentes en check-in, clientes en conversación, clientes en espera, y pausas manuales — el nivel de agregación se ajusta automáticamente según el rango elegido (cada 5 minutos si es un solo día, por día si es un rango dentro del mismo año, por año si el rango cruza años).

### Monitoreo en tiempo real

- **Agentes en línea / usuarios en línea:** quién está conectado ahora mismo.
- **Uso de troncales en tiempo real:** cuántos canales de cada troncal están en uso.
- **Monitoreo de grupo de agentes:** estado en vivo de cada agente del grupo (libre, timbrando, en llamada, pausado) — con acciones directas como forzar check-out, forzar ocupado/libre, o [intervenir sobre una llamada activa](../glosario.md#monitoreo-intervencion-interrupcion-forzada-y-susurro).
- **Información del sistema:** estado general del servidor y de los servicios.

### Financiero

| Tipo de factura | Para quién |
|---|---|
| Factura de sistema | El operador — refleja el costo real de los troncales según la [tarifa de sistema](tarifas-y-facturacion.md#tarifa-de-sistema) |
| Factura de equipo | Cada equipo/cliente, según su tarifa de equipo |
| Factura de usuario | Cuentas individuales con facturación propia |

Las facturas se generan automáticamente de forma periódica y pueden consultarse en línea o enviarse por correo para respaldo o impresión. También existe un **resumen de gasto por agente** y un **log de movimientos financieros por agente**, útil para modelos donde se le paga al agente por desempeño o volumen.

## Referencia rápida

| Necesito | Dónde |
|---|---|
| Ver desempeño de un agente/grupo | Reportes y estadísticas → Servicio de agente / de grupo |
| Ver niveles de servicio (SLA) | Reportes y estadísticas → Servicio de grupo |
| Ver reportes gráficos | Reportes y estadísticas → Gráfico de agente / de grupo |
| Ver detalle de llamadas entrantes/salientes/IVR | Reportes y estadísticas → Detalle de servicio entrante / saliente / IVR |
| Ver quién está conectado ahora | Información en tiempo real del sistema → Agentes/usuarios en línea |
| Intervenir en una llamada en curso | Información en tiempo real → Monitoreo de grupo de agentes |
| Consultar o enviar una factura | Financiero → Factura de sistema / equipo / usuario |

---

## Fuentes

- `raw/zh/模块使用说明/报表和统计/坐席服务明细.txt`
- `raw/zh/模块使用说明/报表和统计/坐席组服务明细.txt`
- `raw/zh/模块使用说明/报表和统计/坐席图形报表.txt`
- `raw/zh/模块使用说明/报表和统计/坐席组图形报表.txt`
- `raw/zh/模块使用说明/报表和统计/呼入服务明细.txt`
- `raw/zh/模块使用说明/报表和统计/呼出服务明细.txt`
- `raw/zh/模块使用说明/报表和统计/呼出汇总.txt`
- `raw/zh/模块使用说明/报表和统计/ivr呼入服务明细.txt`
- `raw/zh/模块使用说明/报表和统计/导入数据统计.txt`
- `raw/zh/模块使用说明/报表和统计/系统数据统计.txt`
- `raw/zh/模块使用说明/财务统计/系统账单.txt`
- `raw/zh/模块使用说明/报表和统计.txt`