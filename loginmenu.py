# Author:Angela Fang
# Date:25/8/2023
# Purpose:to create a simple login program

import random
import string
import time


def login():  # function for previously registered users to login
    print("Login")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    accounts = load_accounts()  # loading user account from a file
    #  check if the username is existed in the account and password matches
    if username in accounts and accounts[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


# functions for users to generate password
def generate_password():
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length >= 10:
                break  # if the password length is valid and exit the loop
            else:
                print("Password length should be 10 or more characters.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

    while True:
        include_numbers = input("Include numbers? (yes/no): ").lower()
        if include_numbers == "yes" or include_numbers == "no":
            break  # if input is valid and exit the loop
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        include_symbols = input("Include symbols? (yes/no): ").lower()
        if include_symbols == "yes" or include_symbols == "no":
            break  # if input is valid and exit the loop
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    characters = string.ascii_letters  # initialize the characters set letters
    if include_numbers == "yes":  # Add numbers to characters if user selects it
        characters += string.digits
    if include_symbols == "yes":  # Add symbols to characters if user selects it
        characters += string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    return generated_password


# Function for user to register
def register():
    new_account = {}  # creating an empty dictionary to store user's information
    print("Register")

    while True:
        # spaces in the username not allowed, also strip any leading/trailing spaces
        username = input("Enter a username: ").strip()
        if ' ' in username:
            print("Username cannot contain spaces.")
        else:
            break

    while True:
        password_choice = input("Enter 'o' to enter your own password or 'g' to generate one: ").lower()
        if password_choice == 'o' or password_choice == 'g':
            break
        else:
            print("Invalid choice. Please enter 'o' or 'g'.")

    if password_choice == "o":
        while True:
            # spaces in the password not allowed, also strip any leading/trailing spaces
            password = input("Enter your password (10 or more characters): ").strip()
            if len(password) >= 10 and ' ' not in password:
                break
            else:
                print("Password length should be 10 or more characters and no space in the password")
    else:
        generated_password = generate_password()  # generate random password
        print("Generated password:", generated_password)
        password = generated_password

    new_account[username] = password  # add username and password to the new_account dictionary
    save_accounts(new_account)  # save the new_account to a file
    print("Registration successful!")


# Function to save user account information to a file
def save_accounts(accounts_to_save):
    with open("accounts.txt", "a") as file:  # open a file in an append mode
        for username, password in accounts_to_save.items():
            file.write(f"{username} {password}\n")  # write the username and password to the file
    print("User accounts saved to accounts.txt.")


# Function to load user account information from a file
def load_accounts():
    user_accounts = {}  # create an empty dictionary to store user accounts
    try:
        with open("accounts.txt", "r") as file:  # open the file in read mode
            lines = file.readlines()  # read all lines from the file
            for line in lines:
                username, password = line.strip().split()  # split each line into username and password
                user_accounts[username] = password
        return user_accounts
    except FileNotFoundError:
        return user_accounts


# Function to view user account information
def view_accounts():
    admin_password = input("Enter the admin password: ")
    if admin_password == "admin12345":
        accounts = load_accounts()  # load user accounts from a file
        if not accounts:
            print("No user accounts found.")
        else:
            print("User accounts:")
            for username, password in accounts.items():
                print(f"Username: {username}, Password: {password}")
    else:
        print("Access denied.")


while True:  # main program loop
    print("\nWelcome to the Simple Login Program!")
    print("\nMain Menu:")
    print("1. Login")
    print("2. Register")
    print("3. View Accounts")
    print("4. Exit")

    choice = input("Choose an option: ")  # user's choice

    if choice == "1":
        login()  # call the login function if choice is "1"
    elif choice == "2":
        register()
    elif choice == "3":
        view_accounts()
    elif choice == "4":
        print("Exiting in 2 seconds...")
        time.sleep(2)
        break
    else:
        print("Invalid option. Please choose again.")
