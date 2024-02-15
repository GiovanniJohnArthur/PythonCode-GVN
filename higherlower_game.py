import os
import random
import game_logo
import game_database

print(game_logo.logo)
score = 0


def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},a {description},from {country}"


def check_answer(guess, follower_count1, follower_count2 ):
    if follower_count1 < follower_count2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False


account2 = random.choice(game_database.data)
continue_flag = True
while continue_flag:
    account1 = account2
    account2 = random.choice(game_database.data)
    while account1 == account2:
        account2 = random.choice(game_database.data)

    print(f"Compare 1: {display_accountinfo(account1)}")
    print(game_logo.vs)
    print(f"Compare 2: {display_accountinfo(account2)}")
    guess = int(input("Who has more followers? Type 1 or 2: "))
    follower_count1 = account1["follower_count"]
    follower_count2 = account2["follower_count"]

    is_correct = check_answer(guess, follower_count1, follower_count2)
    os.system('cls')
    if is_correct:
        score += 1
        print(f"Your right. Your score is: {score}")
        print()
    else:
        print(f"Your wrong. Your final score is : {score}")
        continue_flag = False
