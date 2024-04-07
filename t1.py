from db import Database

a = Database("self")

# a.add_transaction(20000, "salary", "Recieved salary", "pos", "2024-04-07")
print(a.getSpecificMonthStat("2024-04-07"))

# while True:
print("Welcome to the expense tracker sir!!..\n\n")

def ask_user():
    print("What do you want to continue with? Write its appropriate number...\n")
    print("1. Add a transaction.\n")
    print("2. Get all months overall transaction.\n")
    print("3. Get Specific months transaction\n")
    print("4. Exit\n")
    try:
        user_input = int(input(": "))
        return user_input
    except:
        print("\nPlease write number of your option...\n")
        ask_user()

def ask_type():
    print("\nPlease Enter the type of transaction (pos/neg)")
    print("pos means check in amount")
    print("neg means check out amount\n")
    type = input(": ")
    if type.lower() == "pos" or type.lower() == "neg":
        return type
    else:
        ask_type()

def ask_amount():
    amt = input("\nPlease enter the amount: ")
    try:
        amt = round(float(amt), 2)
        return amt
    except:
        print("\nWrite whole amount in numbers....\n")
    

def check_date(date):
    date = date.split("-")
    if len(date) == 2 and len(date[0]) == 3 and int(date[1]) <= 12 and int(date[1]) > 0 and int(date[2]) > 0 and int(date[2]) < 32:
        return True
    else: return False

def check_data(cat, des, type, date):
    mains = False
    if cat is not None or cat is not "" or des is not None or des is not "" or type == "pos" or type == "neg":
        mains == True
    if check_date(date) and mains:
        return True
    else: return False

while True:
    inp = ask_user()
    
    if inp == 1:
        amt = ask_amount()
        cat = input("\nPlease enter the category of transaction: ")
        description = input("\nPlease enter the description of the transaction: ")
        type = ask_type()
        date = input("\nEnter the date of transaction(yyyy-mm-dd): ")

        data_valid = check_data(cat, description, type, date)

        if data_valid:
            a.add_transaction(amt, cat, description, type, date)
        else:
            print("\nDatas are invalid please Re-try again...\n")
    elif inp == 2:
        print(a.getAllMonthStats())
    elif inp == 3:
        date = input("\nEnter the date(yyyy-mm-dd): ")

        if check_date(date):
            print(a.getSpecificMonthStat(date))
        else:
            print("\nInvalid date\n")
    elif inp == 4:
        break