#/usr/bin/python3
from random import randint
from numpy import less, mean

def gen (num:int=100) -> int:
    return randint(1, num)

def guess(number):
    start_number = 0 # start number
    end_number = 100 #end number
    current_guess_number = 0 # current random number
    count = 0 # step number

    while current_guess_number != number:
        count += 1
        current_guess_number = randint(start_number, end_number)
        if current_guess_number < number:
            start_number = current_guess_number + (end_number-current_guess_number)//2
            
            #print(f'{count} step: nope - need more+  {current_guess_number}  to {number}')
        elif current_guess_number > number:
            start_number = current_guess_number//2
            end_number =  current_guess_number
            #print(f'{count} step: nope - need less-  {current_guess_number} - {number}')
    #print(f'win  {count} steps . {current_guess_number} is {number} ')
    return count
    
def game(total_games:int=1000) ->int:
    x = []
    for i in range(total_games):
        x.append(guess(gen()))
        i += 1
    print (f'minimum steps = {min(x)}; max = {max(x)}; среднее = {mean(x)}')

game()
