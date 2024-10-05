print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("you are at a crossroad.")
choice1 = (input("where you want to go? l or r? "))

if choice1 ==  "l":
     choice2 = (input("swim or wait?\n"))
     if choice2 == "wait":
         choice3 = (input("which door you want to open? red or yellow or blue\n"))
         if choice3 == "red":
             print("game over!")
         elif choice3 == "yellow":
             print("you win!")
         elif choice3 == "blue":
             print("game over!")
         else:
             print("game over!")

     else:
         print("game over!")

else:
    print("game over!")