import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
lives = 6

for char in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"********************* {lives}/6 LIVES LEFT *********************")

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(F"********************** IT WAS {chosen_word}. YOU LOSE! **********************")

    if "_" not in display:
        game_over = True
        print("YOU WIN!")
    elif lives == 0:
        game_over = True
        print("YOU LOSE!")

    print(stages[lives])
