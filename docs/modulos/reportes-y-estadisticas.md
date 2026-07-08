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

Existen reportes equivalentes a nivel de **grupo de agentes** y de **llamadas entrantes/salientes detalladas** (servicio entrante, servicio saliente, resumen de salientes, detalle de IVR).

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
| Ver quién está conectado ahora | Información en tiempo real del sistema → Agentes/usuarios en línea |
| Intervenir en una llamada en curso | Información en tiempo real → Monitoreo de grupo de agentes |
| Consultar o enviar una factura | Financiero → Factura de sistema / equipo / usuario |

---

*Fuentes: `raw/zh/模块使用说明/报表和统计/坐席服务明细.txt`, `raw/zh/模块使用说明/财务统计/系统账单.txt`.*
