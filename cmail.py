import smtplib
from smtplib import SMTP 
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(YOUR EMAIL ID,YOUR APP PASSWORD)
    msg=EmailMessage()
    msg['From']=YOUR EMAIL ID
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
