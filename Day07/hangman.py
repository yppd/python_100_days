import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
placeholder = ""
guess = input("Guess a letter:   ").lower()
# print(guess)
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
for word_length in len(chosen_word):
    placeholder += "_"

print(placeholder)



display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display +="_"

# TODO-4
'''
- Create an empty String called placeholder.
- For each letter in the chosen_word, add a _ to placeholder.
So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.
- Print out hint.'''





# TODO-5
'''
- Create an empty string called "display".
- Loop through each letter in the chosen_word
- If the letter at that position matches guess then reveal that letter in the display at that position.
e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
- Print display and you should see the guessed letter in the correct position. 
But every letter that is not a match is represented with a "_".'''

# TODO-6
'''
- Use a while loop to let the user guess again.
- The loop should only stop once the user has guessed all the letters in the chosen_word.
- At that point display has no more blanks ("_"). Then you can tell the user they've won.
'''


# TODO-7
''' 
- Update the for loop so that previous guesses are added to the display String.
- At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.'''

