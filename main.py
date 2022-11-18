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

