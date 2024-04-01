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

def format_number(number):
    abbreviations = [
        (1e33, 'Dc'), (1e30, 'Nn'), (1e27, 'O'), (1e24, 'Sp'), (1e21, 'Sx'),
        (1e18, 'Qi'), (1e15, 'Q'), (1e12, 'T'), (1e9, 'B'), (1e6, 'M'), (1e3, 'k')
    ]
    for threshold, suffix in abbreviations:
        if number >= threshold:
            formatted_number = "{:.1f}{}".format(number / threshold, suffix)
            if len(formatted_number) <= 5:
                return formatted_number
            else:
                formatted_number = "{:.0f}{}".format(number / threshold, suffix)
                if len(formatted_number) <= 5:
                    return formatted_number
                else:
                    formatted_number = "{:.2f}{}".format(number / threshold, suffix)
                    return formatted_number
    return str(number)

def sort_by_month(data):
    # Define a dictionary to map month names to their corresponding numbers
    month_dict = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    # Define a custom key function to extract the month number from each tuple
    def get_month_number(item):
        month_name = item[1]
        return month_dict[month_name]
    
    # Sort the data using the custom key function
    sorted_data = sorted(data, key=get_month_number)
    return sorted_data

class TransactionModes(Enum):
    INSERT = bin(68115)
    UPDATE = bin(25210)
    DELETE = bin(35650)