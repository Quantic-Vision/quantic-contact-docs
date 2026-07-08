---
title: "Oficina virtual"
resumen: "Caso de uso completo: un equipo de agentes atendiendo a varias empresas cliente con datos aislados."
seccion: "5.4 Oficina virtual"
tipo: guia
nivel: intermedio
roles: [administrador]
fuente: zh
obsoleto: false
relacionados: [oficina-virtual-bpo, pbx-y-telefonia]
---

# Oficina virtual

## Qué es

Escenario: la empresa A opera el call center para tres empresas clientes (B, C y D), cada una con su propio número de atención. El objetivo es que cualquier agente disponible pueda atender a un cliente de cualquiera de las tres empresas, viendo en cada llamada la información y el conocimiento de la empresa correspondiente — sin mezclar datos entre ellas.

El detalle de configuración del módulo está en [4.9 Oficina virtual / BPO](../modulos/oficina-virtual-bpo.md); esta página resume el caso aplicado de punta a punta.

## Cómo se usa

1. **Cola y grupo de agentes:** un único grupo de agentes puede atender a las tres empresas cliente, ya que lo que cambia entre ellas es la pantalla y el conocimiento mostrado, no quién contesta.
2. **Un DID por empresa cliente:** B, C y D reciben cada una su propio DID — es la señal que usa el sistema para identificar de qué empresa viene la llamada.
3. **Un usuario virtual por empresa cliente:** se da de alta B, C y D como usuarios virtuales, cada uno con su propio saludo, enlace de pantalla, y base de conocimiento (ver [4.9](../modulos/oficina-virtual-bpo.md#3-dar-de-alta-el-usuario-virtual-empresa-cliente)).
4. **Resultado para el agente:** al entrar una llamada de un cliente de B, el agente ve el nombre de B, su saludo de apertura, los datos del cliente que llama (si ya existía), y puede consultar la base de conocimiento específica de B para resolver la consulta — todo sin salir de la misma plataforma ni conocer de memoria el negocio de B.
5. **Reportes separados por empresa cliente:** si B, C o D necesitan ver sus propias estadísticas sin acceso al resto del sistema, se les crea una [cuenta BPO](../modulos/oficina-virtual-bpo.md#cuentas-bpo) con acceso acotado a su propio usuario virtual.

## Referencia rápida

| Elemento | Uno por |
|---|---|
| Grupo de agentes / cola | Compartido entre todas las empresas cliente |
| DID | Empresa cliente |
| Usuario virtual (pantalla + conocimiento) | Empresa cliente |
| Cuenta BPO (si aplica) | Empresa cliente que necesita ver sus propios reportes |

---

## Fuentes

- `raw/zh/用途和案例/为客户提供虚拟呼叫中心服务.txt`