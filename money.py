amount = (int)(input("How much money do you have?  "))
type = input("Is it pounds or dollars?  ")


if (type == "dollars"):
    print("You have", amount * 0.74, "pounds")

if( type == "pounds"):
    print( "You have", amount * 1.36, "dollars")
