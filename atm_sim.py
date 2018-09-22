""" Simple atm simulator"""



accounts = {} # This dict is for storing account ids and passwords. Keys = id, values = pass



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
    resp = input("Please select an option: ")
    if resp != "1" and resp != "2":
        print("Please enter a valid option")
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
        id_seed += 1
        return generated_acc_id

    acc_id = account_id_generator()
    print("Your account id is: {}".format(acc_id))
    passwd = input("Please enter a password for your account: ")
    accounts[acc_id] = passwd
    print("Your account has successfully created")
    main_menu()




def save_accounts():
    """This function saves the account list to a file"""
    # TODO


def log_in():
    # TODO
    print("Log In")


def load_accounts():
    """ This helper function loads account objects from list created by open account function"""


def main():
    load_accounts()
    response = main_menu()
    if response == "1":
        log_in()
    elif response == "2":
        open_account()


if __name__ == "__main__":
    main()
