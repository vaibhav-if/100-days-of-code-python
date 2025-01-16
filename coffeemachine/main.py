MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources(order):
    for items in MENU[order]["ingredients"]:
        if resources[items] < MENU[order]["ingredients"][items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

def check_money(order, money_inserted):
    if money_inserted < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_inserted >= MENU[order]["cost"]:
        change = round(money_inserted - MENU[order]["cost"], 2)
        print(f"Here is ${change} in change.")
        return True

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        exit()
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if check_resources(order):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if check_money(order, money_inserted):
                money += MENU[order]["cost"]
                for items in MENU[order]["ingredients"]:
                    resources[items] -= MENU[order]["ingredients"][items]
                print(f"Here is your {order} ☕️. Enjoy!")