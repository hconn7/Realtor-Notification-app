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
        # Try to read the existing CSV file
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
