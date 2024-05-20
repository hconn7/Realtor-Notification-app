import pandas as pd

class Entry:
    def __init__(self, name, address, date, gift):
        self.name = name
        self.address = address
        self.date = date
        self.gift = gift

    # Method to update CSV file with the current entry
    def update_csv(self, filename='ClientData.csv'):
        try:
            # Append the entry to the CSV file
            with open(filename, 'a') as file:
                file.write(f'{self.name},{self.address},{self.date},{self.gift}\n')
            print("Entry added successfully to", filename)
        except Exception as e:
            print("Error:", e)



