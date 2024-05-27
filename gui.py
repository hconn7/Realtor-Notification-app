import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox

import callback_functions
import pandas as pd
from csv_methods import Client

class ClientManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Management System")
        self.root.geometry("600x400")
        
        # Load the background image
        self.bg_image = tk.PhotoImage(file="images/bg_image.png")
        
        # Create a Canvas widget covering the entire window
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the canvas
        
        image_path = "images/LOGOGO.png" 
        self.image_photo = tk.PhotoImage(file=image_path)

# Place the image on the canvas
        self.canvas.create_image(300, 80, anchor=tk.CENTER, image=self.image_photo)
   
        
        # Create buttons
        tk.Button(root, text="List Clients", command=self.display_client_list, relief="flat", padx=10,pady=5, font=("Helvetica", 16), borderwidth=0, highlightthickness=0, overrelief="flat").place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        tk.Button(root, text="New Client", command=self.open_submit_window, relief="flat",padx=10, pady=5, font=("Helvetica", 16), borderwidth=0, highlightthickness=0, overrelief="flat").place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Add a label
        
    
    def get_client_list(self):
        print("Fetching client list from CSV file")
        client_list = []
        try:
            df = pd.read_csv('ClientData.csv')
            for _, row in df.iterrows():
                client = Client(name=row['name'], address=row['address'], date=row['date'], gift=row['gift'])
                client_list.append(client)
            return client_list
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")
            return []

    def display_client_list(self):
        client_list = self.get_client_list()
        if client_list:
            list_window = tk.Toplevel(self.root)
            list_window.title("List of Clients")

            frame = ttk.Frame(list_window)
            frame.pack(fill="both", expand=True)

            text = tk.Text(frame, wrap="word", font=("Helvetica", 12), height=40)
            text.pack(fill="both", expand=True, padx=10, pady=10)

            text.insert(tk.END, "List of Clients:\n\n")
            for client in client_list:
                text.insert(tk.END, f"- {client.name}\n   Address: {client.address}\n   Date: {client.date}\n   Gift: {client.gift}\n\n")

            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
            scrollbar.pack(side="right", fill="y")
            text.config(yscrollcommand=scrollbar.set)



    def open_submit_window(self):
        submit_window = tk.Toplevel(self.root)
        submit_window.title("New Client")

        input_frame = ttk.Frame(master=submit_window)
        input_frame.pack(padx=10, pady=10)

        label_client = ttk.Label(master=input_frame, text="Client Name:")
        label_address = ttk.Label(master=input_frame, text="Address:")
        label_date = ttk.Label(master=input_frame, text="Date:")
        label_gift = ttk.Label(master=input_frame, text="Gift:")

        self.entry_client = ttk.Entry(master=input_frame)
        self.entry_address = ttk.Entry(master=input_frame)
        self.entry_date = ttk.Entry(master=input_frame)
        self.entry_gift = ttk.Entry(master=input_frame)

        submit = ttk.Button(master=input_frame, text='Update Data', command=self.submit_data)
        submit.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        label_client.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        label_address.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        label_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        label_gift.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_client.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_address.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_gift.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        
    def submit_data(self):
        name = self.entry_client.get()
        address = self.entry_address.get()
        date = self.entry_date.get()
        gift = self.entry_gift.get()
        
        try:
            message = callback_functions.submit_data(name, address, date, gift)
            messagebox.showinfo("Success", message)
            self.entry_client.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_gift.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    
