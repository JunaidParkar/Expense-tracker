import sqlite3
import os
from datetime import datetime
from DBMS import saveCategory, saveExpense, getData
from paths import DATABASE_DIR, EXPENSE_DATABASE_DIR
import eel

eel.init("UI")

def createDir(name):
    os.makedirs(name)
    print(f"Directory '{name}' created successfully.")

if not os.path.isdir(DATABASE_DIR):
    createDir(DATABASE_DIR)

if not os.path.isdir(EXPENSE_DATABASE_DIR):
    createDir(EXPENSE_DATABASE_DIR)


# date pattern = yyyy-mm-dd

def storeExpense(amount, description, category, date_of_expense):
    saveCategory(category)
    saveExpense(amount, description, category, date_of_expense)


# storeExpense(20000, "Brought PS5", "gaming", "2024-03-25")
# storeExpense(55999, "Brought Xbox", "gaming", "2020-04-25")
# storeExpense(400, "RFS subscription", "gaming", "2020-03-25")
# storeExpense(6000, "Purchased SSD", "laptop acessories", "2024-02-25")
# storeExpense(100000, "Currency exchange INR to dihram", "workplace", "2024-03-30")
    
def getFiles(year = False, month = False, all = False):
    datas = {}
    if all:
        for item in os.listdir(EXPENSE_DATABASE_DIR):
            item_path = os.path.join(EXPENSE_DATABASE_DIR, item)
            if os.path.isfile(item_path):
                month_data = getData(DB=item)
                datas[item.split(".db")[0]] = month_data
        return datas
    if year is False and month is False:
        return {"Data range not available"}
    
    if not year is False and not month is False:
        datas[year] = getData(year=year, month=month)
        return datas

print(getFiles(year=2024, month="May", all=True))

# eel.start("index.html")