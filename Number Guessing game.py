import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I have chosen a number between 1 and 100.")
print (f"You have {max_attempts} attempts to guess the number ")
while attempts < max_attempts:
    guess = input("Enter your guess:")

    if not guess.isdigit():
        print("Please enter a valid number:")
        continue
    guess = int(guess)

    attempts += 1

    if guess < secret_number:
        print("Too low! try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've Guessed the number {secret_number} in {attempts} attempts.")
        break
else:
    print(f"Sorry! You've used all your attempts . the number was {secret_number}.")
