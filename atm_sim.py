""" Simple atm simulator"""
import pickle
with open("accounts.pickle", "rb") as file:
    accounts = pickle.load(file)
file.close()


def main_menu():
    """Welcome screen function. It gives some options to the user and returns a value
    input --> number from menu
    returns --> response as string
    """
    print("--------------------------------------")
    print("Welcome to Jupiter Bank ATM Simulator\n")
    print("--------------------------------------")
    print("1) Log in to your  account\n")
    print("2) Create an account\n")
    print("3) Exit\n")
    resp = input("Please select an option: ")
    if resp != "1" and resp != "2" and resp != "3":
        print("Please enter a valid option\n")
        main_menu()
    else:
        return resp


def login_menu():
    pass


def open_account():

    """Creates a Account and adds to the accounts list"""

    def account_id_generator():

        """Creates an account id number form current year and month"""
        from datetime import datetime
        now = datetime.now()
        year = now.year
        month = now.month
        id_seed = 1
        generated_acc_id = str(year) + str(month) + str(id_seed)
        while generated_acc_id in accounts:
            id_seed += 1
            generated_acc_id = str(year) + str(month) + str(id_seed)
        return generated_acc_id

    acc_id = account_id_generator()
    print("Your account id is: {}".format(acc_id))
    passwd = input("Please enter a password for your account: ")
    accounts[acc_id] = passwd
    print("Your account has successfully created\n")
    print(accounts)
    main()


def save_accounts():
    """This function saves the account list to a file"""
    with open("accounts.pickle", "wb") as file:
        pickle.dump(accounts, file, protocol=pickle.HIGHEST_PROTOCOL)
    file.close()


def log_in():
    acc_num = input("Please enter your account number\n")
    pwd = input("Please enter your password\n")

    while

    pass


def end_program():
    save_accounts()
    print("Thank yu for using Jupiter Bank ATM Machine\n")
    print("We wish you a pleasant day :) \n")


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
