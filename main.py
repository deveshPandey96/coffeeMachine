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
profit = 0
def check_availability(coffee):
    if coffee == "espresso":
        if resources["water"] < 50 or resources["coffee"] < 18:
            return False
        else:
            return True
    elif coffee == "latte":
        if resources["water"] < 200 or resources["milk"] < 150 or resources["coffee"] < 24:
            return False
        else:
            return True
    elif coffee == "cappuccino":
        if resources["water"] < 250 or resources["milk"] < 100 or resources["coffee"] < 24:
            return False
        else:
            return True


def take_money(coffee):
    global profit
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if coffee == "espresso":
        if total < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is ${round(total - 1.5,2)} in change.")
            profit += 1.5
            return True
    elif coffee == "latte":
        if total < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is ${round(total - 2.5,2)} in change.")
            profit += 2.5
            return True
    elif coffee == "cappuccino" :
        if total < 3.0:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is ${round(total - 3.0,2)} in change.")
            profit += 3.0
            return True

def give_coffee(coffee):
    global resources
    if coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        print(f"Here is your {coffee} ☕️. Enjoy!")
    elif coffee == "latte" :
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        print(f"Here is your {coffee} ☕️. Enjoy!")
    elif coffee == "cappuccino" :
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        print(f"Here is your {coffee} ☕️. Enjoy!")

coffee_machine_on = True

while coffee_machine_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif drink =="off":
        coffee_machine_on = False
    else:
        if check_availability(drink):
            money = take_money(drink)
            if money:
                give_coffee(drink)
        else:
            print("Sorry there is not enough water.")