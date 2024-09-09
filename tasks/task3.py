#Rock, Paper, Scissors Game

import random

def game():
    
    choice = [ "rock", "paper",  "scissors"]
    user_scour = 0
    computer_scour = 0
    print("\n======================= Welcome in Rock, Paper, Scissors Game ! =======================")
    
    while True:

        user_choice =  input(f'Enter Your Choice => rock , paper or scissors :').lower()
        while user_choice not in choice:
            print('Invalid choice. Please try again.')
            user_choice =  input(f'Enter Your Choice =>  rock , paper or scissors :').lower()

        computer_choice = random.choice(choice)
        print(f'Computer Choice IS {computer_choice} ')

        if user_choice == computer_choice :
            print("It's a tie!")
            print("Choice again")
            continue
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            result = 'WIIIIIIN'
            print(result)
            user_scour =+ 1
            
        else:
            result = 'LOOOOOOOOSER'
            print(result)
            
            computer_scour =+ 1
            
        print(f"\nScore: You ( {user_scour} ) - ( {computer_scour} ) Computer")
            
        another_game = input(f'Do you want to play again? (y/n): ').lower()
        if another_game != "y":
            print(f"THANKS FOR PLAYING ")
            break
game()