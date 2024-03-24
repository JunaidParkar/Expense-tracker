import os
from sqlite3 import connect
from paths import routes, RouteType

class database(routes):
    def __init__(self, username):
        super().__init__(username)

    def handleDirs(self):
        dir_list = self.geDirList()
        for dir in dir_list:
            os.makedirs(dir, exist_ok=True)
            print(f"Directory '{dir}' created successfully.")

    def add_transaction(self, amount, category, description, type, date):
        date = date.split("/")
        main_db = connect(self.getRoute(RouteType.DATABASE_MAIN_DB))
        main_db_cursor = main_db.cursor()
        main_db_cursor.execute('''CREATE TABLE IF NOT EXISTS month_stats (id INTEGER PRIMARY KEY, month TEXT, year REAL, income REAL, expense REAL)''')
        main_db.commit()
        main_db_cursor.execute(f"{routes.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR)}/")

a = database("self")
a.handleDirs()
