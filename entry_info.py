from dataclasses import dataclass
import pandas as pd
import csv
from emailing import send_email
import datetime
import sched
import time


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
            print(f"Existing data read from {filename}:")
            print(df)
        except FileNotFoundError:
            # If the file does not exist, create an empty DataFrame with the appropriate columns
            df = pd.DataFrame(columns=['name', 'address', 'date', 'gift'])
            print(f"{filename} not found. Created a new DataFrame.")

        # Convert client data to DataFrame
        new_data = pd.DataFrame([client.to_dict()])
        print("New client data to add:")
        print(new_data)

        # Concatenate the new data with the existing DataFrame
        df = pd.concat([df, new_data], ignore_index=True)
        print("Updated DataFrame:")
        print(df)

        # Save updated DataFrame to CSV
        df.to_csv(filename, index=False)
        print("Entry added successfully to", filename)
    except Exception as e:
        print("Error:", e)
csv_file = 'ClientData.csv'
def send_anniversary_emails(csv_file):
    global anniversary_sent
    today = datetime.date.today()
    print("Today's date:", today)

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        anniversary_sent = False
        for row in reader:
            # Extract data from the current row
            name = row['name']
            address = row['address']
            date_str = row['date'].strip()  # Remove leading and trailing whitespace
            gift = row['gift']

            # Parse the date string
            anniversary_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            print("Anniversary date for", name, ":", anniversary_date)

            # Check if today is the anniversary date
            if today.month == anniversary_date.month and today.day == anniversary_date.day:
                recipient_email = 'henryconner10@gmail.com'  # Update with recipient's email address
                print("Sending email to", recipient_email, "for", name)
                sender_email = 'henryconner10@gmail.com'
                sender_password = "kudl alca cyah jlnr"

                subject = 'Anniversary Update'
                body = f'Hello Shannon, your client, {name} has an anniversary today! The gift you gave them was: {gift}'
                

                send_email(sender_email, sender_password, recipient_email, subject, body)
                print("Email sent successfully to", recipient_email)
                anniversary_sent = True
            else:
                print("No anniversary today for", name)
send_anniversary_emails(csv_file)

          
