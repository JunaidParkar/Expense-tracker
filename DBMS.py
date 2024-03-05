from sqlite3 import connect
import os
from paths import DATABASE_PATH, EXPENSE_DATABASE_DIR
from datetime import datetime
import calendar

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

def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date

def saveExpense(amount, description, category, date_of_expense):
    months_array = calendar.month_name[1:]
    print(months_array)
    de = date_of_expense.split("-")
    conn = connect(os.path.join(EXPENSE_DATABASE_DIR, f'{de[0]}.db'))
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {months_array[int(de[1])]} (id INTEGER PRIMARY KEY, amount REAL, date_of_expense DATE, category TEXT, description TEXT, date_of_registration DATE)")
    conn.commit()
    current_date = get_current_date()
    
    # Manually format string values and enclose them in single quotes
    query = f"INSERT INTO {months_array[int(de[1])]} (amount, date_of_expense, category, description, date_of_registration) VALUES ({float(amount)}, '{date_of_expense}', '{str(category)}', '{str(description)}', '{current_date}')"
    
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
