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

def coffe():
    global resources
    if choose == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18


    elif choose == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif choose == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24

    print(f"Here is your {choose} ☕️. Enjoy!")
    return


def payment(cost):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    calculate = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if calculate >= cost:
        change = round(calculate - cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def current_resources(choose):
    global resources
    drink = MENU[choose]
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


while True:
    choose = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choose == "off":
        break
    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choose]
        if current_resources(choose):
            cost = drink["cost"]
            print(f"Cost of {choose} is ${cost}.")
            if payment(cost):
                coffe()
