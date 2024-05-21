import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def send_email(receiver_email, subject, body):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def check_anniversary(func):
    def wrapper(entry, *args, **kwargs):
        client_date = datetime.datetime.strptime(entry.date, "%Y/%m/%d")
        today = datetime.datetime.today()
        if today.month == client_date.month and today.day == client_date.day:
            return func(entry, *args, **kwargs)
        else:
            print(f"Today is not the anniversary for {entry.name}.")
    return wrapper

class Entry:
    def __init__(self, name, address, date, gift):
        self.name = name
        self.address = address
        self.date = date
        self.gift = gift

    def update_csv(self, filename='ClientData.csv'):
        try:
            with open(filename, 'a') as file:
                file.write(f'{self.name},{self.address},{self.date},{self.gift}\n')
            print("Entry added successfully to", filename)
        except Exception as e:
            print("Error:", e)

    @check_anniversary
    def send_anniversary_email(self):
        receiver_email = "shannon@shannonconner.com"
        subject = f"Anniversary Reminder for {self.name}"
        body = f"Dear {self.name},\n\nThis is a reminder for your anniversary. We hope you enjoy your {self.gift}.\n\nBest regards,\nYour Company"
        send_email(receiver_email, subject, body)

def check_and_send_anniversaries(filename='ClientData.csv'):
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        name = row['Name']
        address = row['Address']
        date = row['Date']
        gift = row['Gift']
        entry = Entry(name, address, date, gift)
        entry.send_anniversary_email()

if __name__ == "__main__":
    check_and_send_anniversaries()
