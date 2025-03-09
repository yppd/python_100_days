import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
# TODO-1: - Use a while loop to let the user guess again.
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    # TODO-2: Change the for loop so that you keep the previous correct
    # letters in display.

# every time it reconstructs the display
    for letter in chosen_word:
        if letter == guess:
            display += letter  # take the letter from chosen word
            correct_letters.append(guess)
        elif letter in correct_letters:  # take the letter from correct_letters
            display += letter
        elif letter != chosen_word:
            display += "_"
            print(stages[-1])
            

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")
        print(correct_letters)
    print(stages[-1])
