import tkinter as tk
from tkinter import *
from tkinter import ttk
from entry_info import Client
from entry_info import update_csv

def submit_data():
    name = entry_client.get()
    address = entry_address.get()
    date = entry_date.get()
    gift = entry_gift.get()
    
    new_entry = Client(name, address, date, gift)

    update_csv(new_entry)
    
   
# Create the main window
window = tk.Tk()
window.title("Input Form")

# Change image type
icon = PhotoImage(file='ICON.png')
window.iconphoto(True, icon)

# Create a frame to contain input widgets
input_frame = ttk.Frame(master=window)
input_frame.pack(padx=10, pady=10)

# Create labels for entry fields
label_client = ttk.Label(master=input_frame, text="Client Name:")
label_address = ttk.Label(master=input_frame, text="Address:")
label_date = ttk.Label(master=input_frame, text="Date:")
label_gift = ttk.Label(master=input_frame, text="Gift:")

# Create input fields
entry_client = ttk.Entry(master=input_frame)
entry_address = ttk.Entry(master=input_frame)
entry_date = ttk.Entry(master=input_frame)
entry_gift = ttk.Entry(master=input_frame)

# Create a button
submit = ttk.Button(master=input_frame, text='Update Data', command=submit_data)

# Arrange labels and entry fields in grid layout
label_client.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
label_address.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
label_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
label_gift.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

entry_client.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
entry_address.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
entry_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
entry_gift.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

submit.grid(row=4, columnspan=2, pady=10)

# Run the application
window.mainloop()
