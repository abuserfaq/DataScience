import numpy as np

def gen (times:int=1000) -> int:
    return np.random.randint(1, times)

def guess(number):
    gnumo = 0
    gnum = 0
    gg = 1000
    count = 0
    #print(f'num is {number}')
    while gnum != number:
        count += 1
        gnum = np.random.randint(gnumo, gg)
        if gnum < number:
            #print(f'Nope - need more+  {gnum}')
            gnumo += int((number - gnum)/2)
            
            #print(f'{gnum} += ({number} - {gnum})/2 = {gnumo}\r\n')
            
        elif gnum > number:
            #print(f'nope - need less-  {gnum}')
            gnumo -= int((gnum - number)/2)
            gg =  gnum
            #print(f'{gnum} -= ({gnum}-{number})/2 = {gnumo}\r\n')
            
    #print(f'You win! {number}, by {count} steps')
    return count
    
      

def game(tm:int=100) ->int:
    x = []
    for i in range(tm):
        x.append(guess(gen()))
        i+=1
    print (f'minimum steps = {min(x)}')


game()