
class Account:

    def __init__(self, filepath):
        self.filepath = filepath # set self.filepath as a variable to use in the commit function
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance)) #note: str is usde to write amount back into file


#account = Account('balance.txt')
#account.withdraw(200)
#account.deposit(5000)

#print(account.balance)
#account.commit()

##########################################
#INHEREITANCE                                                   #
##########################################
class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

ichecking = Checking("balance.txt", 3.10)
ichecking.transfer(100)
ichecking.commit()
print(ichecking.balance)