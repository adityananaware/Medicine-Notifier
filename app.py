import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from medicine_db import add_medicine, fetch_medicines
import datetime

# Function to Add Medicine
def add_medicine_ui():
    name = name_entry.get()
    expiry_date = expiry_date_entry.get()
    purchase_date = purchase_date_entry.get()
    duration = duration_entry.get()

    if not (name and expiry_date and purchase_date and duration):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    add_medicine(name, expiry_date, purchase_date, int(duration))
    messagebox.showinfo("Success", "Medicine added successfully!")
    refresh_medicine_list()

# Function to Refresh Medicine List
def refresh_medicine_list():
    medicines_list.delete(*medicines_list.get_children())
    medicines = fetch_medicines()
    
    for med in medicines:
        name, expiry, purchase, duration = med[1:]
        finish_date = datetime.datetime.strptime(purchase, "%Y-%m-%d").date() + datetime.timedelta(days=duration)
        days_to_expiry = (datetime.datetime.strptime(expiry, "%Y-%m-%d").date() - datetime.date.today()).days
        days_to_finish = (finish_date - datetime.date.today()).days
        
        medicines_list.insert("", "end", values=(name, expiry, f"{days_to_expiry} days", finish_date, f"{days_to_finish} days"))

# UI Setup
app = tk.Tk()
app.title("Medicine Tracker")
app.geometry("600x500")
app.configure(bg="#f5f5f5")

# Header Label
title_label = tk.Label(app, text="Medicine Tracker", font=("Arial", 18, "bold"), fg="#333", bg="#f5f5f5")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(app, bg="#f5f5f5")
frame.pack(pady=10)

tk.Label(frame, text="Medicine Name:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Expiry Date
tk.Label(frame, text="Expiry Date:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5)
expiry_date_entry = DateEntry(frame, font=("Arial", 12), date_pattern='yyyy-mm-dd')
expiry_date_entry.grid(row=1, column=1, padx=5, pady=5)

# Purchase Date
tk.Label(frame, text="Purchase Date:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=5, pady=5)
purchase_date_entry = DateEntry(frame, font=("Arial", 12), date_pattern='yyyy-mm-dd')
purchase_date_entry.grid(row=2, column=1, padx=5, pady=5)

# Duration
tk.Label(frame, text="Duration (days):", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, padx=5, pady=5)
duration_entry = tk.Entry(frame, font=("Arial", 12))
duration_entry.grid(row=3, column=1, padx=5, pady=5)

# Add Medicine Button
add_button = tk.Button(app, text="Add Medicine", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=add_medicine_ui)
add_button.pack(pady=10)

# Medicine List Table
columns = ("Name", "Expiry Date", "Days Left", "Finish Date", "Days Left to Finish")
medicines_list = ttk.Treeview(app, columns=columns, show="headings")
for col in columns:
    medicines_list.heading(col, text=col)
    medicines_list.column(col, width=100, anchor="center")
medicines_list.pack(pady=10, fill="both", expand=True)

refresh_medicine_list()
app.mainloop()