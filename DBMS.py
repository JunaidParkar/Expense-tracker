from sqlite3 import connect
import os
from paths import DATABASE_PATH, EXPENSE_DATABASE_DIR, SAVINGS_DATABASE_PATH
from datetime import datetime
import calendar

class DBMS:
    def __init__(self, database_path, expense_database_directory):
        self.__DATABASE_PATH = database_path
        self.__EXPENSE_DATABASE_DIRECTORY = expense_database_directory

    def __get_current_date(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        return current_date
    
    def __get_months_list(self):
        return calendar.month_name[1:]

    def __is_specific_income_available(self, year, month):
        if os.path.isfile(self.__DATABASE_PATH):
            conn = connect(self.__DATABASE_PATH)
            cur = conn.cursor()
            cur.execute(f"SELECT COUNT(*) FROM income WHERE year={int(year)} AND month='{str(self.__get_months_list()[int(month) - 1])}'")
            count = cur.fetchone()[0]
            conn.close()
            return count > 0

    def __is_expense_available(self, file_name, month, id):
        if os.path.isfile(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, file_name)):
            conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, file_name))
            cur = conn.cursor()
            cur.execute(f"SELECT COUNT(*) FROM {self.__get_months_list()[int(month) - 1]} WHERE id='{str(id)}'")
            count = cur.fetchone()[0]
            conn.close()
            return count > 0

    def addIncome(self, amount, date = False):
        date = date.split("-") if not date is False else self.__get_current_date().split("-")
        conn = connect(self.__DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, year INTEGER, month TEXT, income REAL, expense REAL, date DATE)")
        conn.commit()
        cur.execute(f"INSERT INTO income (year, month, income, expense, date) VALUES ({int(date[0])}, '{str(self.__get_months_list()[int(date[1]) - 1])}', {float(amount)}, {float(0.00)}, '{'-'.join(date)}')")
        conn.commit()
        conn.close()

    def addExpense(self, amount, category, description, type = "negative", date = False, edit = False, id = None):
        date = date.split("-") if not date is False else self.__get_current_date().split("-")
        is_income_available = self.__is_specific_income_available(int(date[0]), int(date[1]))
        if is_income_available:
            conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {self.__get_months_list()[int(date[1]) - 1]} (id INTEGER PRIMARY KEY, amount REAL, date_of_expense DATE, category TEXT, description TEXT, date_of_registration DATE, type TEXT)")
            conn.commit()
            if edit:
                is_income_available = self.__is_expense_available(f"{date[0]}.db", date[1], id)
                if not is_income_available:
                    conn.close()
                    return "Can't edit an non existing expense"
            else:
                    cur.execute(f"INSERT into {self.__get_months_list()[int(date[1]) - 1]} (amount, date_of_expense, category, description, date_of_registration, type) VALUES ({float(amount)}, '{"-".join(date)}', '{str(category)}', '{str(description)}', '{str(self.__get_current_date())}', '{str(type)}')")
                    conn.commit()
                    conn.close()
                    conn2 = connect(self.__DATABASE_PATH)
                    cur2 = conn2.cursor()
                    old_value = cur2.execute(f"SELECT {"expense" if type == "negative" else "income"} FROM income WHERE year={int(date[0])} AND month='{str(self.__get_months_list()[int(date[1]) - 1])}'")
                    old_value = old_value.fetchall()[0][0]
                    conn2.commit()
                    new_value = float(old_value) + float(amount)
                    cur2.execute(f"UPDATE income SET {"expense" if type == "negative" else "income"}={float(new_value)} WHERE year={int(date[0])} AND month='{self.__get_months_list()[int(date[1]) - 1]}'")
                    conn2.commit()
                    conn2.close()
        else:
            self.addIncome(0, date)
    
    def getExpense(self, date):
        date = date.split("-")
        conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.__get_months_list()[int(date[1]) - 1]}")
        expenseSet = cur.fetchall()
        conn.commit()
        conn.close()
        return expenseSet

    def getMonthlyStat(self):
        conn = connect(self.__DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM income")
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data

    def trial(self, date = False):
        date = date.split("-") if not date is False else self.__get_current_date().split("-")
        conn2 = connect(self.__DATABASE_PATH)
        cur2 = conn2.cursor()
        hel = cur2.execute(f"SELECT expense FROM income WHERE year={int(date[0])} AND month='{str(self.__get_months_list()[int(date[1]) - 1])}'")
        hel = hel.fetchall()
        conn2.commit()
        conn2.close()
        return hel

class SAVINGSDBMS:
    def __init__(self, saving_databse_path):
        self.SAVING_DATABSE_PATH = saving_databse_path

    def __get_current_date(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        return current_date

    def saveAmount(self, amount, description, type="negative", date=None):
        date = date if not date is None else self.__get_current_date()
        conn = connect(self.SAVING_DATABSE_PATH)
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS savings (id INTEGER PRIMARY KEY, amount REAL, date DATE, description TEXT, type TEXT)")
        conn.commit()
        cur.execute(f"INSERT INTO savings (amount, date, description, type) VALUES ({float(amount)}, '{str(date)}', '{str(description)}', '{str(type)}')")
        conn.commit()
        conn.close()

    def updateAmount(self, id, amount, description, date, type="negative"):
        conn = connect(self.SAVING_DATABSE_PATH)
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS savings (id INTEGER PRIMARY KEY, amount REAL, date DATE, description TEXT, type TEXT)")
        cur.execute(f"UPDATE savings SET amount={float(amount)}, date='{str(date)}', description='{str(description)}', type='{str(type)}' WHERE id={int(id)}")
        conn.commit()
        conn.close()

    def deleteData(self, id):
        conn = connect(self.SAVING_DATABSE_PATH)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM savings WHERE id={int(id)}")
        conn.commit()
        conn.close()



saving = SAVINGSDBMS(SAVINGS_DATABASE_PATH)
# saving.saveAmount(20000, "Salary", "positive")
# saving.saveAmount(15000, "Salary", "positive")
# saving.saveAmount(33000, "food essentials", "negative")
# saving.saveAmount(50000, "clothings", "negative")
# saving.saveAmount(20000, "Salary", "positive")
# saving.saveAmount(45000, "Salary", "positive")

# saving.updateAmount(7, 1000, "Basic ammenities", "2024-02-10")
saving.deleteData(3)


# dbm = DBMS(DATABASE_PATH, EXPENSE_DATABASE_DIR)
# income = dbm.addIncome(200000, "2024-01-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2024-02-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2024-02-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2023-01-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2023-01-23")
# print(income if not income is None else "Income successfully added")

# exp = dbm.addExpense(2000, "gaming", "Purchased GTA V", "negative", id=2, date="2024-01-20")
# print(exp)
# exp = dbm.addExpense(2000, "gaming", "Purchased GTA V", "negative", id=2, date="2024-02-20")
# print(exp)
# exp = dbm.addExpense(2000, "gaming", "Purchased GTA V", "negative", id=2, date="2024-02-20")
# print(exp)
# exp = dbm.addExpense(2000, "gaming", "Purchased GTA V", "negative", id=2, date="2023-01-20")
# print(exp)
# exp = dbm.addExpense(2000, "gaming", "Purchased GTA V", "negative", id=2, date="2023-01-23")
# print(exp)
# exp = dbm.addExpense(10000, "gaming", "Purchased GTA V", "negative", id=2, date="2024-01-23")
# print(exp)
# exp = dbm.addExpense(1000, "rent", "Company rent", "positive", date="2024-01-23")
# print(exp)


# print(dbm.trial("2024-02-20")[0][0])


# income = dbm.addIncome(200000, "2024-01-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2024-02-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2024-02-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2023-01-20")
# print(income if not income is None else "Income successfully added")
# income = dbm.addIncome(200000, "2023-01-23")
# print(income if not income is None else "Income successfully added")

# print(exp)

# expense = dbm.getExpense("2024-01-20")
# print(expense)

# ms = dbm.getMonthlyStat()
# print([list(t) for t in ms])