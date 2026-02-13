import resend
from flask import current_app


def send_email(to, subject, template):
    try:
        # configurar resend con su api key
        resend.api_key = current_app.config["RESEND_API_KEY"]
        # crear el contenido del correo
        params: resend.Emails.SendParams = {
            "from": current_app.config["EMAIL_FROM"],
            "to": [to],
            "subject": subject,
            "html": template,
        }

        email_enviado = resend.Emails.send(params)
        print(email_enviado)
        return True
    except Exception as e:
        print(e)
        return None


def send_verification_email(email, nombre, codigo):
    email = "jz.ai.test@gmail.com"
    subject = "Código de verificación"
    template = f"""
        <!Doctype html>
        <html>
        <head>
        <style>
            body {{
            font-family: Arial, sans-serif;
            color: #333;
            }}
            .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            }}
            .header {{
            background-color: #4f46e5;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
            }}
            .content {{
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 0 0 5px 5px;
            }}
            .code {{
            background-color: #4f46e5;
            color: #fff;
            font-size: 32px;
            font-weight: bold;
            padding: 15px;
            text-align: center;
            border-radius: 5px;
            margin: 20px 0;
            }}
            .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px
            }}
        </style>
        </head>
        <body>
        <div class="container">
            <div class="header">
            <h1>Verificación de cuenta</h1>
            </div>
            <div class="content">
            <p>Hola, {nombre}</>
            <p>Gracias por registrarse en TODO App, para completar tu registro, usa el siguiente codigo</p>
            <div class="code">
                {codigo}
            </div>
            <p>Este codigo, expira en 15 minutos</p>
            </div>
            <div class="footer">
            <p>Este es un email automatico, por favor no respondas este mensaje.</p>
            </div>
        </div>
        </body>
    """
    return send_email(email, subject, template)


def send_welcome_email(email, nombre):
    email = "jz.ai.test@gmail.com"
    subject = "Bienvenido a TODO App"
    template = f"""
        <!Doctype html>
        <html>
        <head>
        <style>
            body {{
            font-family: Arial, sans-serif;
            color: #333;
            }}
            .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            }}
            .header {{
            background-color: #4f46e5;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
            }}
            .content {{
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 0 0 5px 5px;
            }}
            .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px
            }}
        </style>
        </head>
        <body>
        <div class="container">
           <div class="header">
            <h1>Bienvenido a TODO App</h1>
            </div>
            <div class="content">
            <p>Hola, {nombre}</>
            <p>Gracias por registrarse en TODO App, ya puedes iniciar sesion y empezar a crear tus tareas</p>
            </div>
            <div class="footer">
            <p>Este es un email automatico, por favor no respondas este mensaje.</p>
            </div>
        </div>
        </body>
    """
    return send_email(email, subject, template)


def send_password_recovery_email(email, nombre, codigo):
    email = "jz.ai.test@gmail.com"
    subject = "Recupera tu contraseña - TODO App"
    template = f"""
        <!Doctype html>
        <html>
        <head>
        <style>
            body {{
            font-family: Arial, sans-serif;
            color: #333;
            }}
            .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            }}
            .header {{
            background-color: #4f46e5;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
            }}
            .content {{
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 0 0 5px 5px;
            }}
            .code {{
            background-color: #4f46e5;
            color: #fff;
            font-size: 32px;
            font-weight: bold;
            padding: 15px;
            text-align: center;
            border-radius: 5px;
            margin: 20px 0;
            }}
            .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px
            }}
        </style>
        </head>
        <body>
        <div class="container">
            <div class="header">
            <h1>Recuperar contraseña</h1>
            </div>
            <div class="content">
            <p>Hola, {nombre}</p>
            <p>Hemos recibido una solicitud para restablecer la contraseña de tu cuenta en <strong>TODO App</strong>. Usa el siguiente código para continuar con el proceso:</p>
            <div class="code">
                {codigo}
            </div>
            <p>Este código es válido por 15 minutos. Si no solicitaste este cambio, puedes ignorar este correo de forma segura.</p>
            </div>
            <div class="footer">
            <p>Este es un email automático, por favor no respondas este mensaje.</p>
            </div>
        </div>
        </body>
        </html>
    """
    return send_email(email, subject, template)


def send_password_changed_email(email, nombre):
    email = "jz.ai.test@gmail.com"
    subject = "Tu contraseña ha sido actualizada - TODO App"
    template = f"""
        <!Doctype html>
        <html>
        <head>
        <style>
            body {{
            font-family: Arial, sans-serif;
            color: #333;
            }}
            .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            }}
            .header {{
            background-color: #4f46e5;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
            }}
            .content {{
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 0 0 5px 5px;
            }}
            .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px
            }}
        </style>
        </head>
        <body>
        <div class="container">
            <div class="header">
            <h1>Contraseña actualizada</h1>
            </div>
            <div class="content">
            <p>Hola, {nombre}</p>
            <p>Te informamos que la contraseña de tu cuenta en <strong>TODO App</strong> ha sido cambiada exitosamente.</p>
            <p>Ya puedes iniciar sesión con tu nueva clave. Si tú realizaste este cambio, no es necesario que hagas nada más.</p>
            <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
            <p style="font-size: 13px; color: #e11d48;">
                <strong>¿No reconoces este cambio?</strong><br>
                Si no cambiaste tu contraseña, por favor ponte en contacto con nuestro equipo de soporte de inmediato para proteger tu cuenta.
            </p>
            </div>
            <div class="footer">
            <p>Este es un email automático, por favor no respondas este mensaje.</p>
            </div>
        </div>
        </body>
        </html>
    """
    return send_email(email, subject, template)
