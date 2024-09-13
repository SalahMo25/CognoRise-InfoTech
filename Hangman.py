import random
def hangman():
    players = ['ronaldo' , 'salah' , 'messi']
    player = random.choice(players)

    guessed_player = ['_'] * len(player)
    tries = 7
    gussed_letters =[]
    guessed = False
    
    
    print(f'================== Welcome to Hangman Game! ================== ')
    
    
    def display_player():
        print(' '.join(guessed_player))
    
    while not guessed and tries > 0:
        
        letter = input("Guess a letter: ").lower()

        
        if len(letter) == 1 and letter.isalpha():
            if letter in gussed_letters:
                print(f'You already guessed the letter {letter} before ')
                
            elif letter not in player:
                print(f'{letter} is not a player name')
                tries -= 1
                gussed_letters.append(letter)
                
            else:
                print(f'{letter} in player name , GOOOOOOD !!')
                gussed_letters.append(letter)
                for i in range(len(player)):
                    if player[i] == letter:
                        guessed_player[i] = letter
                
        else:
            print('Invalid input. Please enter a single letter.')
            
        
        
        
            
        if '_' not in guessed_player:
                display_player()
                print("Congratulations! You guessed the word!")
                break
            
    else:
            print(f"Sorry, you ran out of tries. The word was '{player}'.")
hangman()
        
play_again = input("Do you want to play again? (y/n): ").lower()
if play_again == 'y':
    hangman()
