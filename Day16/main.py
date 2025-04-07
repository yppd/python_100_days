from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True
while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
#     else:
#         drink = MENU[coffee_choice]
#         if resources_check(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(coffee_choice, drink["ingredients"])
