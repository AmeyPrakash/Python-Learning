import random
choices = ["rock", "paper", "scissor"]
player = input("Enter rock paper or scissor:").lower()
computer = random.choice(choices)
print(f"You chose : {player}")
print(f"Coputer chose : {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissor":
        print("You win! Rock crushes scissors.")
    else:
        print("You lose! Paper covers rock.")
elif player == "paper":
    if computer == "rock":
        print("You win! Paper cocvers rock.")
    else:
        print("You lose! Scissor cuts paper.")
elif player == "scissor":
    if computer == "paper":
        print("You  win! Scissor cuts paper.")
    else:
        print("You lose! Rock crushes scissors.")
else:
    print("Invalid Input! Please choose rock, Paper or scissors.")
                                     