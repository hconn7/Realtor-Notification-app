
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')



csv_file = "ClientData.csv"

reciever_email = "henryconner10@gmail.com"

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Setup the email message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.starttls()
    
    # Login to the SMTP server
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

    # Close the connection to the SMTP server
    server.quit()
    












    # Reschedule the task for the next day
    

