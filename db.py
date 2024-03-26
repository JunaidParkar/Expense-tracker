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

    def __handleMainStats(self, date, amount, type, mode):
        income = amount if type == "pos" else 0
        expense = amount if type == "neg" else 0
        main_db = connect(self.getRoute(RouteType.DATABASE_MAIN_DB))
        main_db_cursor = main_db.cursor()
        main_db_cursor.execute('''CREATE TABLE IF NOT EXISTS month_stats (id INTEGER PRIMARY KEY, month TEXT, year INTEGER, income REAL, expense REAL)''')
        main_db.commit()
        main_db_cursor.execute(f"SELECT * FROM month_stats WHERE year={int(date[0])} AND month='{str(self.months[int(date[1]) - 1])}'")
        dt = main_db_cursor.fetchone()
        if dt is None:
            if mode == TransactionModes.UPDATE or mode == TransactionModes.DELETE:
                return
            main_db_cursor.execute(f"INSERT INTO month_stats (month, year, income, expense) VALUES ('{str(self.months[int(date[1]) - 1])}', {int(date[0])}, {round(float(income), 2)}, {round(float(expense), 2)})")
            main_db.commit()
            main_db.close()
        else:
            if mode == TransactionModes.INSERT:
                d = round(float(round(float(dt[3 if type == 'pos' else 4]) + float(amount), 2)), 2)
                main_db_cursor.execute(f"UPDATE month_stats SET {'expense' if type == 'neg' else 'income'}={d} WHERE year={int(date[0])}, month='{str(self.months[int(date[1]) - 1])}'")
                main_db.commit()
            elif mode == TransactionModes.UPDATE:
                d = round(float(round(float(dt[3 if type == 'pos' else 4]) + float(amount), 2)), 2)
                ...
            elif mode == TransactionModes.DELETE:
                print(dt)
            main_db.close()

    def add_transaction(self, amount, category, description, type, date):
        self.handleDirs()
        date = str(date).split("-")
        self.__handleMainStats(date, amount, type, TransactionModes.INSERT)
        ex_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
        ex_db_cursor = ex_db.cursor()
        ex_db_cursor.execute(f"CREATE TABLE IF NOT EXISTS {str(self.months[int(date[1]) - 1])} (id INTEGER PRIMARY KEY, date DATE, amount REAL, type TEXT, category TEXT, description TEXT)")
        ex_db.commit()
        ex_db_cursor.execute(f"INSERT INTO {str(self.months[int(date[1]) - 1])} (date, amount, type, category, description) VALUES ('{"-".join(date)}', {round(float(amount), 2)}, '{str(type)}', '{str(category)}', '{str(description)}')")
        ex_db.commit()
        ex_db_cursor.close()

    def update_transaction(self, id, amount = None, date = None, income = None, expense = None, description = None, category = None, type = None):
        self.handleDirs()
        date = str(date).split("-")
        if os.path.isfile(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db")):
            print("exist")
            master_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
            master_db_cursor = master_db.cursor()
            master_db_cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{str(self.months[int(date[1]) - 1])}'")
            i_data = master_db_cursor.fetchone()
            if i_data is None:
                self.__handleMainStats(date=date, amount=amount, type=type, mode=TransactionModes.DELETE)
                return
            main_db = connect(os.path.join(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
            main_db_cursor = main_db.cursor()
            main_db_cursor.execute(f"SELECT * FROM {str(self.months[int(date[1]) - 1])} WHERE id={str(id)}")
            m_data = main_db_cursor.fetchone()
            print(m_data)
            if m_data is None:
                return
            i, i_date, i_amount, i_type, i_category, i_description = m_data
            main_db_cursor.execute(f"UPDATE {str(self.months[int(date[1]) - 1])} SET date='{"-".join(i_date)}', amount={round(float(i_amount), 2)}, type='{i_type}, ' WHERE id={str(id)}")
        else:
            print("not exist")
            self.__handleMainStats(date=date, amount=amount, type=type, mode=TransactionModes.DELETE)
        # main_db()
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?")
        # self.__handleMainStats(date, amount, type, TransactionModes.UPDATE, id=id)


a = database("self")
# a.add_transaction(500, "c", "n", "pos", "2024-06-15")
a.update_transaction(1, 2000, "2024-07-30", 25000, 200, "vrjv", "uv4ioj", "pos")