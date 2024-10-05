rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose? type 0 for rock,1 for paper, 2 for scissors?\n"))
print(game_images[user_choice])
import random
computer_choice = random.randint(0,2)
print("computer_choice:" + str(computer_choice))
print(game_images[computer_choice])
# (f"computer choice"{computer choice}
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("draw")