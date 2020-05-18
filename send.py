import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

name = 'Sivert'
email = 'wolf.siver@gmail.com'
classed = '11'
topic = 'REGISTER'
toaddr = email
message = f"Имя: {name}. Клас: {classed}"

msg = MIMEMultipart()
msg[ 'Subject' ] = topic
msg[ 'From' ] = 'wolf.sivert@gmail.com'
body = message
msg.attach(MIMEText(body, 'plain'))

server = root.SMTP_SSL('smtp.gmail.com', 465)
server.login('wolf.sivert@gmail.com', 'yfcnz27000')
server.sendmail('wolf.sivert@gmail.com', toaddr, msg.as_string())