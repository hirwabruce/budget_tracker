import json


users = {}

def add_user(name, password):
    users[name] = {'password': password,'expenses': {},'incomes': {}}

def add_income(username, income_name, amount):
    users[username]['incomes'][income_name] = amount

def add_expense(username, expense_name, amount):
    users[username]['expenses'][expense_name] = amount

def save_data():
    with open('data.json', 'w') as f:
        json.dump(users, f)
def load_data():
  try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        users.clear()
        users.update(data)

  except FileNotFoundError:
        users.clear()

load_data()


def validate_password(password):
    if len(password) < 6:
        return False
    if not password.isdigit():
        return False
    return True

def validate_username(username):
    if len(username) < 3:
        return False
    if not username.isalnum():
        return False
    return True

def delete_expense():
    username = input("Enter your username: ")

