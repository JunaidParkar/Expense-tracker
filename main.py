import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from functions import open_calendar, format_number, sort_by_month
from paths import routes, RouteType
import os
from db import Database

database = Database("self")

router = routes("self")
window = ctk.CTk()
# window.overrideredirect(True)
window.title("Expense Tracker")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
js_font = ctk.FontManager.load_font(f"{os.path.join(router.getRoute(RouteType.ASSETS_FONT_DIR), "js.ttf")}")
window.geometry(f"{screen_width}x{screen_height}+0+0")
window.minsize(screen_width, screen_height)
window.maxsize(screen_width, screen_height)

def set_on_click(widget, data):
    widget.bind("<Button-1>", lambda e: clicker(data))
    for child in widget.winfo_children():
        set_on_click(child, data)

def set_cursor_to_pointer(widget):
    widget.configure(cursor="hand2")
    for child in widget.winfo_children():
        set_cursor_to_pointer(child) 


def clicker(dataf):
    # print(self)
    print(dataf)
    print("hey")

def cancel_transaction_form(add_transaction_frame, frame_to_show_on_over):
    add_transaction_frame.destroy()
    frame_to_show_on_over()
    
def show_add_transaction_form(frame_to_destroy, frame_to_show_on_over):
    frame_to_destroy.destroy() if frame_to_destroy else ...
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

    date_set_input = ctk.StringVar()
    date_input = ctk.CTkEntry(add_transaction_frame, placeholder_text="Click here to select the date", width=470, font=('Century Gothic' if not js_font else js_font,15))
    date_input.place(x=25, y=480)
    def setVal(v):
        date_input.configure(textvariable = date_set_input)
        date_set_input.set(v)
        date_input.configure(textvariable = None)
    # date_input.configure(textvariable = date_set_input)
    date_input.bind("<1>", lambda event: open_calendar(ctk, setVal, window))

    add_transaction_button_frame = ctk.CTkFrame(add_transaction_frame, width=470)
    add_transaction_button_frame.place(x=25, y=530)

    cancel_button = ctk.CTkButton(add_transaction_button_frame, text="Cancel", fg_color="red", text_color="black", font=('Century Gothic' if not js_font else js_font,15), width=225, height=35, command=lambda: cancel_transaction_form(add_transaction_frame, frame_to_show_on_over))
    cancel_button.place(x=0, y=0)

    continue_button = ctk.CTkButton(add_transaction_button_frame, text="Continue", font=('Century Gothic' if not js_font else js_font,15), width=225, height=35)
    continue_button.place(x=235, y=0)

def mainPage():
    main_frame = ctk.CTkFrame(window, width=screen_width-100, height=75, bg_color="transparent", fg_color="transparent")
    main_frame.place(x=50, y=0)

    main_heading_frame = ctk.CTkFrame(main_frame, width=screen_width-100, height=50, bg_color="transparent", fg_color="transparent")
    main_heading_frame.place(x=0, y=25)

    main_heading_text = ctk.CTkLabel(main_heading_frame, text="Manage your expenses", font=('Century Gothic' if not js_font else js_font,20, "bold"))
    main_heading_text.place(x=0, y=0)
    window.update_idletasks()
    main_heading_text.place(x=0, y=(main_heading_frame.winfo_height()/2)-(main_heading_text.winfo_height()/2))

    main_heading_add_transaction_button = ctk.CTkButton(main_heading_frame, text="Add new transaction", height=35, width=200, font=('Century Gothic' if not js_font else js_font,17, "normal"), command=lambda e=None: show_add_transaction_form(main_frame, mainPage))
    window.update_idletasks()
    main_heading_add_transaction_button.place(x=screen_width-300, y=25-17.5)

    main_container = ctk.CTkScrollableFrame(window, orientation="vertical", width=screen_width-100, height=screen_height-200, bg_color="transparent", fg_color="transparent")
    main_container.place(x=50, y=100)

    monthly_data = database.getAllMonthStats()

    for year, datas in monthly_data.items():
            datas = sort_by_month(datas)
            main_year_frame = ctk.CTkScrollableFrame(main_container, orientation="horizontal", width=screen_width-100, height=260, bg_color="transparent", fg_color="transparent", label_text=year, label_font=('Century Gothic' if not js_font else js_font, 17, "normal"), label_anchor="w")
            main_year_frame.pack(fill="both", expand=True)
            for data in datas:
                saving = format_number(round(float(data[3]) - float(data[4]), 2))
                main_month_card = ctk.CTkFrame(main_year_frame, width=300)
                main_month_card.pack(side="left", fill="y", expand=True, padx=15)

                main_month_name = ctk.CTkLabel(main_month_card, text=data[1], width=280, anchor="w", text_color="#f2b418", font=('Century Gothic' if not js_font else js_font, 20, "normal"))
                main_month_name.place(x=10, y=10)

                main_month_saving_frame = ctk.CTkFrame(main_month_card, width=280, height=80, bg_color="transparent", fg_color="transparent")
                main_month_saving_frame.place(x=10, y=50)

                main_month_saving_heading = ctk.CTkLabel(main_month_saving_frame, text="Available savings", width=280, font=('Century Gothic' if not js_font else js_font, 20, "normal"))
                main_month_saving_heading.place(x=0, y=10)

                main_month_saving_amount = ctk.CTkLabel(main_month_saving_frame, text=saving, width=280, font=('Century Gothic' if not js_font else js_font, 17, "normal"))
                main_month_saving_amount.place(x=0, y=40)

                main_month_income_frame = ctk.CTkFrame(main_month_card, width=280, height=50, bg_color="transparent", fg_color="#4C7A9E")
                main_month_income_frame.place(x=10, y=130)

                main_month_income_label = ctk.CTkLabel(main_month_income_frame, text="Income", width=120, height=50, anchor="w", font=('Century Gothic' if not js_font else js_font, 17, "normal"))
                main_month_income_label.place(x=10, y=0)

                main_month_income_amount = ctk.CTkLabel(main_month_income_frame, text=format_number(data[3]), width=120, height=50, anchor="e", font=('Century Gothic' if not js_font else js_font, 17, "normal"))
                main_month_income_amount.place(x=280-130)


                main_month_expense_frame = ctk.CTkFrame(main_month_card, width=280, height=50, bg_color="transparent", fg_color="#8E5757")
                main_month_expense_frame.place(x=10, y=190)

                main_month_expense_label = ctk.CTkLabel(main_month_expense_frame, text="Expense", width=120, height=50, anchor="w", font=('Century Gothic' if not js_font else js_font, 17, "normal"))
                main_month_expense_label.place(x=10, y=0)

                main_month_expense_amount = ctk.CTkLabel(main_month_expense_frame, text=format_number(data[4]), width=120, height=50, anchor="e", font=('Century Gothic' if not js_font else js_font, 17, "normal"))
                main_month_expense_amount.place(x=280-130)

                set_cursor_to_pointer(main_month_card)
                set_on_click(main_month_card, (year, data[1]))

def close_window(event=None):
    window.destroy()

mainPage()

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