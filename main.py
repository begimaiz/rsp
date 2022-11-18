import random

def generate_turn():
    letter = ''
    random_number = random.randint(2)
    if random_number == 0:
        letter = 'r'
    elif random_number == 1:
        letter = 's'
    elif random_number == 2:
        letter = 'p'
    else:
        letter = 'n'
    return letter


def is_wrong(letter):
    if len(letter) == 1:
        if letter in 'rsp':
            return False
        else:
            return True
    else:
        return True

def new_game():

    game_limit = 5
    wrong_input = True

    while wrong_input and game_limit > 0:
        user_input = input('enter one of there three to make a move R S P: ')
        user_input = user_input.lower()
        wrong_input = is_wrong(user_input)
        game_limit -= 1

new_game()