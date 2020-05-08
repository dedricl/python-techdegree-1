"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
import random

    
def start_game():
# write your code inside this function.
    
    random_number = random.randrange(1, 11)
     
    player_guess = 0
    
    player_attemps = 1
    
    high_score = 1000    
    
    print("#"* 40 +" \nWelcome to the Number Guessing Game !!!!\n" + "#" * 40)
    while player_guess != random_number:
        try:
            player_guess = int(input("Guess the secret number betwenn 1 and 10?  ")) 
        except ValueError:
            print("Sorry that not valid! It must be a number")
            
        else:
            if player_guess > 10 or player_guess < 0:
                print("Wrong value range. Try again")
                player_attemps += 1
            elif player_guess > random_number:
                    print("It's lower")
                    player_attemps += 1     
            elif player_guess < random_number:
                print("It's higher")
                player_attemps += 1
            else:
                print("You guess correct! It only took you {} attemps.".format(player_attemps))
                if player_attemps < high_score:
                    high_score = player_attemps
                play_again = input("Would you like to play again? Y/N ")
                if play_again.upper() == "Y":
                    print("The High Score is {}".format(high_score))
                    random_number = random.randrange(1, 11)
                    player_guess = 0
                    player_attemps = 1
                elif play_again.upper() == "N":
                    print("Thanks for playing my game!! See you next time!")
                    break
                else:    
                    print("Invaild Value! Please type 'y' for yes and 'n' for  no")
                    print("Last chance before the game ends automatic")
                    play_again = input("Would you like to play again? Y/N ")
                    if play_again.upper() == "Y":
                        print("The High Score is {}".format(high_score))
                        random_number = random.randrange(1, 11)
                        player_guess = 0
                    elif play_again.upper() == "N":
                        print("Thanks for playing my game!! See you next time!")
                        break
                        player_attemps = 1  
                    else:    
                        print("Game is terminate")
                        
                        
    
# Kick off the program by calling the start_game function.


start_game()


























