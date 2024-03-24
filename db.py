import os
from sqlite3 import connect
from paths import routes, RouteType
import calendar

class database(routes):
    def __init__(self, username):
        super().__init__(username)
        self.months = calendar.month_name[1:]

    def handleDirs(self):
        dir_list = self.geDirList()
        for dir in dir_list:
            os.makedirs(dir, exist_ok=True)
            print(f"Directory '{dir}' created successfully.")

    def __addMainStats(self, date, amount):
        income = amount if type == "pos" else 0
        expense = amount if type == "neg" else 0
        main_db = connect(self.getRoute(RouteType.DATABASE_MAIN_DB))
        main_db_cursor = main_db.cursor()
        main_db_cursor.execute('''CREATE TABLE IF NOT EXISTS month_stats (id INTEGER PRIMARY KEY, month TEXT, year INTEGER, income REAL, expense REAL)''')
        main_db.commit()
        main_db_cursor.execute(f"SELECT * FROM month_stats WHERE year={int(date[0])} AND month='{str(self.months[int(date[1]) - 1])}'")
        dt = main_db_cursor.fetchone()
        print(dt)
        if dt is None:
            main_db_cursor.execute(f"INSERT INTO month_stats (month, year, income, expense) VALUES ('{str(self.months[int(date[1]) - 1])}', {int(date[0])}, {round(float(income), 2)}, {round(float(expense), 2)})")
            main_db.commit()
            main_db.close()
        else:
            print(dt)
            main_db_cursor.execute(f"UPDATE month_stats SET {'expense' if type == 'neg' else 'income'}={round(float(round(float(dt[3 if type == "pos" else 4]) + float(amount), 2)), 2)}")
            main_db.commit()
            main_db.close()

    def add_transaction(self, amount, category, description, type, date, mode = ""):
    # self.handleDirs()
        date = date.split("-")
        self.__addMainStats(date, amount)
        ex_db = connect(os.path.join(routes.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR), f"{date[0]}.db"))
        ex_db_cursor = ex_db.execute("CREATE TABLE IF NOT EXISTS month_stats (id INTEGER PRIMARY KEY, date DATE, amount REAL, type TEXT, category TEXT, description TEXT)")
        ex_db.commit()

        


        # exp_db = connect(f"{routes.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR)}/{date[0]}.db")

a = database("self")
a.add_transaction(500.5066, "c", "n", "neg", "2024-07-15")

# print(calendar.month_name[1:])
        
# print((0.0, 0.0))