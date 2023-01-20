from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while is_on:
    customer_order = input(f"What would you like to drink? ({menu.get_items()}) ")
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        customer_order = menu.find_drink(customer_order)
        if coffee_maker.is_resource_sufficient(customer_order):
            if money_machine.make_payment(customer_order.cost):
                coffee_maker.make_coffee(customer_order)
