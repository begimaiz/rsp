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


def interpreter(letter):
    if letter == 'p':
        return 'Paper'
    elif letter == 'r':
        return 'Rock'
    elif letter == 's':
        return 'Scissors'
    else:
        return 'Tie'


def new_game():

    try_limit = 5
    wrong_input = True

    while wrong_input and try_limit > 0:
        user_input = input('enter one of there three to make a move R S P: ')
        user_input = user_input.lower()
        wrong_input = is_wrong(user_input)
        try_limit -= 1

    computer_input = generate_turn()
    print('Between', interpreter(user_input), interpreter(computer_input))
    print('Wins:', interpreter(who_wins(user_input, computer_input)))


def main():
    game_limit = 6
    play_again = True
    try_limit = 10

    while play_again and game_limit > 0 and try_limit > 0:
        new_game()
        game_limit -= 1
        play = input('play again? (y/n):')
        if play in 'yY':
            continue
        elif play in 'nN':
            play_again = False
        else:
            print('enter valid input')
            try_limit -= 1

main()

