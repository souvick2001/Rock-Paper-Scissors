# Rock Paper Scissors

import random
rock = "✊"
paper = "🫱"
scissors = "✌️"

image = [rock, paper, scissors]
user = int(input("Enter your option (Type 0 for rock, type 1 for paper, type 2 for scissors) : "))
if user >=3 or user<0 :
  print("You type invalid number, you lose !")
else :
  print(image[user])
  computer_choice = random.randint(0,2)
  print(f"Computer choose : ")
  print(image[computer_choice])
  
  if user >=3 or user<0 :
    print("You type invalid number, you lose !")
  elif user == 0 and computer_choice == 2:
    print("You win")
  elif computer_choice == 0 and user == 2:
    print("You lose")
  elif computer_choice > user:
    print("You lose")
  elif user > computer_choice :
    print("You win")
  elif computer_choice == user:
    print("Match draw !")
