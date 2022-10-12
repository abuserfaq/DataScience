#/usr/bin/python3
"""AutoFind game
    Code to show some indian code skills
"""

from random import randint
from numpy import less, mean

def gen (times:int=100) -> int:
    """Generate random number for guessing
    Args:
        times (int, optional): maximum value of guessing number. Defaults to 100.
    Returns:
        int: returning number for guessing
    """
    return randint(1, times)

def guess(number):
    """main guessing function
    Args:
        number (_type_): _description_
    Returns:
        count: number of steps for guessed number
    """
    start_number = 0 # start number
    end_number = 100 #end number
    current_guess_number = 0 # current random number
    count = 0 # step number

    while current_guess_number != number:
        count += 1
        current_guess_number = randint(start_number,    end_number)
        if current_guess_number < number:
            start_number += (number - current_guess_number)//2 +1
            print(f'Nope - need more+  {current_guess_number} to {number}')
            #print(f'{current_guess_number} += ({number} - {current_guess_number})/2 = {start_number}\r\n')
            
        elif current_guess_number > number:
            start_number -= (current_guess_number - number)//2
            end_number =  current_guess_number
            print(f'nope - need less-  {current_guess_number} to {number}')
            #print(f'{current_guess_number} -= ({current_guess_number}-{number})/2 = {start_number}\r\n')
            
    #print(f'You win! {number}, by {count} steps')
    print(f'win  {count} steps . {current_guess_number} - {number} ')
    return count
    
def game(total_games:int=10) ->int:
    """Main game function
    Args:
        totalgames (int, optional): how many games to play. Defaults to 1000.
    Returns:
        int: return list of tryies
    """
    x = []
    for i in range(total_games):
        x.append(guess(gen()))
        i += 1
    
    print (f'minimum steps = {min(x)}; max = {max(x)}; среднее = {mean(x)}')


game()

"""
x = 50
1-100
g = 75
need less
g = 75//2

rand(75//2 , 75-1)

"""