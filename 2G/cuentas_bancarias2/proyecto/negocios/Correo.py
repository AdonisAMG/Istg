# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# import time
# from random import randrange

class EnvioEmails:
    def __init__(self, correo_origen, password, destinatario, asunto, mensaje):
        self.correo_origen = correo_origen
        self.password = password
        self.destinatario = destinatario
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar_correo(self,mensaje_error):
        try:
            # create message object instance
            msg = MIMEMultipart()

            mensaje=self.mensaje

            # setup the parameters of the message
            password = self.password
            msg['From'] = self.correo_origen
            msg['To'] = self.destinatario
            msg['Subject'] =self.asunto

            # # add in the message body
            msg.attach(MIMEText(mensaje, 'plain'))
            #print(msg)

            #create server
            server = smtplib.SMTP('smtp.gmail.com:587')
            #prueba pa generar error
            #server = smtplib.SMTP('smtp.gmail.com:099')
            # server = smtplib.SMTP('smtp.gmail.com',587)

            server.starttls()

            # Login Credentials for sending the mail
            #print(f"user:{msg['From']}  passw:{password}")
            server.login(msg['From'], password)

            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()

            #print("successfully sent email to %s:" % (msg['To']))
            return True

        except Exception as inst:
            mensaje_error.setdefault('ERROR_1', str(type(inst)))
            mensaje_error.setdefault('ERROR_2', str(inst.args))
            mensaje_error.setdefault('ERROR_3', str(inst))

            # print(type(inst))  # the exception instance
            # print(inst.args)  # arguments stored in .args
            # print(inst)
            return False


#fecha=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


# fecha=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
#
# mensage = """Registramos solicitud de clave de seguridad
# temporal el:  '{}'
#   La clave asignada es {}""".format(fecha,randrange(1000,9999))
#
# correo_origen="pruebas.correos.poo.2g2h@gmail.com"
# password = "Pcorreos123456"
# destinatario = "jojam200x@hotmail.com"
# asunto= "Solicitud de Transaccion"
#
# msg_errores={}
# envio_correo=EnvioEmails(correo_origen,password,destinatario,asunto,mensage)
# value=envio_correo.enviar_correo(msg_errores)
# print(value)
#
# if not value:
#     print("**** Error ****: ")
#     print(msg_errores["ERROR_1"])
#     print(msg_errores["ERROR_2"])
#     print(msg_errores["ERROR_3"])
# else:
#     print("Correo Enviado con exito")


