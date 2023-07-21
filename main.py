import data
#TODO: 1.When the user enters “report” to the prompt, a report should be generated that shows the current resource values
def repporting(current_water,current_milk,current_cofee,current_money) :
    """This function report the ramaining Resources and the Money gained"""
    print(f"Water: {current_water}ml")
    print(f"Milk: {current_milk}ml")
    print(f"Coffee: {current_cofee}g")
    print(f"Money: {current_money}$")

#TODO: 2.Check if resources are sufficient
def is_suffisiant(current_water,current_milk,current_cofee,wanted_water,wanted_milk,wanted_cofee) :
    """This function check if there are suffiiant resources to prepare wathever user wanted """
    if current_water<wanted_water :
        print("Sorry there is not enough water")
        suffisiant=False
    if current_milk<wanted_milk :
        print("Sorry there is not enough milk")
        suffisiant = False
    if current_cofee<wanted_cofee :
        print("Sorry there is not enough coffee")
        suffisiant = False
    if current_water>=wanted_water and current_milk>=wanted_milk and current_cofee>=wanted_cofee :
        suffisiant=True
    return  suffisiant
#TODO : 3.Process coins
def Process_coins() :
    """This function will process the coins and calculate the totale money insered by user"""
    print("Please insert coins.")
    quarters=int(input("How many carters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    return money
#TODO: 4.Check transaction successful?
def transaction_Done(wanted_product,quantities,product_water,product_milk,product_coffee ,cost,current_water,current_milk,current_cofee,current_money,money) :
    """This function check if user input the requred money or not , and change the output according to the situation"""
    if money<cost :
        print("Sorry that's not enough money. Money refunded.")
    else :
        current_money+=cost
        if 'water' in quantities:
            current_water -= product_water
        if 'milk' in quantities:
            current_milk -= product_milk
        if 'coffee' in quantities:
            current_cofee -=product_coffee
        refund=round(money-cost,2)
        if refund>0:
            print(f"Here is ${refund} dollars in change.")
        print(f"Here is your {wanted_product}. Enjoy!")
    return [current_water,current_milk,current_cofee,current_money]

#TODO: let's build the machine Algorithme step by step
def Machine(Wanted,current_water,current_milk,current_cofee,current_money) :
    product = data.MENU[Wanted]
    product_cost=product['cost']
    quantities = product['ingredients']
    if 'water' in quantities:
        product_water = quantities['water']
    if 'milk' in quantities:
        product_milk = quantities['milk']
    if 'coffee' in quantities:
        product_coffee = quantities['coffee']
    ## see if the current uantities are suffissiants
    suffisiant=is_suffisiant(current_water=current_water,current_milk=current_milk,current_cofee=current_cofee,wanted_water=product_water,wanted_milk=product_milk,wanted_cofee=product_coffee)
    if suffisiant==True :
        ### process the insered coin
        inserred_money=Process_coins()
        ##see if the money is suffisiant and do the job
        new_results=transaction_Done(wanted_product=Wanted,quantities=quantities,product_water=product_water,product_milk=product_milk,product_coffee=product_coffee,cost=product_cost,current_water=current_water,current_milk=current_milk,current_cofee=current_cofee,current_money=current_money,money=inserred_money)
    return new_results

#TODO: finally let's begin the workflow
initial_water=data.resources['water']
initial_milk=data.resources['milk']
initial_cooffee=data.resources['coffee']
intitial_profit=data.profit
wanted = input("What would you like? (espresso/latte/cappuccino): ").lower()
if wanted!="report" and wanted!="off" :
    results=Machine(Wanted=wanted,current_water=initial_water,current_cofee=initial_cooffee,current_milk=initial_milk,current_money=intitial_profit)
    current_water=results[0]
    current_milk=results[1]
    current_coofee=results[2]
    current_money=results[3]
if wanted=="report":
    repporting(current_water=initial_water, current_milk=initial_milk, current_money=intitial_profit,current_cofee=initial_cooffee)
    reported=True
while wanted != "off":
        wanted = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if wanted!="report" and wanted!="off" :
            if reported==True :
                results = Machine(Wanted=wanted, current_water=initial_water, current_cofee=initial_cooffee,current_milk=initial_milk, current_money=intitial_profit)
                reported=False
            if wanted=="report" :
                results = Machine(Wanted=wanted, current_water=current_water, current_cofee=current_coofee,current_milk=current_milk, current_money=current_money)
            current_water = results[0]
            current_milk = results[1]
            current_coofee = results[2]
            current_money = results[3]
        else:
            repporting(current_water=current_water,current_milk=current_milk,current_money=current_money,current_cofee=current_coofee)

