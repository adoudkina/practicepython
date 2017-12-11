'''
Created on Dec 10, 2017

@author: antonina

Description:

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
       print out a message of congratulations to the winner, 
       and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''

def getPlayerName(i):
    """Returns name of player i"""
    while True:
        str_to_ask = "Input name for Player " + str(i) + ": "
        name = input(str_to_ask).strip()
        if name != '': 
            return name
        
    
def getPlayerChoice():
    """Returns player choice: rock, paper or scissors"""
    while True:
        p_choice = input("Input 'r' for Rock, 'p' for Paper or 's' for Scissors: ").strip()
        if p_choice == 'r':
            return "Rock"
        elif p_choice == "p":
            return "Paper"
        elif p_choice == "s":
            return "Scissors"
        else: 
            print("Input is invalid. Try again")
            

def play(pl1, ch1, pl2, ch2):
    """1) Returns None if both choices are equal, otherwise returns player name who won.\n
    2) Decision table:    
     ------R-------S-------P
     R    tie     P2 W    P1 W
     S    P1 W    tie     P2 W
     P    P2 W    P1 W    tie

    """
    
    if ch1 == ch2:
        print("It's a tie.")
        return None
    if ch1 == 'Rock':
        if ch2 == 'Scissors':
            print("Congratulations,", pl1, ". You WON! Rock beats Scissors!")
            return pl1
        else:
            print("Congratulations,", pl2, ". You WON! Paper beats Rock!")
            return pl2
    elif ch1 == 'Scissors':
        if ch2 == 'Rock':
            print("Congratulations,", pl2, ". You WON! Rock beats Scissors!")
            return pl2
        else:
            print("Congratulations,", pl1, ". You WON! Scissors beat Paper!")
            return pl1 
    else:
        if ch2 == 'Rock':
            print("Congratulations,", pl1, ". You WON! Paper beats Rock!")
            return pl1
        else:
            print("Congratulations,", pl2, ". You WON! Scissors beat Paper!")
            return pl2 
    
    

def main():
    
    print("Welcome to the Rock-Paper-Scissors game!\n", "-" * 100)
    
    while True:
        answer = input("Would you like to start a new game? Input 'yes' or 'no': ")
        if answer == 'no': break
        elif answer == 'yes': 
            print("-" * 100)
            player1 = getPlayerName(1)
            player2 = getPlayerName(2)
            
            print("-" * 50)
            print(player1, ", make a choice.")
            choice1 = getPlayerChoice()
            print(player1, ", YOUR CHOICE IS -", choice1)
            
            print("-" * 50)
            print(player2, ", make a choice.")
            choice2 = getPlayerChoice()
            print(player2, ", YOUR CHOICE IS -", choice2)
            
            print("*" * 50)
            play(player1, choice1, player2, choice2)
            print("*" * 50)
        else: 
            print("Your input is invalid. Try again.")
            

if __name__ == "__main__":
    main()