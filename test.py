import csv
import os
import tkinter as tk
from tkinter import ttk

# define global variables
tenant_data_file = "tenant_data.csv"
expense_data_file = "expense_data.csv"
category_data_file = "category_data.csv"

# define functions for account management
def create_account(username, password):
    # create a new account with the given username and password
    with open("accounts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def login(username, password):
    # log in to an existing account with the given username and password
    with open("accounts.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
        return False

def manage_account(username):
    # manage the account settings for the user with the given username
    pass

# define functions for managing tenant data
def add_tenant(name, address, phone_number, email):
    # add a new tenant with the given data to the tenant data file
    with open(tenant_data_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, address, phone_number, email])

def delete_tenant(name):
    # delete the tenant with the given name from the tenant data file
    data = []
    with open(tenant_data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                data.append(row)
    with open(tenant_data_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def manage_tenant(name):
    # manage the data for the tenant with the given name
    pass

# define functions for managing expense data
def add_expense(amount, description):
    # add a new expense with the given amount and description to the expense data file
    with open(expense_data_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, description])

def allocate_category(expense_id, category):
    # allocate the given category to the expense with the given ID in the expense data file
    data = []
    with open(expense_data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == expense_id:
                row.append(category)
            data.append(row)
    with open(expense_data_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# define functions for viewing/displaying record data
def view_tenant_data():
    # display the tenant data in a table or other format
    with open(tenant_data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def view_expense_data():
    # display the expense data in a table or other format
    with open(expense_data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def view_category_data():
    # display the category data in a table or other format
    with open(category_data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# define functions for
