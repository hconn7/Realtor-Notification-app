from dataclasses import dataclass
import pandas as pd
from emailing import send_email
import datetime
import os
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox

@dataclass
class Client:
    name: str
    address: str
    date: str
    gift: str


    def to_dict(self):
        return {'name': self.name, 'address': self.address, 'date': self.date, 'gift': self.gift}

def append_to_dataframe(client: Client, df: pd.DataFrame):
    if df.empty:
        return pd.DataFrame([client.to_dict()])
    else:
        return df.append(client.to_dict(), ignore_index=True)
    
def save_to_csv(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)

def update_csv(client, filename='ClientData.csv'):
    try:
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['name', 'address', 'date', 'gift'])

        new_data = pd.DataFrame([client.to_dict()])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(filename, index=False)
    except Exception as e:
        print("Error:", e)

csv_file = 'ClientData.csv'
def send_anniversary_emails(csv_file):
    today = datetime.date.today()

    with open(csv_file, 'r') as file:
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            name = row['name']
            date_str = row['date'].strip()
            gift = row['gift']
            anniversary_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

            if today.month == anniversary_date.month and today.day == anniversary_date.day:
                recipient_email = 'henryconner10@gmail.com'
                sender_email = os.getenv("SENDER_EMAIL")
                sender_password = os.getenv('SENDER_PASSWORD') 


                subject = 'Anniversary Update'
                body = f'Hello, your client {name} has an anniversary today! The gift you gave them was: {gift}'
                
                send_email(sender_email, sender_password, recipient_email, subject, body)
                print(f"Email sent to {recipient_email} for {name}")

send_anniversary_emails(csv_file)