class Bankaccount():
    def __init__(self, name, password, balance, account_number):
        self.name = name
        self.password = password
        self.balance = balance
        self.account_number = account_number

    def checkbalance(self, account_number, password):
        if password == self.password and self.account_number == account_number:
            print(self.balance)
        else:
            print("incorrect name or password")

    
    def deposit(self, password, amount, account_number):
        if password == self.password and self.account_number == account_number:
            if amount >= 0:
                self.balance += amount
                print(f"your new balance is {self.balance}")
            else:
                print("cannot deposit negative amount")
        else:
            print("incorrect name or password")


    def withdraw(self, password, amount, account_number):
        if password == self.password and account_number == self.account_number:
            if amount > self.balance:
                print('you cannot withdraw more money than your current balance')
            else:
                self.balance -= amount
                print(f'withdrawal successful, your new amount is {self.balance}')
            
        else:
            print("invalid name or password")
        
    def _accountDetails(self, name, password):
        if name == self.name and password == self.password:
            print(f"account name: {self.name}")
            print(f"Your account number is {self.account_number}")
            print(f"account balance: {self.balance}")
        else:
            print("invalid name or password")

#user1 = Bankaccount('Oswald', '4Jesus', 2000)
#user1.checkbalance('Oswald', '4Jesus')

#user1.withdraw('Oswald', '4Jesus', 1350)

#user2 = Bankaccount('kofi', '4Jesus', 5000)
#user2.checkbalance('kofi', '4Jesus')
#user2.withdraw('kofi', '4Jesus', 2530)
#user1.deposit('Oswald', '4Jesus', 3200)