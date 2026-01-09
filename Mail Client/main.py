import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server=smtplib.SMTP("smtp.gmail.com",25)
server.ehlo()
server.login("mail@gmail.com","password123")
with open('password.txt','r') as f:
    password=f.read()

server.login('nivedshenoy0@gmail.com',password)

msg=MIMEMultipart()
msg['From']='NeuralNine'
msg['To']='nivedshenoy0@gmail.com'
msg['Subject']='Just a test'

with open('message.txt','r') as f:
    message=f.read()
msg.attach(MIMEText(message,'plain'))

filename='coding.jpg'
attachment=open(filename,'rb')

p= MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition",f"attachment; filename={filename}")
msg.attach(p)
text=msg.as_string()
server.sendmail("nivedshenoy0@gmail.com","nivedshenoy@somaiya.edu")