import eel
import os
from DBMS import Savings, IncomeExpense
from paths import DATABASE_PATH, EXPENSE_DATABASE_DIR, DATABASE_DIR, SAVINGS_DATABASE_DIR, SAVINGS_DATABASE_PATH

def createDir(name):
    os.makedirs(name)
    print(f"Directory '{name}' created successfully.")

if not os.path.isdir(DATABASE_DIR):
    createDir(DATABASE_DIR)

if not os.path.isdir(EXPENSE_DATABASE_DIR):
    createDir(EXPENSE_DATABASE_DIR)

if not os.path.isdir(SAVINGS_DATABASE_DIR):
    createDir(SAVINGS_DATABASE_DIR)

eel.init("UI")

incomeExpense = IncomeExpense(DATABASE_PATH, EXPENSE_DATABASE_DIR)
savings = Savings(SAVINGS_DATABASE_PATH)

@eel.expose
def getSpecificStats(date):
    data = incomeExpense.getSpecificExpense(date)
    return data

@eel.expose
def getMonthlyStats():
    data = incomeExpense.getMonthlyStat()
    return data



eel.start("index.html")