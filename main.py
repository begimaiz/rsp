import random

def generate_turn():
    list_letter = ['r', 's', 'p']
    return random.choice(list_letter)


def is_wrong(letter):
    if len(letter) == 1:
        if letter in 'rsp':
            return False
        else:
            return True
    else:
        return True

def who_wins(user,computer):
    pass

def new_game():

    game_limit = 5
    wrong_input = True

    while wrong_input and game_limit > 0:
        user_input = input('enter one of there three to make a move R S P: ')
        user_input = user_input.lower()
        wrong_input = is_wrong(user_input)
        game_limit -= 1

    computer_input = generate_turn()


print(generate_turn())