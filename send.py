from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

print("Please enter App Passwords in the .env file (See https://support.google.com/mail/?p=InvalidSecondFactor)\n")

email_sender = input("Please enter your email: ")
email_password = os.getenv('APP_PASSWORDS')
email_receiver = input("Please enter the email of the person you want to email: ")

subject = input("Please enter the subject of the email: ")
content = input("Please enter the content of the email: \n")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(content)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("\n\nSuccessful mailing.")