from dataclasses import dataclass
import pandas as pd

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
        df = pd.read_csv(filename)  # Load existing data
        new_data = pd.DataFrame([client.to_dict()])  # Convert client data to DataFrame
        if df.empty:
            df = new_data  # If DataFrame is empty, assign new_data directly
        else:
            df = pd.concat([df, new_data], ignore_index=True)  # Concatenate existing and new data
        df.to_csv(filename, index=False)  # Save updated data
        print("Entry added successfully to", filename)
    except Exception as e:
        print("Error:", e)
