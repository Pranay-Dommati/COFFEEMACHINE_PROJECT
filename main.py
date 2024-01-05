MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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

MONEY=0
QUARTERS=DIMES=NICKLES=PENNIES=0

def enough_resources_2(water,milk,coffee):
    global resources
    resources['water']=resources['water']-water
    resources['milk']=resources['milk']-milk
    resources['coffee']=resources['coffee']-coffee

def total_money_change(QUARTERS, DIMES, NICKLES, PENNIES, coffee_type):
    global MONEY
    MONEY+=coffee_type


    money=0
    money += 1 / 4 * QUARTERS
    money += 1 / 10 * DIMES
    money += 1 / 20 * NICKLES
    money += 1 / 100 * PENNIES
    if money>=coffee_type:
        enough_resources_2(MENU[type_coffee]['ingredients']['water'],MENU[type_coffee]['ingredients']['milk'],
                         MENU[type_coffee]['ingredients']['coffee'])
        change=money-coffee_type
        return [True,change]
    else:
        return [False,0]

def coffee_selection(type_coffee):
    print("please insert coins:")
    QUARTERS = int(input("how many quarters: "))
    DIMES = int(input("how many dimes: "))
    NICKLES = int(input("how many nickles: "))
    PENNIES = int(input("how many pennies: "))
    enough_money = total_money_change(QUARTERS, DIMES, NICKLES, PENNIES, MENU[type_coffee]['cost'])
    if enough_money[0]:
        print(f"Take your change {round(enough_money[1],2)}")
        print(f"Here is your {type_coffee} ☕,enjoy..!")
    else:
        print("sorry that's not enough money..your money refunded")

def enough_resources(water,milk,coffee):
    global resources
    if resources['water']>=water and resources['milk']>=milk and resources['coffee']>=coffee:
        return True
    else:
        return False

should_continue=True
print("""     ..
      ..  ..
            ..
             ..
            ..
           ..
         ..
##       ..    ####
##.............##  ##
##.............##   ##
##.............## ##
##.............###
 ##...........##
  #############
  #############
################# """)
print("""\n+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+
 |W|E|L|C|O|M|E| |T|O| |A|.|A| |C|A|F|E|
 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+""")
while should_continue:

    continue_=input("DO YOU WANT TO REFRESH WITH A CUP OF COFFEE TYPE 'Y' OR 'N': ").lower()
    if continue_=='y':
        pass
    elif continue_=='n':
        break
    type_coffee=input("What would you like? (espresso/latte/cappuccino) or type 'report' to see resources:").lower()

    if type_coffee=='espresso':
        is_enough=enough_resources(MENU['espresso']['ingredients']['water'],MENU['espresso']['ingredients']['milk'],
                         MENU['espresso']['ingredients']['coffee'])
        if is_enough:
            pass
        else:
            print("sorry there is not enough resources")
            break
        coffee_selection(type_coffee)
    elif type_coffee=="latte":
        is_enough=enough_resources(MENU['latte']['ingredients']['water'], MENU['latte']['ingredients']['milk'],
                         MENU['latte']['ingredients']['coffee'])
        if is_enough:
            pass
        else:
            print("sorry there is not enough resources")
            break
        coffee_selection(type_coffee)
    elif type_coffee=="cappuccino":
        is_enough=enough_resources(MENU['cappuccino']['ingredients']['water'], MENU['cappuccino']['ingredients']['milk'],
                         MENU['cappuccino']['ingredients']['coffee'])
        if is_enough:
            pass
        else:
            print("sorry there is not enough resources")
            break
        coffee_selection(type_coffee)

    elif type_coffee=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}gm")
        print(f"money: {MONEY}$")
    else:
        print("please choose correct one")



