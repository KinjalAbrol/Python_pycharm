print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
    print("you have to pay $15")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 2


    else:
        bill += 0

elif size == "M":
    bill = 20
    print("you have to pay $20")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3

    else:
        bill += 0

else:
    bill = 25
    print("you have to pay $25")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3

    else:
        bill += 0

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
    print("your total bill is:" + "$"+ str(bill))
else:
    bill += 0
    print("your total bill is:" + "$" + str(bill))
