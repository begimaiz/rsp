import random
import time


def generate_turn():
    list_letter = ['r', 's', 'p']
    return random.choice(list_letter)


def is_wrong(letter):
    if len(letter) == 1:
        if letter in 'rsp':
            return False
        else:
            print('Enter valid input! only one of P R S allowed')
            return True
    else:
        print('Enter valid input! only one character allowed')
        return True


def who_wins(u, c):
    if u == c:
        return 'Tie'
    elif (u == 'r' and c == 's') or\
            (u == 's' and c == 'p') or \
            (u == 'p' and c == 'r'):
        return 'user'
    elif (u == 'r' and c == 'p') or \
            (u == 'p' and c == 's') or \
            (u == 's' and c == 'r'):
        return 'computer'


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

    computer_wins = 0
    user_wins = 0
    user_input = ''
    game_limit = 20
    score = {'user': 0, 'computer': 0}

    while game_limit > 0 and user_wins <= 2 and computer_wins <= 2:

        wrong_input = True
        try_limit = 5
        while wrong_input and try_limit > 0:
            print()
            message = 'Enter R/S/P ('+str(try_limit)+'): '
            user_input = input(message)

            user_input = user_input.lower()
            wrong_input = is_wrong(user_input)

            try_limit -= 1

        if wrong_input:
            game_limit = 0
            continue

        computer_input = generate_turn()
        time.sleep(1)
        print('Computer entered the following:', computer_input)
        print()
        print('Calculating...')
        print()
        time.sleep(2)
        print('Between:')
        print('User:', interpreter(user_input))
        print('Computer:', interpreter(computer_input))
        winner = who_wins(user_input, computer_input)
        print()
        print('Wins:', winner)

        game_limit += 1

        if winner == 'user':
            user_wins += 1
            score['user'] += 1
        elif winner == 'computer':
            computer_wins += 1
            score['computer'] += 1
        else:
            pass

        print()
        print(score)
        print()


def main():
    print('--------------NEW GAME--------------')
    new_game()

    session_limit = 20
    play_again = True
    try_limit = 10

    while play_again and session_limit > 0 and try_limit > 0:
        session_limit -= 1
        print()
        message = 'Play again? y/n ('+str(try_limit)+'): '
        play = input(message)
        play = play.lower()

        print()

        if play == 'y':
            print('--------------NEW GAME--------------')
            new_game()

        elif play == 'n':
            play_again = False

        else:
            print('Enter valid input!')
            try_limit -= 1


main()
