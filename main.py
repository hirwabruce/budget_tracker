
from users import add_expense, load_data
from users import add_income
from users import add_user,users,save_data

print("Hello")
print("Your Budget Tracker")
print("1.Create a new account")
print("2.Login to existing account")
load_data()
choice = input("Enter your choice: ")

if choice == "1":
    name = input("What is your name? ")
    password = input("What is your password? ")
    add_user(name, password)
    save_data()
    
elif choice == "2":
    name = input("What is your name? ")
    password = input("What is your password? ")
    
    if name in users and users[name]['password'] == password:
        print("Login successful.")
    else:
        print("Invalid credentials.")
        exit()
else:
    print("Invalid choice.")
    exit()

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
    
total_expenses = sum(users[name]['expenses'].values())
total_incomes = sum(users[name]['incomes'].values())
balance = total_incomes - total_expenses

print(f"Total expenses: ${total_expenses}")
print(f"Total incomes: ${total_incomes}")
print(f"Balance: ${balance}")
#print(users)
save_data()
if balance < 0:
    print(f"{name.capitalize()}, you are in debt.")
else:
    print(f"{name.capitalize()}, you are financially stable.")