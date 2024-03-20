from sqlite3 import connect
import os
from datetime import datetime
import calendar


class Common:
    def __init__(self):
        pass

    def get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')
    
    def get_months_list(self):
        return calendar.month_name[1:]

class IncomeExpense(Common):
    def __init__(self, database_path, expense_database_dir):
        super().__init__()
        self.__DATABASE_PATH = database_path
        self.__EXPENSE_DATABASE_DIRECTORY = expense_database_dir

    def __is_specific_income_available(self, year, month):
        if os.path.isfile(self.__DATABASE_PATH):
            conn = connect(self.__DATABASE_PATH)
            cur = conn.cursor()
            cur.execute(f"SELECT COUNT(*) FROM income WHERE year={int(year)} AND month='{str(self.get_months_list()[int(month) - 1])}'")
            count = cur.fetchone()[0]
            conn.close()
            return count > 0

    def addIncome(self, amount, date=None):
        date = date.split("-") if date else self.get_current_date().split("-")
        conn = connect(self.__DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, year INTEGER, month TEXT, income REAL, expense REAL, date DATE)")
        cur.execute(f"INSERT INTO income (year, month, income, expense, date) VALUES ({int(date[0])}, '{str(self.get_months_list()[int(date[1]) - 1])}', {round(float(amount), 2)}, {round(float(0.00), 2)}, '{'-'.join(date)}')")
        conn.commit()
        conn.close()

    def addExpense(self, amount, category, description, type="negative", date=None):
        amount = round(float(amount), 2)
        date = date.split("-") if date else self.get_current_date().split("-")
        is_income_available = self.__is_specific_income_available(int(date[0]), int(date[1]))
        if not is_income_available:
            self.addIncome(0.00, "-".join(date))
        conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS {self.get_months_list()[int(date[1]) - 1]} (id INTEGER PRIMARY KEY, amount REAL, date_of_expense DATE, category TEXT, description TEXT, date_of_registration DATE, type TEXT)")
        cur.execute(f"INSERT INTO {self.get_months_list()[int(date[1]) - 1]} (amount, date_of_expense, category, description, date_of_registration, type) VALUES ({round(float(amount), 2)}, '{"-".join(date)}', '{str(category)}', '{str(description)}', '{str(self.get_current_date())}', '{str(type)}')")
        conn.commit()
        conn.close()
        conn2 = connect(self.__DATABASE_PATH)
        cur2 = conn2.cursor()
        old_value = cur2.execute(f"SELECT {'expense' if type == 'negative' else 'income'} FROM income WHERE year={int(date[0])} AND month='{str(self.get_months_list()[int(date[1]) - 1])}'").fetchall()[0][0]
        new_value = float(old_value) + float(amount)
        cur2.execute(f"UPDATE income SET {'expense' if type == 'negative' else 'income'}={round(float(new_value), 2)} WHERE year={int(date[0])} AND month='{self.get_months_list()[int(date[1]) - 1]}'")
        conn2.commit()
        conn2.close()

    def getSpecificExpense(self, date):
        date = date.split("-")
        conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.get_months_list()[int(date[1]) - 1]}")
        expense = cur.fetchall()
        conn.close()
        return expense

    def deleteExpense(self, date, expense_id):
        date = date.split("-")
        conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {self.get_months_list()[int(date[1]) - 1]} WHERE id={expense_id}")
        conn.commit()
        conn.close()

    def editExpense(self, date, expense_id, amount, category, description, expense_type):
        date = date.split("-")
        conn = connect(os.path.join(self.__EXPENSE_DATABASE_DIRECTORY, f"{date[0]}.db"))
        cur = conn.cursor()
        cur.execute(f"UPDATE {self.get_months_list()[int(date[1]) - 1]} SET amount={round(amount, 2)}, category='{category}', description='{description}', type='{expense_type}' WHERE id={expense_id}")
        conn.commit()
        conn.close()

    def getMonthlyStat(self):
        if os.path.isfile(self.__DATABASE_PATH):
            conn = connect(self.__DATABASE_PATH)
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, year INTEGER, month TEXT, income REAL, expense REAL, date DATE)")
            conn.commit()
            cur.execute("SELECT * FROM income")
            data = cur.fetchall()
            conn.close()
        else:
            data = None
        return data

class Savings:
    def __init__(self, saving_databse_path):
        self.SAVING_DATABSE_PATH = saving_databse_path

    def get_current_date(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        return current_date

    def saveAmount(self, amount, description, type="negative", date=None):
        date = date if not date is None else self.get_current_date()
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