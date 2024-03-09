import os
from DBMS import DBMS
from paths import DATABASE_PATH, EXPENSE_DATABASE_DIR, DATABASE_DIR
from tryi.paths import SAVINGS_DATABASE_PATH

print(SAVINGS_DATABASE_PATH)

def createDir(name):
    os.makedirs(name)
    print(f"Directory '{name}' created successfully.")

if not os.path.isdir(DATABASE_DIR):
    createDir(DATABASE_DIR)

if not os.path.isdir(EXPENSE_DATABASE_DIR):
    createDir(EXPENSE_DATABASE_DIR)

database = DBMS(DATABASE_PATH, EXPENSE_DATABASE_DIR)