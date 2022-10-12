# /usr/bin/python3
"""Game: AutoGuessNumber
    author: Alexey Soloviev 115 potok.
    mail: abuser_faq@mail.ru
"""

from random import randint
from numpy import mean


def gen(num: int = 100) -> int:
    """function return random number from 1 to "num" space

    Args:
        num (int, optional): Defaults to 100.

    Returns:
        int: random number
    """
    return randint(1, num)


def guess(number):
    """guessing function

    Args:
        number (_type_): number for guessing

    Returns:
        _type_: returning nubmer of steps taken for correct guessing
    """
    start_number = 0  # start number
    end_number = 100  # end number
    current_guess_number = 0  # current random number
    count = 0  # step number

    while current_guess_number != number:
        count += 1
        current_guess_number = randint(start_number, end_number)
        if current_guess_number < number:
            start_number = current_guess_number + \
                (end_number-current_guess_number)//2  # change start number of guessing to previous value+ half of difference between prev. value and end number

            #print(f'{count} step: nope - need more+  {current_guess_number}  to {number}')
        elif current_guess_number > number:
            # dropping start number to half of previous value
            start_number = current_guess_number//2
            # change max guessing value to curent guessed number
            end_number = current_guess_number
            #print(f'{count} step: nope - need less-  {current_guess_number} - {number}')

    #print(f'win  {count} steps . {current_guess_number} is {number} ')
    return count


def game(total_games: int = 1000):
    """game starting function

    Args:
        total_games (int, optional):  How many times to guess numbers. Defaults to 1000.

    Returns:
        printing stats
    """
    x = []
    for i in range(total_games):
        x.append(guess(gen()))
        i += 1
    print(f'minimum steps = {min(x)}; max = {max(x)}; average = {mean(x)}')


game()  # Let's play!
