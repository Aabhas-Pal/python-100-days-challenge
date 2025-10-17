#Hey guys welcome to my journey of python programming it is the fourth project ever created.
#Please stay tuned for upcoming projects.

import random
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the rock paper and scissors game")

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

game_options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(game_options[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_options[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice == 1 and user_choice == 2:
    print("You lose!")
elif computer_choice == 1 and user_choice == 0:
    print("You lose!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
print("Thanks for playing with us!!!")
