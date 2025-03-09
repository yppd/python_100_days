import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = ""
correct_letters = []
game_over = False


for letter in chosen_word:
    display += "_"
print(display)

while not game_over:

    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter  # take the letter from chosen word
            correct_letters.append(guess)
        elif letter in correct_letters:  # take the letter from correct_letters
            display += letter
        elif letter != chosen_word:
            display += "_"


    wprint(display)
    print(correct_letters)

    if "_" not in display:
        game_over = True
        print("You win")
        print(correct_letters)