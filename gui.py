import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
import data_functions

class ClientManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#ADD8E6")  # Set background color
        
        # Set window icon
        icon = PhotoImage(file='ICON.png')
        self.root.iconphoto(True, icon)
        
        # Create image label
        image_path = "shannon_logo.png"  # Replace with your image path
        self.image_photo = PhotoImage(file=image_path)
        image_label = tk.Label(root, image=self.image_photo, bg="#ADD8E6")
        image_label.pack(pady=10)
        
        # Create buttons
        tk.Button(root, text="List Clients", command=self.list_clients, bg="#008080", fg="black", font=("Helvetica", 12)).pack(pady=5)
        tk.Button(root, text="New Client", command=self.open_submit_window, bg="#008080", fg="black", font=("Helvetica", 12)).pack(pady=5)


    def list_clients(self):
        client_list = data_functions.list_clients()
        list_window = tk.Toplevel(self.root)
        list_window.title("List of Clients")
        text = tk.Text(list_window)
        text.pack()
        text.insert(tk.END, client_list)

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

        submit = ttk.Button(master=input_frame, text='Update Data', 
                            command=self.submit_data)

        label_client.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        label_address.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        label_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        label_gift.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_client.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_address.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_date.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_gift.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        submit.grid(row=4, columnspan=2, pady=10)

    def submit_data(self):
        name = self.entry_client.get()
        address = self.entry_address.get()
        date = self.entry_date.get()
        gift = self.entry_gift.get()
        
        try:
            message = data_functions.submit_data(name, address, date, gift)
            messagebox.showinfo("Success", message)
            self.entry_client.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_gift.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.geometry("600x400")

root.configure(bg="#ADD8E6")





# Pack the label to display it in the window




app = ClientManagementSystem(root)
root.mainloop()
