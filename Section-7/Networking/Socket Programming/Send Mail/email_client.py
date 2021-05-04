import smtplib
from email.mime.text import MIMEText

body = "This is text email:How are you"

msg = MIMEText(body)
msg['From'] = "appliedmk@gmail.com"
msg['To'] = "muzmmilpathan@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("appliedmk@gmail.com","9145686396")

server.send_message(msg)

print("Send Mail")

server.quit()