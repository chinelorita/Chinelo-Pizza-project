"""Pizza data struction
A dictionary to map, selection to a list
containing size and price in form [size (int), price (float)]
"""
pizza = {
  "1": [7, 3],
  "2": [9, 5.5],
  "3": [14, 7.25]
}

"""Topping data structure
A dictionary to map selection to a list containing
type and price in form [type (str), price (float)]
"""
topping = {
  "1": ["Ham", 0.8],
  "2": ["Mushrooms", 0.5],
  "3": ["Pepperoni", 1.0],
  "4": ["Olives", 0.3],
  "5": ["Pineapple", 0.6],
  "6": ["Extra Cheese", 1.2]
}

class User:
  def __init__(self, credit):
    self.credit = 0
    self.amount = 0
    self.start = False

  def add_credit(self, credit):
    self.credit += credit

  def sub_credit(self, credit):
    self.credit -= credit
  
  def add_amount(self, value):
    self.amount += value

user = User(0)
def add_credit():
  print("Please enter how many credits you would like to add to your balance: ", end="")
  cred = int(input())
  user.add_credit(cred)
  if not user.start:
    main()
  # print("New credit is {:.2f}".format(user.credit))

def summary():
  print("........................................")
  print("Available Balance: {} credits".format(user.credit))
  print("Pizza price: {:.2f} credits".format(user.amount))
  print("----------------------------------------")
  print("Your new Balance = {:.2f} credits".format(user.credit - user.amount))
  print("----------------------------------------")
  
  if user.amount > user.credit:
    print("You have insufficient credits available. You require \"{:.2f}\" credits.".format(user.amount - user.credit))
    print("Would you like to add more credits?")
    print("Please enter 'Y' for yes and 'N' for no : ", end="")

    choice = str(input())

    if choice == "Y":
      add_credit()
      summary()

    if choice == "N":
      print("Sorry, you cannot continue without sufficient credit")
      return

  else:
    print("Would you like to order another pizza?")
    print("Please input 'Y' for yes and 'N' for no : ", end="")

    choice = str(input())

    user.sub_credit(user.amount)

    if choice == "N" or choice == "n":
      print("Thank you, goodbye!")
    elif choice == "Y" or choice == "y":
      print("Here we go again")
    else:
      print("Invalid selection")
    return

def order_pizza():
  print("ORDER PIZZA – Select Size [Current Balance = {:.2f} credits]".format(user.credit))
  print("Please choose from the following options:")
  print("1. 7 inch [3.0 credits]")
  print("2. 9 inch [5.50 credits]")
  print("3. 14 inch [7.25 credits]")
  print("0. Return to Main Menu")
  print("........................................")
  print("Please enter a number : ", end="")
  order = int(input())
  print("order = ", order)
  user.start = True
  if order in [1, 2, 3]:
    pizza_select = pizza[str(order)]

    print("You have selected a {} inch pizza.".format(pizza_select[0]))
    print("Please choose from the following toppings:")
    print("1. Ham [0.80 credits]")
    print("2. Mushrooms [0.50 credits]")
    print("3. Pepperoni [1.00 credits]")
    print("4. Olives [0.30 credits]")
    print("5. Pineapple [0.60 credits]")
    print("6. Extra Cheese [1.20 credits]")
    print("0. Return to Main Menu")

    toppin = int(input())

    if toppin > 6:
      print("invalid selection")
      return order_pizza()
    
    topping_select = topping[str(toppin)]
    
    user.add_amount(pizza_select[1] + topping_select[1])

    print("You have added {} to your pizza. Your current price is: {:.2f} credits.".format(topping_select[0], user.amount))
    
    print("Would you like to add additional toppings?")
    print("Please input 'Y' for yes and 'N' for no :", end="")

    choice = str(input())

    print(choice)
    
    if choice == "Y" or choice == "y":
      print("ok")
    if choice == "N" or choice == "n":
      summary()
      return
      

      

  elif order == 0:
    main()
  else:
    print("Invalid selection")
    order_pizza()

def main():
  print("-------------------------------")
  print("UCLan PIZZA")
  print("-------------------------------")
  print("MAIN MENU")
  print("1. Add Credits (current credits = {:.2f})".format(user.credit))
  print("2. Order Pizza")
  print("0. Exit")
  print("Please enter a number: ", end="")

  num = int(input())

  if num == 1:
    add_credit()
  elif num == 2:
    order_pizza()
  elif num == 0:
    print("Thank you, goodbye!")
    return
  else:
    print("Invalid Selection, Please try again.")

if __name__ == "__main__":
  main()