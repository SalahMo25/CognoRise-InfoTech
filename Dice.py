#DICE ROLLING SIMULATOR
import random

def dice():
    
    sides = int(input(f'Enter the number of sides:'))
    if sides > 6: 
        print('Invalid number of sides. The maximum number of sides is 6')
        sides = int(input(f'Enter the number of sides between 1 and 6 : '))

    
    rolls = int(input(f'Enter the number of rolls :'))
    
    for roll in range(1 , rolls+1):
        
        num = random.randint(1, sides)
        print(f'Roll {roll} => {num}')
    
        

dice()
    