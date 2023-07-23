import random

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

#Write your code below this line 👇
game = [rock,paper,scissors]
gamer_choice=input("enter 0 for rock 1 for paper and 2 for scissors\n")
gamer_choice=int(gamer_choice)
print(game[gamer_choice])
computer_choice=random.randint(0,2)
print(game[computer_choice])
if gamer_choice >= 3 or gamer_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif gamer_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and gamer_choice == 2:
  print("You lose")
elif computer_choice > gamer_choice:
  print("You lose")
elif gamer_choice > computer_choice:
  print("You win!")
elif computer_choice == gamer_choice:
  print("It's a draw")