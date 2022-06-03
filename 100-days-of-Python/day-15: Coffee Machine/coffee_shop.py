from menu import MENU,resources

money = 0

machine_on = True

def prompt_customer():
    drink = input("What would you like to drink? (espresso/latte/cappuccino) ")
    return drink

def report():
    print("Water : "+resources['water']+"ml")
    print("Milk : "+resources['milk']+"ml")
    print("Coffee : "+resources['coffee']+"g")
    print("Money : $"+money)

def coin_count():
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quater = 0.25
    
    q = float(input("How many quarters? "))
    d = float(input("How many dimes? "))
    n = float(input("How many nickels? "))
    p = float(input("How many pennies? "))
    
    total = q*quater + d*dime + n*nickel + p*penny
    return total
    
def check_res(bev_ing):
    #checks resources for making a beverage
    for item in bev_ing:
        if bev_ing[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def check_transaction(money_put, drink_cost):
    if money_put >= drink_cost:
        change = round(money_put - drink_cost,2)
        print(f"Your change is: {change}")
        global money
        money+= drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_order(bev_name, bev_ing):
    for item in bev_ing:
        resources[item] -= bev_ing[item]
    print("Here's your "+bev_name+" order. Enjoy :)")
    

while machine_on:
    answ = prompt_customer()
    
    if answ == "off":
        machine_on = False
        exit()
    elif answ == "report":
        report()
    else:
        bev = MENU[answ]
        if check_res(bev["ingredients"]):
            payment = coin_count()
            if check_transaction(payment,bev["cost"]):
                make_order(answ, bev["ingredients"])
    