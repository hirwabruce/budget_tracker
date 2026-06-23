
from expenses import add_expense, expenses
from incomes import add_income, incomes

print("Hello")
print("Your Budget Tracker")
name = input("What is your name? ")
while True:
    name_expense = input("Enter the name of the expense: ")
    if name_expense.lower() == 'end':
        while True:
            name_income = input("Enter the name of the income: ")
            if name_income.lower() == 'end':
                break
            amount_in = float(input("Enter the amount of the income: "))
            add_income(name_income, amount_in)
            #print(incomes)
        break
    amount_exp = float(input("Enter the amount of the expense: "))
    add_expense(name_expense, amount_exp)
    
total_expenses = sum(expenses.values())
total_incomes = sum(incomes.values()) 
balance = total_incomes - total_expenses

print(f"Total expenses: ${total_expenses}")
print(f"Total incomes: ${total_incomes}")
print(f"Balance: ${balance}")
