
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
# i.e Creating a sub class from a base class.      #
#  its has its own methods like seen below too.   #                                              #
##########################################

class Checking(Account):
    #Doc string
    '''The is used to give more info about the class and what id does'''
    #Data Members:
    #All class & instance variables are data members in a class

    type = 'Checking' #class variable: can use in many functions in a class object

    #this is a class Contructor
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee #use instance variable in an init for the class objectself.

    #this is a class method
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

ichecking = Checking("balance.txt", 2) # this an Object insatnce with a file path
ichecking.transfer(50)
ichecking.commit()

#This is an example of instantiation
# Johns_acc = Checking("johns-account.txt", 2)


print(ichecking.balance, "Account type:", ichecking.type)
print(ichecking.__doc__)#print doc string info