from art import logo, vs
from game_data import data
import random


def format_data(account):
    """ Takes the account data and returns the printable format. """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country} "


def check_answer(user_guess, a_follower, b_follower):
    """ Takes a user's guess and the followers count and returns if they got it right"""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

    print(logo)
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

#*### My Version ######

# #function to choose a dictionary from game data list
# def data_choice():
#     a = random.choice(data)
#     return a


# play_game = True
# score = 0
# comparison_dict = {"b": data_choice()}
# print(logo)

# while play_game:
#     comparison_dict["a"] = comparison_dict["b"]
#     comparison_dict["b"] = data_choice()
#     if comparison_dict["a"]["name"] == comparison_dict["b"]["name"]:
#         comparison_dict["b"] = data_choice()

#     print(f"Compare A: {comparison_dict["a"]["name"]}, a {comparison_dict["a"]["description"]}, from {comparison_dict["a"]["country"]}.")
#     print(vs)
#     print(f"Against B: {comparison_dict["b"]["name"]}, a {comparison_dict["b"]["description"]}, from {comparison_dict["b"]["country"]}.")
#     winning_answer = ""
#     if comparison_dict["a"]["follower_count"] > comparison_dict["b"]["follower_count"]:
#         winning_answer = comparison_dict["a"]
#     else:
#         winning_answer = comparison_dict["b"]

#     choice = input("Who has more followers? Type 'A' or 'B': ").lower()
#     print("\n" * 20)
#     print(logo)
#     if comparison_dict[choice]== winning_answer:
#         score += 1
#         print(f"You're right! Current score: {score}")
#         comparison_dict["a"] = winning_answer

#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         play_game = False
