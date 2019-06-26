#!/usr/bin/python3

import smtplib
from  email.mime.text import MIMEText # Multipurpose internet mail extensions
from email.mime.multipart import MIMEMultipart 

# email of sender

email_sen=input("Your email address:-")
passwd=input("Your email password:-")
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
text=msg.as_string()

# Initializing SMTP server 
# USing Gmail smtp server  ,  there port number is 587
server = smtplib.SMTP("smtp.gmail.com",587)

# I nitializing secure connection
server.starttls()

# Login credentials
server.login(email_sen,passwd)


# Sending mail 
server.sendmail(email_sen,email_rec,text)

# Ending the sevice
server.quit()
