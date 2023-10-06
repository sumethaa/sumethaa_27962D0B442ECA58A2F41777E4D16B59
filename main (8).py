'''Implement a class called BankAccount that represents a bank account.The class should have private
attributes for account number, account holder name, and account balance.Include methods to
deposite money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class.Write a program to create an instance of the
BankAccount class and test the deposite and withdrawal functionality.'''


class BankAccount:
  
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  
  def deposite(self, amount):
    if amount > 0:
      self.__account_balance +=amount
      #self.__account_balance = self._-account_balance+amount
      print("deposite ₹{}.New balance{}".format(amount,
                                             self.__accont_balance))
    else:
      print("Invalid deposite amount.")

  def withdrawal(self,amount):
    if amount > 0 and amount <=self.__account_balance:
      self.__account_balance -= amount
      #self._account-balance = self.__account_balance-account
      print("withdrawal ₹{}.New balance:₹{}".format(amount, 
                                                 self.__acconut_balance))
    else:
      print("Invalid withdrawal amount or insuffiecient balance.")

  def display_balance(self):
     print("Account balance for {} (Account #{}): ₹{}".format(
         self.__account_holder_name,self.__account_number,
         self.__account_balance))


#create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="Hari praphu",
                      initial_balance=5000.0)
      
# Test deposie and withdrawal functionality
account.display_balance()
#account.deposite(500.0)
#account.withdrawal(200.0)
#account.display_balance()
      