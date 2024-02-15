Menu = {
    'latte': {
        'ingredients': {
            'water': 500,
            'milk': 200,
            'coffee': 100,
        },
        'cost': 150
    },
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 100
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 200
    }
}
profit = 0
resources = {
    'water': 1500,
    'milk': 1200,
    'coffee': 1100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"There is no enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = 0
    coins_five = int(input("How many 5Tsh coin?: "))
    coins_ten = int(input("How many 10Tsh coin?: "))
    coins_twenty = int(input("How many 20Tsh coin?: "))
    total = coins_ten*5 + coins_five*10 + coins_twenty*20
    return total


def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit +=coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your {change}Tsh change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}...Enjoy")


is_no = True
while is_no:
    choice = input("What would you like to have? (latte/ espresso/ cappuccino), Enter 'report' for the report and 'off'"
                   "to turn off the machine: ").lower()
    if choice == 'off':
        is_no = False
    elif choice == 'report':
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}ml")
        print(f"Money = {profit}Tsh")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
