
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

is_machine_on = True

money = 0

while is_machine_on:

#Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    coffe_type = input("What would you like? (espresso/latte/cappuccino):")

#Turn off the Coffee Machine by entering “off” to the prompt

    if coffe_type == "off":        
        is_machine_on = False

    if coffe_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    
    if coffe_type not in {"report", "off"}:
    #Check resources sufficient?

        if resources["water"] < MENU[coffe_type]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        
        elif coffe_type!="espresso" and resources["milk"] < MENU[coffe_type]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.”")

        elif resources["coffee"] < MENU[coffe_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.") 

        else:

            #Process coins.

            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            inserted_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


            #Check transaction successful?

            if inserted_money < MENU[coffe_type]["cost"]:
                print("Sorry that's not enough money. Money refunded.")

            elif inserted_money >= MENU[coffe_type]["cost"]:

                resources["water"] -= MENU[coffe_type]["ingredients"]["water"]

                if coffe_type!="espresso":
                    resources["milk"] -= MENU[coffe_type]["ingredients"]["milk"]

                resources["coffee"] -= MENU[coffe_type]["ingredients"]["coffee"] 

                money += MENU[coffe_type]["cost"] 

                if inserted_money > MENU[coffe_type]["cost"]:

                    change = inserted_money - MENU[coffe_type]["cost"]
                    print(f"Here is ${round(change, 2)} dollars in change.")
                
                #Make Coffee
                print(f"Here is your {coffe_type} ☕.Enjoy!")


    

