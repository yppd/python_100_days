def calculate_love_score(name1, name2):
# your code here
    true_counter = 0
    love_counter = 0
    names = name1.replace(" ", "").lower() + name2.replace(" ", "").lower()

    for letter in names:
        if letter in "true":
            true_counter += 1
    for letter in names:
        if letter in "love":
            love_counter += 1
            love_score = str(true_counter) + str(love_counter)

    print(love_score)

calculate_love_score("Kim Kardashian", "Kanye West")