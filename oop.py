

'''
# write a book class with attributes title, and author. create a object and print the detatils of the book 

class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author 
        
Book1 = Book('Inside the company a CIA diary', 'Philip Agee')
#print(Book1.title + ' by ' + Book1.author) # Inside the company a CIA diary by Philip Agee
print(f'title: {Book1.title}, author: {Book1.author}') # title: Inside the company a CIA diary, author: Philip Agee

'''


#create a class named BankAccount with: 
# an __init__method that takes account_holder and balance (dafault value 0) as arguments
# a method deposit(amount)that adds money to the balance
#a method withdraw(amount)that substacts money if theres enough balance
#a method get_balance() that returns the balance 
#create an object of BankAccount and preform the following actions:
# deposit 100
# withdraw 50
#print the balance

'''
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('insufficient balance')
            
    def get_balance(self):
        return self.balance
print ('account holder: ', BankAccount('John Doe').account_holder) # account holder:  John Doe
account = BankAccount('John Doe')       
account.deposit(1000)
account.withdraw(50)
print('balance: ', account.get_balance()) # balance:  50
'''


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            print(f'you have amount {amount} in your account')
        else:
            print('invalid amount')
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'you have withdrawn {amount} from your account')
        else:
            print('insufficient balance')
    def get_balance(self):        
        return self.balance 
 
myaccount = BankAccount('Felipe Ruiz', 1000)
myaccount.deposit(500)
myaccount.withdraw(200)
print('balance: ', myaccount.get_balance()) # balance:  1300            
                  
        

    