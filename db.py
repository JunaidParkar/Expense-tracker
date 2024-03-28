import os
from sqlite3 import connect
from paths import routes, RouteType
import calendar
from functions import TransactionModes

class database(routes):
    def __init__(self, username):
        super().__init__(username)
        self.months = calendar.month_name[1:]

    def handleDirs(self):
        dir_list = self.geDirList()
        for dir in dir_list:
            os.makedirs(dir, exist_ok=True)
            print(f"Directory '{dir}' created successfully.")

    def __addMainStats(self, date, amount, type):
        income = amount if type == "pos" else 0
        expense = amount if type == "neg" else 0
        main_db = connect(self.getRoute(RouteType.DATABASE_MAIN_DB))
        main_db_cursor = main_db.cursor()
        main_db_cursor.execute('''CREATE TABLE IF NOT EXISTS month_stats (id INTEGER PRIMARY KEY, month TEXT, year INTEGER, income REAL, expense REAL)''')
        main_db.commit()
        main_db_cursor.execute(f"SELECT * FROM month_stats WHERE year={int(date[0])} AND month='{str(self.months[int(date[1]) - 1])}'")
        dt = main_db_cursor.fetchone()
        if dt is None:
            main_db_cursor.execute(f"INSERT INTO month_stats (month, year, income, expense) VALUES ('{str(self.months[int(date[1]) - 1])}', {int(date[0])}, {round(float(income), 2)}, {round(float(expense), 2)})")
            main_db.commit()
        else:
            d = round(float(round(float(dt[3 if type == 'pos' else 4]) + float(amount), 2)), 2)
            main_db_cursor.execute(f"UPDATE month_stats SET {'expense' if type == 'neg' else 'income'}={d} WHERE year={int(date[0])}, month='{str(self.months[int(date[1]) - 1])}'")
            main_db.commit()
        main_db.close()

    def __updateMainStats(self, date, add_income_amount = 0, add_expense_amount = 0, add_income = False, add_expense = False, remove_income = False, remove_expense = False, prev_amount = 0):
        m_db = connect(self.getRoute(RouteType.DATABASE_MAIN_DB))
        m_db_cursor = m_db.cursor()
        m_db_cursor.execute(f"SELECT * FROM month_stats WHERE year={int(date[0])} AND month='{str(self.months[int(date[1]) - 1])}'")
        m_db_data = m_db_cursor.fetchone()
        if m_db_data is None:
            return False
        old_id, old_month, old_year, old_income, old_expense = m_db_data
        n_i = old_income
        n_e = old_expense
        if add_income:
            n_i = round(round(n_i - round(float(prev_amount), 2), 2) + round(float(add_income_amount), 2), 2)
        if remove_income:
            n_i = round(n_i - round(float(prev_amount), 2), 2)
        if add_expense:
            n_e = round(round(n_e - round(float(prev_amount), 2), 2) + round(float(add_expense_amount), 2), 2)
        if remove_expense:
            n_e = round(n_e - round(float(prev_amount), 2), 2)
            
        m_db_cursor.execute(f"UPDATE month_stats SET income={n_i} AND expense={n_e}")
        m_db.commit()
        m_db.close()
            
        # if prev_type == type:
        #     ...
        # d = old_income - float(prev_amount) if prev_type == type and type == "pos" else old_expense - float(amount) if prev_type == type and type == "neg" else ""
        # n_i = round(round(float(old_income - float(prev_amount)), 2) + float(amount), 2) if prev_type == type and type == "pos" else round(old_income + float(amount), 2) if prev_type != type and type == "pos" else round(old_income - float(amount), 2) if prev_type != type and type == "neg" else old_income
        # n_e = round(round(float(old_expense - float(prev_amount)), 2) + float(amount), 2) if prev_type == type and type == "neg" else round(old_expense + float(amount), 2) if prev_type != type and type == "neg" else round(old_income - float(amount), 2) if prev_type != type and type == "neg" else old_income

    def add_transaction(self, amount, category, description, type, date):
        self.handleDirs()
        date = str(date).split("-")
        self.__addMainStats(date, amount, type)
        ex_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
        ex_db_cursor = ex_db.cursor()
        ex_db_cursor.execute(f"CREATE TABLE IF NOT EXISTS {str(self.months[int(date[1]) - 1])} (id INTEGER PRIMARY KEY, date DATE, amount REAL, type TEXT, category TEXT, description TEXT)")
        ex_db.commit()
        ex_db_cursor.execute(f"INSERT INTO {str(self.months[int(date[1]) - 1])} (date, amount, type, category, description) VALUES ('{"-".join(date)}', {round(float(amount), 2)}, '{str(type)}', '{str(category)}', '{str(description)}')")
        ex_db.commit()
        ex_db_cursor.close()

    def update_transaction(self, id, amount = None, date = None, description = None, category = None, type = None):
        self.handleDirs()
        date = str(date).split("-")
        if os.path.isfile(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db")):
            print("exist")
            master_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
            master_db_cursor = master_db.cursor()
            master_db_cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{str(self.months[int(date[1]) - 1])}'")
            i_data = master_db_cursor.fetchone()
            if i_data is None:
                # deleting stuff here
                # self.__addMainStats(date=date, amount=amount, type=type, mode=TransactionModes.DELETE)
                return
            main_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
            main_db_cursor = main_db.cursor()
            main_db_cursor.execute(f"SELECT * FROM {str(self.months[int(date[1]) - 1])} WHERE id={int(id)}")
            m_data = main_db_cursor.fetchone()
            if m_data is None:
                # deleting stuff here
                return
            i, i_date, i_amount, i_type, i_category, i_description = m_data
            main_db_cursor.execute(f"UPDATE {str(self.months[int(date[1]) - 1])} SET date='{"-".join(date)}', amount={round(float(amount), 2)}, type='{str(type)}', category='{str(category)}', description='{str(description)}' WHERE id={str(id)}")
            main_db.commit()
            if i_type == type:
                if type == "pos":
                    self.__updateMainStats(date=date, add_income_amount=int(amount), add_income=True, prev_amount=i_amount)
                if type == "neg":
                    self.__updateMainStats(date=date, add_expense_amount=int(amount), add_expense=True, prev_amount=i_amount)
            if i_type != type:
                if i_type == "pos" and type == "neg":
                    # self.__updateMainStats(date=date, add_expense_amount=int(amount), add_expense=True, prev_amount=i_amount)
                    self.__updateMainStats(date=date, remove_income=True, prev_amount=i_amount, add_expense=True, add_expense_amount=int(amount))
        else:
            print("not exist")
            # deleting stuff here
            # self.__addMainStats(date=date, amount=amount, type=type, mode=TransactionModes.DELETE, old_type=i_type, old_amount=i_amount)
        # main_db()
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?")
        # self.__addMainStats(date, amount, type, TransactionModes.UPDATE, id=id)


a = database("self")
a.add_transaction(500, "c", "n", "pos", "2024-06-15")
# a.update_transaction(1, 50000, "2024-6-30", "Purchased PS", "gaming", "neg")