from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
menu = Menu()
mmachine = MoneyMachine()

#Print report
coffee_maker.report()
mmachine.report()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        mmachine.report()
    else:
        drink = menu.find_drink(choice)
        #Check Resources,Process coins and Check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and mmachine.make_payment(drink.cost):
            #Make coffee
            coffee_maker.make_coffee(drink)
            
        
        
        





