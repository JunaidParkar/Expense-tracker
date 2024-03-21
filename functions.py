from tkcalendar import Calendar
from datetime import datetime

def open_calendar(tk, selected_date, window):
    def select_date():
        selected_date.set(cal.get_date())
        top.destroy()

    top = tk.CTkToplevel(window)
    top.wm_transient(window)
    top.title("Expense Tracker")
    today = datetime.today().date()
    cal = Calendar(top, selectmode="none", maxdate=today)
    cal.pack(padx=10, pady=10)

    select_button = tk.CTkButton(top, text="Select", command=select_date)
    select_button.pack(pady=10)