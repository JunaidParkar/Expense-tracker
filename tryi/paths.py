import os

DATABASE_DIR = os.path.join(os.getcwd(), "database")
DATABASE_PATH = os.path.join(DATABASE_DIR, "user.db")
EXPENSE_DATABASE_DIR = os.path.join(DATABASE_DIR, "expenses")

SAVINGS_DATABASE_DIR = os.path.join(DATABASE_DIR, "savings")
SAVINGS_DATABASE_PATH = os.path.join(SAVINGS_DATABASE_DIR, "savings.db")