from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_working = True
while machine_working:
    print_list = menu.get_items()
    order = input(f"What would you like? /{print_list}: ")

    if order == "off":
        machine_working = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost): # drink 객체는 menu.MenuItem 객체라서 흠....
                coffee_maker.make_coffee(drink)


'''
menu = Menu()
menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_working = True
while machine_working:
    print_list = menu.get_items()
    order = input(f"What would you like? /{print_list}: ")
    # drink = menu.find_drink(order) #주문 가능한지

    if order == "off":
        machine_working = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(drink): #drink에 필요한 재료 다 있으면
            money_received = money_machine.process_coins() #돈 받고 받은 돈 변수에 저장
            money_machine.make_payment(menu.menu[drink]) # 못해먹겠네 아오
'''
