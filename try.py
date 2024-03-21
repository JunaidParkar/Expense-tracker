import customtkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

def submit_expense():
    amount = amount_entry.get()
    description = description_entry.get()
    category = category_var.get()
    date = date_entry.get_date()

    if not amount or not description or not category or not date:
        tk.messagebox.showerror("Error", "All fields are required.")
        return

    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date,
    }

    print(expense)

app = tk.CTk()
app.title("Expense Form")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set the window size to match the screen size
# app.geometry(f"{screen_width}x{screen_height}+0+0")
app.minsize(width=screen_width, height=screen_height)
app.maxsize(width=screen_width, height=screen_height)
# app.attributes("-topmost", True)  # Ensure the window stays on top
app.wm_attributes("-toolwindow", True)

# Create form fields
amount_label = tk.CTkLabel(app, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
amount_entry = tk.CTkEntry(app)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

description_label = tk.CTkLabel(app, text="Description:")
description_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
description_entry = tk.CTkEntry(app)
description_entry.grid(row=1, column=1, padx=5, pady=5)

category_label = tk.CTkLabel(app, text="Category:")
category_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
category_var = tk.StringVar()
category_options = ["Food", "Transportation", "Entertainment", "Other"]
category_optionmenu = tk.CTkOptionMenu(app, variable=category_var, values=category_options)
category_optionmenu.grid(row=2, column=1, padx=5, pady=5)

date_label = tk.CTkLabel(app,text="Date:")
date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
date_entry = DateEntry(app, date_pattern="y-mm-dd")
date_entry.grid(row=3, column=1, padx=5, pady=5)

# Create submit button
submit_button = tk.CTkButton(app, text="Submit", command=submit_expense)
submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, ipadx=10, ipady=5)

app.mainloop()