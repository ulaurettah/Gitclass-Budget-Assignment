class Budget:

    def __init__(self, category):
        self.category = category
        self.balance = 0

    def withdraw(self, amount):
      if self.balance>=amount:
            self.balance= self.balance-amount
      else:
            print('Insufficient balance')

     
    def deposit(self, amount):
        self.balance = self.balance+amount
        

    def compute(self):
        return self.balance

    def set_balance(self, balance):
        self.balance= balance


    def Transfer(cat_from, cat_to, amount):
        if cat_from.compute() >= amount:
            cat_from.set_balance(cat_from.compute() - amount)
            cat_to.set_balance(cat_to.compute() + amount)
        else:
            print('Insufficient Balance')


    
food = Budget('food')
clothing =Budget ('clothing')
entertainment =Budget('entertainment')
print(food.compute())
print(clothing.compute())
food.deposit(100)
clothing.deposit(50)
entertainment.deposit(200)
print(food.compute())
print(clothing.compute())
clothing.withdraw(10)
print(food.compute())
print(clothing.compute())
Budget.Transfer(food,clothing, 15)
Budget.Transfer(clothing,entertainment, 50)
print(food.compute())
print(clothing.compute())
print(entertainment.compute())
print(food.compute())
print(clothing.compute())
print(entertainment.compute())
