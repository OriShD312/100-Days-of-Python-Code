MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}


def check_resources(request):
    for item in request:
        if request[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins(cost):
    print(f"Please insert ${cost} worth of coins")
    total = int(input("How many quarters?: ($0.25) ")) * 0.25
    total += int(input("How many dimes?: ($0.10) ")) * 0.10
    total += int(input("How many nickels?: ($0.05) ")) * 0.05
    total += int(input("How many cents?: ($0.01) ")) * 0.01
    return total


def make_coffee(request, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {request} ☕. Enjoy!")


working = True

while working:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        working = False
    elif choice == "report":
        print(f'Water: {resources["Water"]}ml')
        print(f'Milk: {resources["Milk"]}ml')
        print(f'Coffee: {resources["Coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                profit += drink["cost"]
                print(f"Here is ${change} in change.")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Not enough money, refunded coins")
