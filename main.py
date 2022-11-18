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
    if user == computer:
        return 'tie'
    elif user == 'r' and computer == 's':
        return user
    elif user == 'r' and computer == 'p':
        return computer
    elif user == 'p' and computer == 'r':
        return user
    elif user == 'p' and computer == 's':
        return computer
    elif user == 's' and computer == 'p':
        return user
    elif user == 's' and computer == 'r':
        return computer



def new_game():

    game_limit = 5
    wrong_input = True

    while wrong_input and game_limit > 0:
        user_input = input('enter one of there three to make a move R S P: ')
        user_input = user_input.lower()
        wrong_input = is_wrong(user_input)
        game_limit -= 1

    computer_input = generate_turn()
    print('between', user_input, computer_input)
    print('wins:', who_wins(user_input, computer_input))


new_game()