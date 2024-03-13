import email, smtplib, ssl
from sms.providers.providers import PROVIDERS
class Email_MESSAGE(object):

    def send_sms_via_gmail(
            number:str, 
            message:str, 
            provider:str, 
            sender_credential:tuple, 
            subject:str="Tracker", 
            smpt_server="smtp.gmail.com", 
            smpt_port:int = 465
    ):
        sender_email, email_password = sender_credential
        reciever_email= f"{number}@{PROVIDERS.get(provider).get('sms')}"

        email_message = f"Subject:{subject}\nTo:{reciever_email}\n{message}" 

        with smtplib.SMTP_SSL(smpt_server, smpt_port,context=ssl.create_default_context()) as email:
            email.login(sender_email, email_password)
            email.sendmail(sender_email, reciever_email,email_message)
    
    def send_sms_via_icloud(
            number:str, 
            message:str, 
            provider:str, 
            sender_credential:tuple, 
            subject:str="Tracker", 
            smpt_server="smtp.mail.me.com", 
            smpt_port:int = 587 
    ):
        sender_email, email_password = sender_credential
        reciever_email= f"{number}@{PROVIDERS.get(provider).get('sms')}"

        email_message = f"Subject:{subject}\nFrom:{sender_email}\nTo:{reciever_email}\n{message}" 

        context = ssl.create_default_context()
        with smtplib.SMTP(smpt_server, smpt_port) as email_server:
            email_server.starttls(context=context)  # Secure the connection
            email_server.login(sender_email, email_password)
            email_server.sendmail(sender_email, reciever_email, email_message)