# Create a number guessing game where the user has 5 attempts to guess a secret number between 1 and 50. 
# Use continue for invalid inputs (outside range) and break when guessed correctly.

secret = 25
attempts = 0

while attempts < 5:
    guess = int(input())
    attempts += 1
    if guess == secret:
        print(f"Correct! You guessed in {attempts} attempts.")
        quit()
    elif guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    if attempts == 5:
        print("Game over")
        quit()