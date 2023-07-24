from menu import MENU
from resources import resources


# todo 2
machine_working = True
PASSWORD = "root"

# todo 5-b.
QUARTER_DIME_NICKEL_PENNY = [0.25, 0.10, 0.05, 0.01]
coins = [0, 0, 0, 0]

# todo 3
report = resources.copy()
report["money"] = 0


# todo 3
def print_report():
    """print f-string of contents to report."""
    for key in report:
        if key == "money":
            print(f"\t{key.title()}: ${round(report[key], 3)}")
        elif key == "coffee":
            print(f"\t{key.title()}: {report[key]}g")
        else:
            print(f"\t{key.title()}: {report[key]}ml")


# todo 4
def check_resources():
    """return True or False. check if resources is enough."""
    check = True
    for factor in user_choice["ingredients"]:
        if report[factor] < user_choice["ingredients"][factor]:
            print(f"Sorry there is not enough {factor}")
            check = False
    return check


# todo 5-c.
def added_coins():
    """return integer. value is total of inserted coins. """
    user = 0
    for i in range(0, 4):
        user += QUARTER_DIME_NICKEL_PENNY[i] * coins[i]
    return user


# todo 7
def make_menu(menu):
    for factor in menu["ingredients"]:
        report[factor] -= menu["ingredients"][factor]
    return menu


while machine_working:
    # TODO: 1. prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    ## a. Check the user's input to decide what to do next.
    ## b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
    chosen_menu = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    ## a. For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code should end execution when this happens.
    if chosen_menu == "off":
        check_pw = input("Enter the password: ")
        if check_pw == PASSWORD:
            machine_working = False
    # TODO: 3. Print report.
    ## a. When the user enters "report" to the prompt, a report should be generated that shows the current resource values. e.g.
    ## - Water: 100ml
    ## - Milk: 50ml
    ## - Coffee: 76g
    ## - Money: $2.5
    elif chosen_menu == "report":
        print_report()
    else:
        user_choice = MENU[chosen_menu]
        # TODO: 4. Check resources sufficient?
        ## a. When the chooses a drink, the program should check if there are enough resources to make that drink.
        ## b. E.G. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: "Sorry there is not enough water."
        ## c. The same should happen if another resource is depleted, e.g. milk or coffee.
        if check_resources():
            # TODO: 5. Process coins.
            ## a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
            ## b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            ## c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies = 0.25 + 0.1x2 + 0.05 + 0.01x2 = $0.52
            print("Please insert coins.")
            coins[0] = int(input("How many quarters?"))
            coins[1] = int(input("How many dimes?"))
            coins[2] = int(input("How many nickles?"))
            coins[3] = int(input("How many pennies?"))
            user_money = added_coins()
            # TODO: 6. Check transaction successful?
            ## a. Check that the user has inserted enough money to purchase the drink they selected. E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say "Sorry that's not enough money. Money refunded.".
            ## b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered. E.g.
            ## - Water: 100ml
            ## - Milk: 50ml
            ## - Coffee: 76g
            ## - Money: $2.5
            ## c. If the user has inserted too much money, the machine should offer change. E.g. "Here is $2.45 in change." The changes should be rounded to 2 decimal places.
            if user_money < user_choice["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if user_money > user_choice["cost"]:
                    change = round(user_money - user_choice["cost"], 3)
                    print(f"Here is ${change} in change.")
                    report["money"] += (user_money - change)
                else:
                    report["money"] += user_money
                # TODO: 7. Make Coffee.
                ## a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
                ## E.g. report before purchasing Latte:
                ## - Water: 300ml
                ## - Milk: 200ml
                ## - Coffee: 100g
                ## - Money: $0
                ## Report after purchasing latte:
                ## - Water: 100ml
                ## - Milk: 50ml
                ## - Coffee: 76g
                ## - Money: $2.5
                ## b. Once all resources have been deducted, tell the user "Here is your latte. Enjoy!". If latte was their choice of drink.
                make_menu(user_choice)
                print(f"Here is your {chosen_menu}. Enjoy!")
