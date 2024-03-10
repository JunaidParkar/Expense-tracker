import eel
import os
import random
from DBMS import IncomeExpenseTracker, Savings, IncomeExpense
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

incomeExpense = IncomeExpenseTracker(DATABASE_PATH, EXPENSE_DATABASE_DIR)
savings = Savings(SAVINGS_DATABASE_PATH)

@eel.expose
def getSpecificStats(date):
    data = incomeExpense.getSpecificExpense(date)
    return data

@eel.expose
def getMonthlyStats():
    data = incomeExpense.getMonthlyStat()
    return data

# Instantiate the IncomeExpenseTracker class
# tracker = IncomeExpense(DATABASE_PATH, EXPENSE_DATABASE_DIR)

# # Year 2022
# for month in range(1, 13):  # Months are from 1 to 12
#     # Example data for expenses
#     tracker.addExpense(random.uniform(50, 200), "Rent", "Monthly rent payment", "negative", f"2022-{month:02d}")
#     tracker.addExpense(random.uniform(20, 100), "Utilities", "Electricity bill", "negative", f"2022-{month:02d}")
#     tracker.addExpense(random.uniform(50, 300), "Groceries", "Monthly grocery shopping", "negative", f"2022-{month:02d}")
#     # Example data for income
#     tracker.addIncome(random.uniform(100, 5000), f"2022-{month:02d}")

# # Year 2023
# for month in range(1, 13):
#     tracker.addExpense(random.uniform(50, 200), "Rent", "Monthly rent payment", "negative", f"2023-{month:02d}")
#     tracker.addExpense(random.uniform(20, 100), "Utilities", "Electricity bill", "negative", f"2023-{month:02d}")
#     tracker.addExpense(random.uniform(50, 300), "Groceries", "Monthly grocery shopping", "negative", f"2023-{month:02d}")
#     tracker.addIncome(random.uniform(100, 5000), f"2023-{month:02d}")

# # Year 2024
# for month in range(1, 13):
#     tracker.addExpense(random.uniform(50, 200), "Rent", "Monthly rent payment", "negative", f"2024-{month:02d}")
#     tracker.addExpense(random.uniform(20, 100), "Utilities", "Electricity bill", "negative", f"2024-{month:02d}")
#     tracker.addExpense(random.uniform(50, 300), "Groceries", "Monthly grocery shopping", "negative", f"2024-{month:02d}")
#     tracker.addIncome(random.uniform(100, 5000), f"2024-{month:02d}")

# print("Expenses and income added successfully.")


eel.start("index.html")