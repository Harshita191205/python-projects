import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!......")
    print("I'm thinking of a number between 1 and 100.")
    print("------------------------------------------------------------------------------------------")

    difficulty_level = input("Choose a difficulty level (easy, medium, hard): ")
    if difficulty_level.lower() == "easy":
        max_attempts = 10
    elif difficulty_level.lower() == "medium":
        max_attempts = 5
    elif difficulty_level.lower() == "hard":
        max_attempts = 3
    else:
        print("Invalid difficulty level.\n......Defaulting to medium.....")
        max_attempts = 5

    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess and attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

        if attempts == max_attempts - 1:
            print("Last chance! Make it count.")

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number ({number_to_guess}) in {attempts} attempts.")
    else:
        print(f"Game over! The number was {number_to_guess}. Better luck next time.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing!")

# main program 
number_guessing_game()