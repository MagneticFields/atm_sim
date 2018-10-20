""" Simple atm simulator"""
import pickle
import sys

"""
Loading accounts file
"""
with open("accounts.pickle", "rb") as file:
    accounts = pickle.load(file)
file.close()

# This will load a balances dictionary

with open("balances.pickle", "rb") as f:
    balances = pickle.load(f)
f.close()


def main_menu():
    """Welcome screen function. It gives some options to the user and returns a value
    input --> number from menu
    returns --> resp, string
    """
    print("--------------------------------------")
    print("Welcome to Jupiter Bank ATM Simulator\n")
    print("--------------------------------------")
    print("1) Log in to your  account\n")
    print("2) Create an account\n")
    print("3) Exit\n")
    print("---------------------------------------\n")
    resp = input("Please select an option: ")
    if resp != "1" and resp != "2" and resp != "3":
        print("Please enter a valid option\n")
        main_menu()
    else:
        return resp


def login_menu(acc_id):
    """
    Account menu. With this menu user will able to perform some operations on his / her account
    :param acc_id: passed from login_menu() func.
    :return: none
    """

    print("Welcome " + acc_id)
    print("Your balance is: " + str(balances[acc_id]))
    print("-----------------\n")
    print("Please select an item")
    print("1) Withdraw money")
    print("2) Deposit money")
    print("3) Transfer money")
    print("4) View balance")
    print("5) Return to main menu")
    print("6) Exit\n")
    print("------------------")
    choice = input("Please select an option: ")

    def withdraw(acc_id):
        """
        Withdraws money  from the account. First ask for the amount to be withdrawn and checks if the account does have
        sufficient amount. Then updates the balances dict by subtracting the withdrawn amount.
        :param acc_id:
        :return: None
        """
        amount = input("Please enter the amount you wish to withdraw: ")
        while not amount.isdigit():
            print("Please enter only numbers!\n")
            amount = input("Please enter the amount you wish to withdraw: ")

        if balances[acc_id] < int(amount):
            print("Insufficient funds\n")
            print("You have " + str(balances[acc_id]) + " in your account")
            trial = input("Press 1 for account menu, any key for try again: ")

            if trial == "1":
                login_menu(acc_id)
            else:
                withdraw(acc_id)
        else:
            balances[acc_id] = balances[acc_id] - int(amount)
            print("Your balance is now: " + str(balances[acc_id]))
            login_menu(acc_id)

    def deposit(acc_id):
        """
        helper function for depositing some amount to the account. Simply updates the balances dict.
        :param acc_id:
        :return: None
        """
        amount = input("Please enter the amount you wish to deposit")
        while not amount.isdigit():
            print("Please use only digits\n")
            amount = input("Please enter the amount you wish to deposit")

        balances[acc_id] += int(amount)
        print(str(amount) + " has been added to your funds")
        login_menu(acc_id)

    def transfer_money(acc_id):
        """
        Transfers money to another account. First checks if the account number, the funds will be sent, is valid
        and checks if  there is enough money in the current account. Then updates the balances.
        :param acc_id:
        :return: None
        """
        other_acc_id = input("Please enter the account number you with to send funds: ")

        # Checks if such account number exists.
        while other_acc_id not in accounts:
            print("There is no such account number in our system")
            other_acc_id = input("Please enter the account number you wish to send funds:")

        transferring_amount = input("Please enter the amount you wish to transfer: ")
        if transferring_amount > balances[acc_id]:
            print("You have insufficient funds")
            transfer_money(acc_id)
        else:
            balances[acc_id] -= transferring_amount
            balances[other_acc_id] += transferring_amount
        print("Transfer Complete!")
        login_menu(acc_id)

    def view_balance(acc_id):
        print("You have " + str(balances[acc_id]) + " in your account")
        login_menu(acc_id)

    if choice == "1":
        withdraw(acc_id)

    elif choice == "2":
        deposit(acc_id)

    elif choice == "3":
        transfer_money(acc_id)

    elif choice == "4":
        view_balance(acc_id)
    elif choice == "5":
        main_menu()

    elif choice == "6":
        end_program()


def open_account():

    """Creates a Account and adds to the accounts list"""

    def account_id_generator():

        """
        Creates an account id number form current year and month and adds a number and checks if the number is unique
        """
        from datetime import datetime
        now = datetime.now()
        year = now.year
        month = now.month
        id_seed = 1  # This id seed will be used for create unique acc_id's for everyday.
        generated_acc_id = str(year) + str(month) + str(id_seed)
        while generated_acc_id in accounts:
            id_seed += 1
            generated_acc_id = str(year) + str(month) + str(id_seed)
        return generated_acc_id

    acc_id = account_id_generator()
    print("Your account id is: {}".format(acc_id))
    passwd = input("Please enter a password for your account: ")
    accounts[str(acc_id)] = passwd
    balances[str(acc_id)] = 0
    print("Your account has successfully created\n")
    print(accounts)
    main()


def save_accounts():
    """This function saves the account list to a file"""
    with open("accounts.pickle", "wb") as file:
        pickle.dump(accounts, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()
    with open("balances.pickle", "wb") as f:
        pickle.dump(balances, f, protocol=pickle.HIGHEST_PROTOCOL)
    f.close()


def log_in():
    acc_id = input("Please enter your account number: ")
    if acc_id not in accounts:
        print("There is no such account number\n")
        acc_id = input("Please try again: ")
    else:
        pwd = input("Please enter your password: ")
        tries = 3
        # This code below gives 3 tries for the right password but not working
        while accounts[acc_id] != pwd:
            if tries > 0:
                print("Wrong password, please try again")
                pwd = input("You have " + str(tries) + " remaining: ")
                tries -= 1
            elif tries == 0:
                print("Sorry too many wrong attempts! \n")
                end_program()
                break
        login_menu(acc_id)


def end_program():
    save_accounts()
    print("Thank you for using Jupiter Bank ATM Machine\n")
    print("We wish you a pleasant day :) \n")
    sys.exit()


def main():
    response = main_menu()
    if response == "1":
        log_in()
    elif response == "2":
        open_account()
    elif response == "3":
        end_program()


if __name__ == "__main__":
    main()
