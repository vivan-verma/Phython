pizza_price = 7

salad_price = 5

drink_price = 2

print("                Menu")

print ("Pizza  --------------------  7$")

print ("Salad  --------------------  5$")

print ("Drink -------------------- 2$")

order = input("Welcome to the cafe, What would you like:  ")


if (order == "pizza"):
    n_pizza = (int)(input("How many slices would you like? "))
    total_pizza_cost = n_pizza * 7
    print (total_pizza_cost, "$")
     
if(order == "salad"):
    n_salad = (int)(input("How many salads would you like to buy?"))
    print ("Your total today is", 2 * n_salad, "$")
