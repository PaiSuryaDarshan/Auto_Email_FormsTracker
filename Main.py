from email.message import EmailMessage
import Pre_requisites as Pr
import ssl
import smtplib

em = EmailMessage()

em['From']      = Pr.email_sender
em['To']        = Pr.email_receiver
em['Subject']   = Pr.subject
em.set_content(Pr.body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(Pr.email_sender, Pr.email_password)
    smtp.send_message(em)
    
    print('Email sent successfully!')