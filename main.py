import customtkinter as ctk
from customtkinter import ctk_tk
import tkinter as tk
from tkinter import messagebox
from functions import open_calendar

window = ctk.CTk()
# window.overrideredirect(True)
window.title("Expense Tracker")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to full screen
window.geometry(f"{screen_width}x{screen_height}+0+0")

# Set the minimum and maximum size of the window
window.minsize(screen_width, screen_height)
window.maxsize(screen_width, screen_height)

# lbl = ctk.CTkLabel(window, text="Hello world")

def cancel_transaction_form(add_transaction_frame):
    add_transaction_frame.destroy()
# lbl.pack()
    
def show_add_transaction_form():
    mainDiv = ctk.CTkLabel(window, width=screen_width, height=screen_height)
    mainDiv.place(x=0, y=0)
    mainDiv.lift()

    add_transaction_frame = ctk.CTkFrame(mainDiv, bg_color="red", width=520, height=600, corner_radius=15)
    add_transaction_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    heading = ctk.CTkLabel(add_transaction_frame, text="ADD TRANSACTION,", font=('Century Gothic',20, "bold"), text_color="#f2b418")
    heading.place(x=25, y=25)

    amount_label = ctk.CTkLabel(add_transaction_frame, text="Enter amount", font=('Century Gothic',18))
    amount_label.place(x=25, y=80)

    amount_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic',15))
    amount_input.place(x=25, y=120)

    category_label = ctk.CTkLabel(add_transaction_frame, text="Enter category", font=('Century Gothic',18))
    category_label.place(x=25, y=170)

    category_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic',15))
    category_input.place(x=25, y=210)

    description_label = ctk.CTkLabel(add_transaction_frame, text="Enter reason or description", font=('Century Gothic',18))
    description_label.place(x=25, y=260)

    category_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic',15))
    category_input.place(x=25, y=300)

    type_label = ctk.CTkLabel(add_transaction_frame, text="Select type of transaction", font=('Century Gothic',18))
    type_label.place(x=25, y=350)

    category_values_list = ["Check In", "Check Out"]
    category_input = ctk.CTkOptionMenu(add_transaction_frame, width=470, font=('Century Gothic',15), values=category_values_list)
    category_input.place(x=25, y=390)

    date_label = ctk.CTkLabel(add_transaction_frame, text="Select date of transaction", font=('Century Gothic',18))
    date_label.place(x=25, y=440)

    date_set_input = tk.StringVar()
    date_input = ctk.CTkEntry(add_transaction_frame, state="readonly", textvariable=date_set_input, width=470, font=('Century Gothic',15))
    date_input.place(x=25, y=480)
    date_input.bind("<1>", lambda event: open_calendar(ctk, date_set_input, window))

    add_transaction_button_frame = ctk.CTkFrame(add_transaction_frame, width=470)
    add_transaction_button_frame.place(x=25, y=530)

    cancel_button = ctk.CTkButton(add_transaction_button_frame, text="Cancel", fg_color="red", text_color="black", font=('Century Gothic',15), width=225, height=35, command=lambda: cancel_transaction_form(mainDiv))
    cancel_button.place(x=0, y=0)

    continue_button = ctk.CTkButton(add_transaction_button_frame, text="Continue", font=('Century Gothic',15), width=225, height=35)
    continue_button.place(x=235, y=0)

show_add_transaction_form()

def close_window(event=None):
    window.destroy()

def on_closing():
    open_windows = window.winfo_children()
    if len(open_windows) > 1:
        if messagebox.askokcancel("Close Window", "Please close other windows before closing the main window. Continue?"):
            window.destroy()
    else:
        window.destroy()

window.bind("<Escape>", close_window)
window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()