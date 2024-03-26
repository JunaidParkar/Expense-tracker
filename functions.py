from tkcalendar import Calendar
from datetime import datetime
from enum import Enum

def open_calendar(tk, selected_date, window):
    def select_date():
        selected_date(cal.get_date())
        # selected_date.set(cal.get_date())
        top.destroy()

    top = tk.CTkToplevel(window)
    top.wm_transient(window)
    top.title("Expense Tracker")
    today = datetime.today().date()
    print(today)
    cal = Calendar(top, selectmode="day", maxdate=today, fieldbackground='light green',
                background='dark green',
                foreground='dark blue',
                arrowcolor='white',
                date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    select_button = tk.CTkButton(top, text="Select", command=select_date)
    select_button.pack(pady=10)

class TransactionModes(Enum):
    INSERT = bin(68115)
    UPDATE = bin(25210)
    DELETE = bin(35650)