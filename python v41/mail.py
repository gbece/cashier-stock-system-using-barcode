# Se importan las librerias necesarias
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
def enviar(mail,asunto,mensaje,codigoTemp): 
    # Se crea la instancia del mensaje objeto
    msg = MIMEMultipart()
       
        
    message = mensaje+" "+codigoTemp+"\n\nEste es un mensaje automatico generado por el sistema SBC.\nNo responder, es una cuenta de email desatendida.\n\nGracias.\n\nEl equipo de desarrollo de SISTEMAS EMBEBIDOS.\nORT - Facultad de Ingenieria."
         
    # Se configuran parametros del meensaje
    password = "embebidos123"
    msg['From'] = "embebidos@theko.com.uy"
    msg['To'] = mail
    msg['Subject'] = asunto+codigoTemp
          
    # Se agrega en el cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))
           
    # Se crea el servidor
    server = smtplib.SMTP('mail.theko.com.uy: 587')
            
    server.starttls()
             
    # Credenciales de login del servidor
    server.login(msg['From'], password)
              
               
    # Se envia el mensaje a traves del servidor
    server.sendmail(msg['From'], msg['To'], msg.as_string())
                
    server.quit()
                 
    print "Email enviado correctamente a  %s:" % (msg['To'])
