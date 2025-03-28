from art import logo
from random import randint
# print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.\nGuess again.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.\nGuess again. ")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
# Choosing a random number between 1 and 100
    print("I'm thinking of an number between 1 and 100.")
    answer = randint(1, 101)
# Let the user guess a number
    turns = set_difficulty()

# Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You 've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
