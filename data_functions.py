import pandas as pd
from entry_info import Client

csv = "ClientData.csv"

def list_clients():
    try:
        df = pd.read_csv(csv)
        return df.to_string()
    except FileNotFoundError:
        return "No client data found."

def submit_data(name, address, date, gift):
    client = Client(name, address, date, gift)
    if len(date) != 10:
        raise ValueError("Please enter in the correct format: YYYY-MM-DD")
    
    from entry_info import update_csv  # Local import to avoid circular import at the module level
    update_csv(client)
    return "Client data submitted successfully!"
