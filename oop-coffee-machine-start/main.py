from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        exit()
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)