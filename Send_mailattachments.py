#!/usr/bin/python3

import smtplib
from  email.mime.text import MIMEText # Multipurpose internet mail extensions
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
from email import encoders
import getpass
# email of sender

email_sen=input("Your email address:-")
#passwd=input("Your email password:-")
passwd=getpass.getpass(prompt="Enter password:-")
# email of reciever
email_rec=input("Enter Email Address you want to send mail:-")

# Subject 
subject=input("Enter subject:-")

# Calling MIME multipart
msg = MIMEMultipart()
msg['From'] = email_sen
msg['To'] = email_rec
msg['Subject'] = subject
body=input("Enter message:-")

# Attaching the msg to the body 
msg.attach(MIMEText(body,'plain'))

# Attaching file and image with mail
filename="hello.txt"
attachment = open(filename,"rb")

# Encoding with base64 
# Uploading file with base64
part = MIMEBase("application","octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("Content-Disposition","attachment: filename= "+filename)
msg.attach(part)
text=msg.as_string()

# Initializing SMTP server 
# Using Gmail smtp server  ,  there port number is 587
server = smtplib.SMTP("smtp.gmail.com",587)

# Initializing secure connection
server.starttls()

# Login credentials
server.login(email_sen,passwd)

# Sending mail 
server.sendmail(email_sen,email_rec,text)

# Ending the sevice
server.quit()
