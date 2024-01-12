""" 
    Build a console-based game where the user plays against the computer in the classic rock-paper-scissors game. 
    Ask the user to choose their move (Rock, Paper, Scissors), simulate the computer's move, and determine the winner of each round.
    The program should work with lowercase or uppercase user input. 
    If the user enters an invalid value, a message should be displayed and the program ended.
    Show the chosen moves at the end. 
    additional: If you win, display a Custom message: Ex.: Rock crushes scissors. Paper covers rock. Scissors cuts paper.
"""

import random

def main():
    random_input = random.randint(1,3)
    user_move = input("\nChoose your move (Rock, Paper, Scissors): ").upper()    
    computer_move = ""
    valid_user_move = True

    # 1 - rock, 2 - paper, 3 - scissors

    if not(user_move == "ROCK" or user_move == "PAPER" or user_move == "SCISSORS"):
        print("Wrong input! Please try again.")
        valid_user_move = False

    if random_input == 1:
        computer_move = "ROCK"
    elif random_input == 2:
        computer_move = "PAPER"
    elif random_input == 3:
        computer_move = "SCISSORS"

    if valid_user_move:
        if user_move == computer_move:
            print("No winner. It's a tie.")
        elif user_move == "ROCK" and computer_move == "SCISSORS":
            print("Congrats!\nYou won! :D")
            print("Rock crushes Scissors")
        elif user_move == "PAPER" and computer_move == "ROCK":
            print("Congrats!\nYou won! :D")
            print("Paper covers Rock")
        elif user_move == "SCISSORS" and computer_move == "PAPER":
            print("Congrats!\nYou won! :D")
            print("Scissors cuts Paper")
        else:
            print("Better luck next time!\nYou lost! :~(")
        
        print("\n(Your choice) " + user_move +" vs "+computer_move+" (Computer choice)\n")

    

if __name__ == "__main__":
    main()
