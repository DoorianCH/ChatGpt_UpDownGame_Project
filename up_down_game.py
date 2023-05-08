import random

def guess_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guessed_number = None

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    # Keep asking for the player's guess until they guess the correct number
    while guessed_number != number_to_guess:
        try:
            guessed_number = int(input("Enter your guess: "))
        except ValueError:
            print("That's not a valid number. Please enter a number between 1 and 100.")
            continue

        if guessed_number < number_to_guess:
            print("Too low! Try again.")
        elif guessed_number > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")

if __name__ == "__main__":
    guess_number()
