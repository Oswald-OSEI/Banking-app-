from bankaccount import Bankaccount
import itertools
from random import randint
accounts = {}

for i in itertools.count(start=1):
    print("*******************************************************")
    print("WELCOME TO WEL'S  BANKING")
    print("SELECT AN OPTION")
    print("1. Create Account")
    print("2. Check Account Balance")
    print("3. Make Withdrawal")
    print("4. Deposit")
    print("5.Check account details")
    choice = input("option:")
    choice = int(choice)
    if choice == 1:
        def account_number_generator():
            const = "040"
            first_ = str(randint(100, 999))
            second_ = str(randint(100, 999))
            third_ = str(randint(1, 9))
            account_number = const + first_ + second_ + third_
            account_number = int(account_number)
            return account_number
        username = input("name: ")
        password = input("Password: ")
        balance = input("Account Balance: ")
        balance = int(balance)
        account_number = account_number_generator()
        account_number = int(account_number)
        account = Bankaccount(username, password, balance, account_number)
        accounts[account_number] = account
        print(f"you have successfully created an account with account number {account_number}")

    elif choice == 2:
        account_number = input("Account number: ")
        account_number = int(account_number)
        password = input("password:")
        for keys in accounts:
            if account_number == keys:
                accounts[account_number].checkbalance(account_number, password)
            else:
                print("invalid account number")

    elif choice == 4:
        account_number = input("Account number: ")
        account_number = int(account_number)
        deposit_amount = input("Deposit Amount: ")
        deposit_amount = int(deposit_amount)
        password = input("password:")
        for keys in accounts:
            if account_number == keys:
                accounts[keys].deposit(password, deposit_amount, account_number)
            else:
                print("invalid account number")

    elif choice == 3:
        account_number = input("Account number: ")
        account_number = int(account_number)
        Withdrawal_amount = input("Amount to withdraw: ")
        Withdrawal_amount = int(Withdrawal_amount)
        password = input("password: ")
        for keys in accounts:
            if account_number == keys:
                accounts[keys].withdraw(password, Withdrawal_amount, account_number)
            else:
                print("invalid account number")

    elif choice == 5:
        name = input("Name: ")
        password = input("Password: ")
        for keys, values in accounts:
            values._accountDetails(name, password)
    else:
        print("invalid option")




#account = Bankaccount(username, password, balance)
#account._accountDetails()   