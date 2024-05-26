
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




import sched
import time


csv_file = "ClientData.csv"

sender_password = "kudl alca cyah jlnr"
sender_email = "henryconner10@gmail.com"
reciever_email = "henryconner10@gmail.com"

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Setup the email message
    message = MIMEMultipart()
    message['From'] = sender_email
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
    

