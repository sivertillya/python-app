import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

name = request.form.get("name")
email = request.form.get("email")
classed = request.form.get("classed")
topic = 'REGISTER'
toaddr = email
if not name or not email or not classed:
    return render_template("failder.html")
message = f"Имя: {name}. Клас: {classed}"

msg = MIMEMultipart()
msg[ 'Subject' ] = topic
msg[ 'From' ] = 'wolf.sivert@gmail.com'
body = message
msg.attach(MIMEText(body, 'plain'))

server = root.SMTP_SSL('smtp.gmail.com', 465)
server.login('wolf.sivert@gmail.com', 'yfcnz27000')
server.sendmail('wolf.sivert@gmail.com', toaddr, msg.as_string())