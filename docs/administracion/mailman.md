---
title: "Configurar Mailman / correo saliente"
resumen: "Dependencias Perl necesarias para el script de envío de correo masivo de AsterCC."
seccion: "6.4 Mailman / correo saliente"
tipo: tutorial
nivel: avanzado
roles: [administrador]
fuente: en
obsoleto: true
relacionados: []
---

# Configurar Mailman / correo saliente

## Qué es

AsterCC incluye un script en Perl (`astercc_mailman.pl`) para el envío de correo masivo usado por el módulo de [mensajería](../modulos/atencion-cliente-mensajeria-ecommerce.md#mensajeria-masiva). Este script depende de varios módulos de Perl que se instalan vía CPAN.

!!! warning "Puede estar desactualizado"
    El procedimiento documenta CPAN sobre Perl 5.8.8 — una versión muy antigua. En un servidor moderno, confirma primero si el script de instalación de AsterCC (ver [Descargar e instalar AsterCC](../instalacion/descarga-e-instalacion.md)) ya resuelve estas dependencias automáticamente antes de instalar manualmente.

## Cómo se usa (procedimiento original — referencia histórica)

1. Instalar CPAN:
   ```bash
   yum -y install cpan
   cpan
   ```
2. Dentro de la consola de CPAN, instalar los módulos Perl requeridos:
   ```
   install Module::Build::Compat
   install Config::IniFiles
   install DBI
   install MIME::Lite
   install Net::SSLeay
   install IO::Socket::SSL
   install Authen::SASL
   install Devel::CheckLib
   install Email::Date::Format
   install MIME::Base64
   install Net::SMTP
   install Net::SMTP::SSL
   install Authen::SASL::XS
   install Encode
   install Data::Dumper
   ```

## Referencia rápida

| Dependencia clave | Para qué |
|---|---|
| `DBI` | Conexión a la base de datos |
| `Net::SMTP` / `Net::SMTP::SSL` | Envío de correo |
| `MIME::Lite` / `MIME::Base64` | Formato de mensajes |

---

## Fuentes

- `raw/en/install_astcc_mailman.txt`