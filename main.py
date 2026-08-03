
from users import add_expense, load_data, validate_password, validate_username
from users import add_income,delete_expense,delete_income
from users import add_user,users,save_data

print("Hello")
print("Your Budget Tracker")
print("1.Create a new account")
print("2.Login to existing account")
load_data()
choice = input("Enter your choice: ")
#When a user creates a new account
if choice == "1":
    name_1 = input("Enter your username? ")
    if name_1.title() in users:
        print("Username already exists. Please choose a different username.")
        exit()
    elif not validate_username(name_1):
        print("Username does not meet the requirements.")
        exit()       
    password_1 = input("Enter your password(6 digits required): ")
    if not validate_password(password_1):
        print("Password does not meet the requirements.")
        exit()
    
    add_user(name_1.title(), password_1)
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
               add_expense(name_1.title(), name_expense, amount_exp)
               save_data()
             
    elif account_choice == "2":
            while True:
                name_income = input("Enter the name of the income or type 'end' to finish: ")
                if name_income.lower() == 'end':
                    break
                
                    
                amount_in = float(input("Enter the amount of the income: "))
                add_income(name_1.title(), name_income, amount_in)
    
                save_data()
               
    total_expenses = sum(users[name_1.title()]['expenses'].values())
    total_incomes = sum(users[name_1.title()]['incomes'].values())
    balance = total_incomes - total_expenses

    print(f"Total expenses: ${total_expenses}")
    print(f"Total incomes: ${total_incomes}")
    print(f"Balance: ${balance}")
           
#Login staffs    
elif choice == "2":
    name = input("Enter the  username? ")
    password = input("Enter the password? ")
    #load_data()
    if name in users and users[name]['password'] == password:
        print("Login successful.")
        print(f"Welcome back, {name}!")
        print("1. Expenses")
        print("2. Incomes")
        print("3. View budget summary")
        print("4. Profile")
        print("5. Exit")
        login_choice = input("Enter your choice: ")
        if login_choice == "1":
            print("1.Add an expense")
            print("2.Delete an expense")
            expense_choice = input("Enter your choice (add or delete): ")
            if expense_choice == "1" or expense_choice.lower() == "add":
                while True:
                    name_expense = input("Enter the name of the expense or type 'end' to finish: ")
                    if name_expense.lower() == 'end':
                        break
                    amount_exp = float(input("Enter the amount of the expense: "))
                    add_expense(name.title(), name_expense, amount_exp)
                    save_data()
            elif expense_choice == "2" or expense_choice.lower() == "delete":
                print("As of now your expense sources are:")
                for source in users[name.title()]['expenses']:
                    print(f"  - {source}")
                delete_expense(name.title())
            print("Your expense sources are:")
            for source in users[name.title()]['expenses']:
                print(f"  - {source}")
            total_expenses = sum(users[name.title()]['expenses'].values())
            print(f"Total expenses: ${total_expenses}")
       
        elif login_choice == "2":
            print("1.Add an income")
            print("2.Delete an income")
            income_choice = input("Enter your choice (add or delete): ")
            if income_choice == "1" or income_choice.lower() == "add":

                while True:
                   name_income = input("Enter the name of the income or type 'end' to finish: ")
                   if name_income.lower() == 'end':
                      break
                
                    
                   amount_in = float(input("Enter the amount of the income: "))
                   add_income(name.title(), name_income, amount_in)
                   save_data()
                  
                
            elif income_choice == "2" or income_choice.lower() == "delete":
                print("As of now your income sources are:")
                for source in users[name.title()]['incomes']:
                    print(f"  - {source}")
                delete_income(name.title())
            print("Your income sources are:")   
            for source in users[name.title()]['incomes']:
                print(f"  - {source}")
                total_incomes = sum(users[name.title()]['incomes'].values())  
                print(f"Total incomes: ${total_incomes}")  
        elif login_choice == "3":
            total_expenses = sum(users[name.title()]['expenses'].values())
            total_incomes = sum(users[name.title()]['incomes'].values())
            balance = total_incomes - total_expenses

            print(f"Total expenses: ${total_expenses}")
            print(f"Total incomes: ${total_incomes}")
            print(f"Balance: ${balance}")
            if balance < 0:
             print(f"{name.capitalize()}, you are in debt.")
            else:
             print(f"{name.capitalize()}, you are financially stable.")

        elif login_choice == "4":
            print("1.Change password")
            print("2.Change username")
            
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

