#  nested statement
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("what is the age?"))
#     if age <= 18:
#         print("you have to pay $7")
#     else:
#         print("you have to pay $12")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# elif statement
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("what is the age?"))
#     if age <= 12:
#         print("you have to pay $5")
#     elif age <= 18:
#         print("you have to pay $12")
#     else:
#         print("you have to pay $7")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# multiple example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is the age?"))
    if age <= 12:
        bill = 5
        print("you have to pay $5")
    elif age <= 18:
        bill = 12
        print("you have to pay $12")
    else:
        bill = 7
        print("you have to pay $7")
        photos = input("Do you want photos? ")
        if photos == "yes":
            bill += 3
            print("your total bill is:" + str(bill))
            # print(f"your total bill is {bill}")
        else:

            print(f"your total bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
