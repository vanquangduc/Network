from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
#  server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
#  server.ehlo

pwd = '8602289duc'

server.login('vanquangduc2242000@gmail.com', pwd)
#  server.connect()
msg = MIMEMultipart()
msg['From'] = 'Duc Van'
msg['To'] = 'testmail@spaml.de'
msg['Subject'] = 'This is a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'bimeo.jpg'
attachment = open(filename,'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={ filename }')
msg.attach(p)

text = msg.as_string()

server.sendmail('vanquangduc2242000@gmail.com', 'testmail@spaml.de', text)











