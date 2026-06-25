
from users import add_expense, load_data
from users import add_income
from users import add_user,users,save_data

print("Hello")
print("Your Budget Tracker")
print("1.Create a new account")
print("2.Login to existing account")
load_data()
choice = input("Enter your choice: ")
#When a user creates a new account
if choice == "1":
    name_1 = input("What is your name? ")
    password_1 = input("What is your password? ")
    add_user(name_1, password_1)
    save_data()
    print("Account created successfully.")
    print(f"Welcome, {name_1}!")
    print("1.Add an expense")
    print("2.Add an income")
    account_choice = input("Enter your choice: ")
    
       
    if account_choice == "1":
            while True:
               name_expense = input("Enter the name of the expense or type 'end' to finish: ")
               if name_expense.lower() == 'end':
                  break
               amount_exp = float(input("Enter the amount of the expense: "))
               add_expense(name_1, name_expense, amount_exp)
               save_data()
             
    elif account_choice == "2":
            while True:
                name_income = input("Enter the name of the income or type 'end' to finish: ")
                if name_income.lower() == 'end':
                    break
                
                    
                amount_in = float(input("Enter the amount of the income: "))
                add_income(name_1, name_income, amount_in)
    
                save_data()
               
    total_expenses = sum(users[name_1]['expenses'].values())
    total_incomes = sum(users[name_1]['incomes'].values())
    balance = total_incomes - total_expenses

    print(f"Total expenses: ${total_expenses}")
    print(f"Total incomes: ${total_incomes}")
    print(f"Balance: ${balance}")
           
#Login staffs    
elif choice == "2":
    name = input("What is your name? ")
    password = input("What is your password? ")
    
    if name in users and users[name]['password'] == password:
        print("Login successful.")
        print(f"Welcome back, {name}!")
        print("1.Add an expense")
        print("2.Add an income")
        print("3.View budget summary")
        login_choice = input("Enter your choice: ")
        if login_choice == "1":
            while True:
               name_expense = input("Enter the name of the expense or type 'end' to finish: ")
               if name_expense.lower() == 'end':
                  break
               amount_exp = float(input("Enter the amount of the expense: "))
               add_expense(name, name_expense, amount_exp)
               save_data()
            print("Your expense sources are:")
            for source in users[name]['expenses']:
                print(f"  - {source}")
            total_expenses = sum(users[name]['expenses'].values())  
            print(f"Total expenses: ${total_expenses}")  
        elif login_choice == "2":
            while True:
                name_income = input("Enter the name of the income or type 'end' to finish: ")
                if name_income.lower() == 'end':
                    break
                
                    
                amount_in = float(input("Enter the amount of the income: "))
                add_income(name, name_income, amount_in)
                save_data()
            print("Your income sources are:")
            for source in users[name]['incomes']:
                print(f"  - {source}")
            total_incomes = sum(users[name]['incomes'].values())  
            print(f"Total incomes: ${total_incomes}")  
        elif login_choice == "3":
            total_expenses = sum(users[name]['expenses'].values())
            total_incomes = sum(users[name]['incomes'].values())
            balance = total_incomes - total_expenses

            print(f"Total expenses: ${total_expenses}")
            print(f"Total incomes: ${total_incomes}")
            print(f"Balance: ${balance}")
            if balance < 0:
             print(f"{name.capitalize()}, you are in debt.")
            else:
             print(f"{name.capitalize()}, you are financially stable.")
    else:
        print("Invalid credentials.")
        exit()
else:
    print("Invalid choice.")
    exit()
#End of the login    
"""
while True:
    name_expense = input("Enter the name of the expense or type 'end' to finish: ")
    if name_expense.lower() == 'end':
        while True:
            name_income = input("Enter the name of the income or type 'end' to finish: ")
            if name_income.lower() == 'end':
                break
            amount_in = float(input("Enter the amount of the income: "))
            add_income(name,name_income, amount_in)
            save_data()
            #print(incomes)
        break
    amount_exp = float(input("Enter the amount of the expense: "))
    add_expense(name,name_expense, amount_exp)
    save_data()
    """
"""
total_expenses = sum(users[name]['expenses'].values())
total_incomes = sum(users[name]['incomes'].values())
balance = total_incomes - total_expenses
"""
"""
print(f"Total expenses: ${total_expenses}")
print(f"Total incomes: ${total_incomes}")
print(f"Balance: ${balance}")
"""
#print(users)
save_data()

