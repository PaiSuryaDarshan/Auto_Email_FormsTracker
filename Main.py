from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib

# Any Integer
Selector = 3
if Selector == 0:
    import TEST_Pre_requisites as Pr
elif Selector == 1:
    import Mon_Forms as Pr
elif Selector == 2:
    import Meeting_Time_Venue as Pr
elif Selector == 3:
    import Pre_Lab_Meeting_Time_Venue as Pr

Pr.email_receiver_Test = ["n.pai@kcl.ac.uk", "suryadarshan82@gmail.com"]

em = MIMEMultipart()
em['From']      = Pr.email_sender
em['To']        = ", ".join(Pr.email_receiver_Test)
em['Subject']   = Pr.subject

em.attach(MIMEText(Pr.body, 'html'))

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(Pr.email_sender, Pr.email_password)
    smtp.send_message(em)
    
    print('Email sent successfully!')