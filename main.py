import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from functions import open_calendar
from paths import routes
import os

window = ctk.CTk()
# window.overrideredirect(True)
window.title("Expense Tracker")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
js_font = ctk.FontManager.load_font(f"{os.path.join(routes.ASSETS_FONT, "js.ttf")}")

# Set the window size to full screen
window.geometry(f"{screen_width}x{screen_height}+0+0")

# Set the minimum and maximum size of the window
window.minsize(screen_width, screen_height)
window.maxsize(screen_width, screen_height)

# lbl = ctk.CTkLabel(window, text="Hello world")

def clicker(self):
    print(self)
    print("hey")

def cancel_transaction_form(add_transaction_frame):
    add_transaction_frame.destroy()
    
def show_add_transaction_form():
    add_transaction_frame = ctk.CTkLabel(window, width=screen_width, height=screen_height)
    add_transaction_frame.place(x=0, y=0)
    add_transaction_frame.lift()

    add_transaction_frame = ctk.CTkFrame(add_transaction_frame, width=520, height=600, corner_radius=15)
    add_transaction_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    heading = ctk.CTkLabel(add_transaction_frame, text="ADD TRANSACTION,", font=('Century Gothic' if not js_font else js_font,20, "bold"), text_color="#f2b418")
    heading.place(x=25, y=25)

    amount_label = ctk.CTkLabel(add_transaction_frame, text="Enter amount", font=('Century Gothic' if not js_font else js_font,18))
    amount_label.place(x=25, y=80)

    amount_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic' if not js_font else js_font,15))
    amount_input.place(x=25, y=120)

    category_label = ctk.CTkLabel(add_transaction_frame, text="Enter category", font=('Century Gothic' if not js_font else js_font,18))
    category_label.place(x=25, y=170)

    category_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic' if not js_font else js_font,15))
    category_input.place(x=25, y=210)

    description_label = ctk.CTkLabel(add_transaction_frame, text="Enter reason or description", font=('Century Gothic' if not js_font else js_font,18))
    description_label.place(x=25, y=260)

    category_input = ctk.CTkEntry(add_transaction_frame, width=470, font=('Century Gothic' if not js_font else js_font,15))
    category_input.place(x=25, y=300)

    type_label = ctk.CTkLabel(add_transaction_frame, text="Select type of transaction", font=('Century Gothic' if not js_font else js_font,18))
    type_label.place(x=25, y=350)

    category_values_list = ["Check In", "Check Out"]
    category_input = ctk.CTkOptionMenu(add_transaction_frame, width=470, font=('Century Gothic' if not js_font else js_font,15), values=category_values_list)
    category_input.place(x=25, y=390)

    date_label = ctk.CTkLabel(add_transaction_frame, text="Select date of transaction", font=('Century Gothic' if not js_font else js_font,18))
    date_label.place(x=25, y=440)

    date_set_input = tk.StringVar()
    date_input = ctk.CTkEntry(add_transaction_frame, state="readonly", textvariable=date_set_input, width=470, font=('Century Gothic' if not js_font else js_font,15))
    date_input.place(x=25, y=480)
    date_input.bind("<1>", lambda event: open_calendar(ctk, date_set_input, window))

    add_transaction_button_frame = ctk.CTkFrame(add_transaction_frame, width=470)
    add_transaction_button_frame.place(x=25, y=530)

    cancel_button = ctk.CTkButton(add_transaction_button_frame, text="Cancel", fg_color="red", text_color="black", font=('Century Gothic' if not js_font else js_font,15), width=225, height=35, command=lambda: cancel_transaction_form(add_transaction_frame))
    cancel_button.place(x=0, y=0)

    continue_button = ctk.CTkButton(add_transaction_button_frame, text="Continue", font=('Century Gothic' if not js_font else js_font,15), width=225, height=35)
    continue_button.place(x=235, y=0)

main_frame = ctk.CTkFrame(window, width=screen_width-100, height=75, bg_color="transparent", fg_color="transparent")
main_frame.place(x=50, y=0)

main_heading_frame = ctk.CTkFrame(main_frame, width=screen_width-100, height=50, bg_color="transparent", fg_color="transparent")
main_heading_frame.place(x=0, y=25)

main_heading_text = ctk.CTkLabel(main_heading_frame, text="Manage your expenses", font=('Century Gothic' if not js_font else js_font,20, "bold"))
main_heading_text.place(x=0, y=0)
window.update_idletasks()
main_heading_text.place(x=0, y=(main_heading_frame.winfo_height()/2)-(main_heading_text.winfo_height()/2))

main_heading_add_transaction_button = ctk.CTkButton(main_heading_frame, text="Add new transaction", height=35, width=200, font=('Century Gothic' if not js_font else js_font,17, "normal"))
main_heading_add_transaction_button.place(x=0, y=0)
window.update_idletasks()
main_heading_add_transaction_button.place(x=main_frame.winfo_width()-200, y=(main_heading_frame.winfo_height()/2)-17.5)

main_container = ctk.CTkScrollableFrame(window, orientation="vertical", width=screen_width-100, height=screen_height-200, bg_color="transparent", fg_color="transparent")
main_container.place(x=50, y=100)

# Create the year scrollable frame inside the main container
for i in range(3):
    main_year_frame = ctk.CTkScrollableFrame(main_container, orientation="horizontal", width=screen_width-100, height=250, bg_color="transparent", fg_color="transparent", label_text="2025", label_font=('Century Gothic' if not js_font else js_font, 17, "normal"), label_anchor="w")
    main_year_frame.pack(fill="both", expand=True, pady=10)

    # Create the main_month_card frames
    for j in range(10):
        main_month_card = ctk.CTkFrame(main_year_frame, width=200, bg_color="transparent", fg_color="yellow")
        main_month_card.pack(side="left", fill="y", expand=True, padx=15)
        main_month_card.bind("<Button-1>", clicker)

        card_y_offset = 20

        main_month_card_income = ctk.CTkLabel(main_month_card, text="Income = 20000", width=210, font=('Century Gothic' if not js_font else js_font, 17, "normal"), anchor="w", text_color="black")
        main_month_card_income.place(x=20, y=card_y_offset)

        card_y_offset += 50  # Increase y offset for next card

        main_month_card_expense = ctk.CTkLabel(main_month_card, text="Expense = 20000", width=210, font=('Century Gothic' if not js_font else js_font, 17, "normal"), anchor="w", text_color="black")
        main_month_card_expense.place(x=20, y=card_y_offset)

        card_y_offset += 50  # Increase y offset for next card

        main_month_card_savings = ctk.CTkLabel(main_month_card, text="Savings = 20000", width=210, font=('Century Gothic' if not js_font else js_font, 17, "normal"), anchor="w", text_color="black")
        main_month_card_savings.place(x=20, y=card_y_offset)

# main_year_number = ctk.CTkLabel(main_year_frame, text="2025", height=35, font=('Century Gothic' if not js_font else js_font,17, "normal"))
# main_year_number.place(x=0, y=0)

def close_window(event=None):
    window.destroy()

def on_closing():
    open_windows = [child.winfo_name() for child in window.winfo_children() if child.winfo_name() == '!ctktoplevel']
    if len(open_windows) > 0:
        if messagebox.askokcancel("Close Window", "Please close other windows before closing the main window. Continue?"):
            window.destroy()
    else:
        window.destroy()

window.bind("<Escape>", close_window)
window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()