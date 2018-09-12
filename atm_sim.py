""" Simple atm simulator"""


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


class Account(object):
    id_ = 201801
    passwd = {}

    def __init__(self, password_):
        id_ = 201801
        self.id = Account.id_
        self.password = password_
        self.balance = 0
        Account.passwd[id_] = password_
        Account.id_ += 1

    def __str__(self):
        return 'Account ' + str(self.id) + ' has ' + str(self.balance)

    def set_balance(self, balance):
        self.balance = balance

    def add_funds(self, amount):
        self.balance = self.balance + amount
        print(str(amount) + 'added to your account')

    def withdraw_funds(self, amount):
        if amount > self.balance:
            print('You don\'t have enough funds')
        else:
            self.balance = self.balance - amount

    def get_id(self):
        return self.id

    def transfer_funds(self, other, amount):
        if amount > self.balance:
            print('You don\'t have enough funds!')
        else:
            self.balance = self.balance - amount
            other.balance = other.balance + amount

    def get_pass(self):
        id_ = self.id
        if id_ in Account.passwd:
            return Account.passwd[id_]
        else:
            return 'No id'


# class Password(object):
#
#    def __init__(self, id_, password):
#        self.id = id_
#        self.password = password
#
#    def get_password(self, id_):
#        return self.password

accounts = []


def open_account():
    """Creates a Account object and adds to the accounts list"""

    name = input('Please enter a name for your account: ')
    print('Please enter a password for your account\n')
    password_ = int(input())
    name = Account(password_)  # Need a variable to create object instances
    accounts.append(name)
    save_accounts()
    print('Your account successfully created')
    print('Your account id is: ' + str(Account.get_id()))

    # TODO


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
