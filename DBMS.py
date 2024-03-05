from sqlite3 import connect
import os
from paths import DATABASE_PATH, EXPENSE_DATABASE_DIR
from datetime import datetime
import calendar

def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date

def saveCategory(name):
    conn = connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, category TEXT)")
    conn.commit()
    cur.execute("SELECT * FROM categories WHERE category=?", (name,))
    existing_category = cur.fetchone()

    if not existing_category:
        cur.execute("INSERT INTO categories (category) VALUES (?)", (name,))
        conn.commit()
    conn.close()

def saveIncome(year, month, income):
    months_array = calendar.month_name[1:]
    conn = connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, year INTEGER, month TEXT, income REAL)")
    conn.commit()
    cur.execute(f"INSERT INTO income (year, month, income) VALUES ({int(year)}, '{str(months_array[int(month) - 1])}', {float(income)})")
    conn.commit()
    conn.close()

def getIncome(year, month):
    months_array = calendar.month_name[1:]
    conn = connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM income WHERE year={int(year)} AND month='{str(months_array[month] - 1)}'")
    rows = cur.fetchall()
    conn.close()
    return rows


def saveExpense(amount, description, category, date_of_expense, type):
    months_array = calendar.month_name[1:]
    de = date_of_expense.split("-")
    conn = connect(os.path.join(EXPENSE_DATABASE_DIR, f'{de[0]}.db'))
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {months_array[int(de[1]) - 1]} (id INTEGER PRIMARY KEY, amount REAL, date_of_expense DATE, category TEXT, description TEXT, date_of_registration DATE, type TEXT)")
    conn.commit()
    current_date = get_current_date()
    query = f"INSERT INTO {months_array[int(de[1]) - 1]} (amount, date_of_expense, category, description, date_of_registration, type) VALUES ({float(amount)}, '{date_of_expense}', '{str(category)}', '{str(description)}', '{current_date}', '{str(type)}')"
    
    cur.execute(query)
    conn.commit()
    conn.close()

def getData(year=False, month=False, DB=False):
    if not DB:
        if not year:
            print("Please provide a year or database name.")
            return None
        conn = connect(os.path.join(EXPENSE_DATABASE_DIR, f"{year}.db"))
    else:
        conn = connect(os.path.join(EXPENSE_DATABASE_DIR, DB))

    cur = conn.cursor()
    all_data = {}

    # Fetch all tables and their data
    if not month and not year:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()

        for table in tables:
            table_name = table[0]
            cur.execute(f"SELECT * FROM {table_name};")
            rows = cur.fetchall()
            all_data[table_name] = rows
    else:
        # Fetch data based on the provided conditions
        if month:
            cur.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()

            for table in tables:
                table_name = table[0]
                if table_name.lower() == month.lower():
                    cur.execute(f"SELECT * FROM {table_name};")
                    rows = cur.fetchall()
                    all_data[table_name] = rows

        elif year:
            cur.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()

            for table in tables:
                table_name = table[0]
                if table_name.startswith(year):
                    cur.execute(f"SELECT * FROM {table_name};")
                    rows = cur.fetchall()
                    all_data[table_name] = rows

    conn.close()

    return all_data
