---
title: "Configurar OpenVPN"
resumen: "Cómo dar acceso remoto a teléfonos IP fuera de la oficina mediante OpenVPN."
seccion: "6.2 OpenVPN"
tipo: tutorial
nivel: avanzado
roles: [administrador]
fuente: en
obsoleto: true
relacionados: [pbx-y-telefonia]
---

# Configurar OpenVPN

## Qué es

OpenVPN permite que teléfonos IP fuera de la red local (por ejemplo, agentes trabajando remoto) se conecten de forma segura al servidor de AsterCC como si estuvieran en la oficina, registrando su extensión normalmente.

!!! warning "Puede estar desactualizado"
    El procedimiento original documenta una compilación manual de OpenVPN 2.2.1 desde código fuente sobre CentOS antiguo — versiones y pasos de compilación completamente obsoletos. En un servidor moderno (Rocky Linux 9), instala OpenVPN desde el gestor de paquetes del sistema (`dnf install openvpn easy-rsa`) en vez de compilarlo. Los conceptos generales de configuración de abajo siguen siendo válidos.

## Cómo se usa

### Conceptos generales (siguen aplicando)

1. Abre el puerto UDP 1194 en el firewall hacia el servidor (UDP es preferible a TCP por velocidad y menor consumo de ancho de banda).
2. Genera una **autoridad certificadora (CA)** y un certificado de servidor con `easy-rsa`.
3. Genera un **certificado y llave individual por cada teléfono** que se vaya a conectar — el nombre de cada dispositivo debe ser único, ya que aparece en el estado de conexiones VPN.
4. Configura el servidor OpenVPN con una subred dedicada para los clientes VPN (ej. `192.168.2.0/24`), distinta de la red local, y con los certificados generados.
5. En cada teléfono, carga el certificado de CA, su propio certificado/llave, y la configuración de cliente apuntando a la IP y puerto del servidor.
6. Revisa `/etc/openvpn/openvpn.log` para diagnosticar problemas de conexión.

### Notas

- No todos los teléfonos IP soportan OpenVPN de forma nativa — confirma con el fabricante del modelo que vayas a usar antes de planear esta arquitectura.
- Esta es una alternativa a exponer directamente el puerto SIP/RTP a internet — reduce superficie de ataque, a costa de la complejidad de gestionar certificados por dispositivo.

## Referencia rápida

| Elemento | Valor típico |
|---|---|
| Protocolo/puerto recomendado | UDP 1194 |
| Herramienta de certificados | easy-rsa |
| Log de diagnóstico | `/etc/openvpn/openvpn.log` |

---

## Fuentes

- `raw/en/openvpn.txt`