MENU = {

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 80,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 110,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 140,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Check the resources sufficient to make drink order .
def is_resourse_sufficient(order_ingredient):
    """checks the available amount is there for the order to provide"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True

# TODO: 2. Checks the amount inserted...
def process_amount():
    """Returns the total calculated from the cash inserted. """
    print("Please insert amount ...")
    total = int(input("how many Tens ?: ")) * 10
    total += int(input("how many Twenties ?: ")) * 20
    total += int(input("how many Fifties ?: ")) * 50
    total += int(input("how many Hundreds ?: ")) * 100
    return total

# TODO: 3. shows if the tracstion is accepted or not..
def is_transaction_successfully(money_recived, drink_cost):
    """Returns true when the payment is accepted , or False if the amount is insufficient."""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost)
        print(f'Here is Rs{change} in change..')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO: 4 . Ingredient amount is taken out from the resources..
def make_order(drink_name, order_ingridients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name} ☕")

# TODO: 5. The Coffiee Machice .


is_on = True
while is_on:
    choice = input("What would u like to have?(espresso/ latte/ cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: Rs{profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficient(drink["ingredients"]):
            payment = process_amount()
            is_transaction_successfully(payment, drink["cost"])
            make_order(choice, drink["ingredients"])
