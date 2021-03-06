"""
Bank Account Class Lesson Example from Learn Python
"""

class BankAccount(object):

  balance = 0

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "The account belongs to %s and the balance is $%.2f." % (self.name, self.balance)

  def show_balance(self):
    print('$%.2f' % (self.balance))

  def deposit(self, amount):
    if amount <= 0: 
      print("Error: Deposit Amount too Low")
      return
    else: 
      print("Depositing $%.2f" % (amount))
      self.balance += amount
      self.show_balance()

  def withdraw(self, amount):
    if amount > self.balance:
      print("Error: Withdrawl Amount too High")
      return
    else: 
      print("Withdrawing $%.2f" % (amount))
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Ashley")
print(my_account)

my_account.show_balance()
my_account.deposit(2800)
my_account.withdraw(1200)
print(my_account)
