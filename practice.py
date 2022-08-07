customer = input("What would you like? (expresso/latte/cappuccino): ")

if customer == 'espresso':
    print("Please insert coins.")
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickels = float(input("how many nickels? "))
    pennies = float(input("how many pennies? "))

    quarter = quarters * .25
    dime = dimes * .10
    nickel = nickels * .05
    penny = pennies * .01

    money = quarter + dime + nickel + penny
    exchange = round(money - 1.5, 2)
    print(f"Here is ${exchange} in change.")
    print(f"Here is your {customer}. Enjoy!")



