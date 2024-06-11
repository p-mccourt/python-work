import random

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = 0

if player_choice == 0:
    player_choice = rock
elif player_choice == 1:
    player_choice = paper
else:
    player_choice = scissors

computer_choice_rand = round(random.randint(0, 2))

if computer_choice_rand == 0:
    computer_choice = rock
elif computer_choice_rand == 1:
    computer_choice = paper
else:
    computer_choice = scissors

print(f"Your choice: {player_choice}")
print(f"Computer choose: {computer_choice}")

if (player_choice == rock and computer_choice == paper) or (player_choice == paper and computer_choice == scissors) or (player_choice == scissors and computer_choice == rock):
    print("You Lose")
elif player_choice == computer_choice:
    print("Same Choice!")
else:
    print("You Win")
