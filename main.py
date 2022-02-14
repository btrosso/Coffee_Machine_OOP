from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
# MY First ATTEMPT - Works but i think it could be improved.
coffee_tron3000 = CoffeeMaker()
money_tron3000 = MoneyMachine()
menu1 = Menu()
end_program = 0

while end_program == 0:
    user_choice = input(f"   What would you like? ({menu1.get_items()}): ")

    if user_choice != 'report' and user_choice != 'exit':
        menu_item_choice = menu1.find_drink(order_name=user_choice)
        if coffee_tron3000.is_resource_sufficient(drink=menu_item_choice):
            money_tron3000.make_payment(menu_item_choice.cost)
            coffee_tron3000.make_coffee(menu_item_choice)
    elif user_choice == 'report':
        coffee_tron3000.report()
        money_tron3000.report()
    elif user_choice == 'exit':
        end_program = 1
"""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"   What would you like ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(cost=drink.cost):
            coffee_maker.make_coffee(drink)
