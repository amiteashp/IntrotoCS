'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 2 - Word Search - Functions
Description: Module containing functions for Word Search
Date: 04/25/2022
'''

#Import Modules
from copy import *
from random import *
import os
import sys
from wordsearchClasses import *

#Main Menu
def menu():
    start_game = False
    while not start_game:
        print("Welcome to the Word Search Game.")
        print("\nMAIN MENU")
        print("1. Start Playing")
        print("2. Help")
        print("3. Quit")
        option = int(input("Enter option here: "))

        #Choosing Menu Options
        if option == 1:
            start_game = True
        elif option == 2:
            print("This is a Word Search game where words on a grid will have to be found by the players.\n")
            print("Game Setup Instructions")
            print("Input the preferred board and number of players when prompted. The game needs at least 1 player.\n")
            print("Boards are sorted by their difficulty.\n")
            print("Easy Difficulty: Boards 1~3 (6x6)")
            print("Medium Difficulty: Boards 4~6 (8x8)")
            print("Hard Difficulty: Boards 7~9 (10x10)")
            print("Super Hard Difficulty: Boards 10~12 (15x15)\n")
            print("Playing Instructions")
            print("Each player will take a turn in guessing a word from the grid.")
            print("If the guess is correct, a point will be added and the word capitalized on the board.")
            print("If a guess is wrong, no points are added and the turn goes to the next player.")
            print("Special Rule: If there are more than 25 unsuccessful guesses between any two successful runs, the game will automaticallyend to conserve CPU resources.")
        elif option == 3:
            sys.exit("Thank you for playing Word Search.")


#Setting Up the Game
def setup():
    
    os.system("clear")

    valid_difficulty = False
    
    #Preferred Difficulty
    print("Choose Difficulty.")
    print()
    print("1. Easy Difficulty (6x6 Board)")
    print("2. Medium Difficulty (8x8 Board)")
    print("3. Hard Difficulty (10x10 Board)")
    print("4. Super Hard Difficulty (15x15 Board)")
    print()
    while valid_difficulty == False:
        prefdifficulty = input("Which level of difficulty do you want to play at? ")

        if prefdifficulty.isnumeric() == True:
            if (int(prefdifficulty) >= 1 and int(prefdifficulty) < 5):
                valid_difficulty = True
                prefdifficulty = int(prefdifficulty)
            else:
               print("Invalid entry. Please input a positive integer that is between 1 and 4.") 
        else:
            print("Invalid entry. Please input a positive integer that is between 1 and 4.")

    #Choose Random Board based on Difficulty
    if prefdifficulty == 1:
        prefboard = randint(1,3)
    elif prefdifficulty == 2:
        prefboard = randint(4,6)
    elif prefdifficulty == 3:
        prefboard = randint(7,9)
    elif prefdifficulty == 4:
        prefboard = randint(10,12)

    #Create board
    global board
    board = Board("csv_files/board_%d.csv" % prefboard)

    #Create shownboard
    global shownboard
    shownboard = VisBoard("csv_files/board_%d.csv" % prefboard)

    #Players List
    global PLAYERS
    PLAYERS = []
    valid_players = False

    #Input number of players
    while valid_players == False:
        playernum = input("How many players? ")

        if playernum.isnumeric() == True and int(playernum) > 0:
            valid_players = True
            playernum = int(playernum)
        else:
            print("Invalid entry. Please input an integer that is greater than 0.")

    for player in range(1, (playernum + 1)):
        playername = ("Player %d" % player)
        PLAYERS.append(playername)

    #Words List
    global WORDS
    WORDS = board.words

    #Dimensions List
    global DIM
    DIM = board.dimensions

    #Scores Dictionary
    global scores
    scores= {}
    for player in PLAYERS:
        scores.update({player:0})

    #Guesses Dictionary
    global guesses
    guesses = {}
    for player in PLAYERS:
        guesses.update({player:[]})


#Playing the Game
def play():
    turn = randint(0, (len(PLAYERS) - 1))
    unsuccessful_turns = 0

    win = False
    
    #Remove the dimensions and words list from board (for consistent dimensions)
    board.pop(0)

    #Loop runs until someone wins, or until total number of turns between 2 successful runs reaches 25 (force quit)
    while (not win) and (unsuccessful_turns <= 25): 
        printboard()
        current_player = str(PLAYERS[turn])

        #Breaks loop when words are exhausted
        if WORDS == []:
            win = True
            break

        #Score Display
        print(current_player + "'s turn. \n")
        for player in PLAYERS:
            print(player, "Score:", scores[player], guesses[player])
        
        #User input for word
        valid_guess = False
        while not valid_guess:
            guess = str(input("\nEnter word here: "))

            #Verify guess
            if (guess.islower()) and (len(guess) >= 3):
                valid_guess = True
            else:
                print("Answer must be in lowercase and have more than 3 letters.")
        
        if guess in WORDS:
            input("Correct!") #Allows flow control
            WORDS.remove(guess) #Removes word from list of possible guesses
            scores[current_player] += 1
            guesses[current_player].append(guess)
            turn = (turn + 1) % len(PLAYERS)
            unsuccessful_turns = 0 #Resets unsuccessful turns counter
            updateboard(guess)

        else:
            input("Wrong Guess! Turn goes to next player.") #Allows flow control
            turn = (turn + 1) % len(PLAYERS)
            unsuccessful_turns += 1 #Increments unsuccessful turns counter

    #Print Force Quit declaration (if applicable), Final Scores and Check Winner
    if unsuccessful_turns > 25:
        print("Game force quit due to more than 25 consecutive incorrect guesses.\n")
    for player in PLAYERS:
            print(player, "Final Score:", scores[player], guesses[player])
    print(findwinner())
    print("Thank you for playing Word Search.")


#Printing the board  
def printboard():
    #Clear Screen
    os.system("clear")
    shownboard.print()


#Update board
def updateboard(word):
    #First letter
    direction_confirmed = None
    for row in range(board.length):
        for col in range(board.width):
           #Find first letter
            if word[0] == board[row][col].lower(): 
                #Each if-elif statement checks whether second letter of word and board matches
                if direction_confirmed == None and col > 0:
                    if board[row][col-1].lower() == word[1]:
                        #Search towards left
                        direction_confirmed = board.search(word, "left", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row > 0 and col > 0:
                    if board[row-1][col-1].lower() == word[1]:
                        #Search towards upper-left
                        direction_confirmed = board.search(word, "upleft", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row > 0:
                    if board[row-1][col].lower() == word[1]:
                        #Search upwards
                        direction_confirmed = board.search(word, "up", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row > 0 and col < board.width - 2:
                    if board[row-1][col+1].lower() == word[1]:
                        #Search towards upper-right
                        direction_confirmed = board.search(word, "upright", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and col < board.width - 2:
                    if board[row][col+1].lower() == word[1]:
                        #Search towards right
                        direction_confirmed = board.search(word, "right", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row < board.length - 2 and col < board.width - 2:
                    if board[row+1][col+1].lower() == word[1]:
                        #Search towards lower-right
                        direction_confirmed = board.search(word, "downright", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row < board.length - 2:
                    if board[row+1][col].lower() == word[1]:
                        #Search downwards
                        direction_confirmed = board.search(word, "down", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
                    
                if direction_confirmed == None and row < board.length - 2 and col > 0:
                    if board[row+1][col-1].lower() == word[1]:
                        #Search towards lower-left
                        direction_confirmed = board.search(word, "downleft", row, col)
                        row_confirmed = row
                        col_confirmed = col
                    if direction_confirmed != None:
                        break
    
    #Update board
    board.update(word, direction_confirmed, row_confirmed, col_confirmed)

def findwinner():
    draw = True

    #Find max. score and assume as winner
    highscore = max(scores.values())
    winner = list(scores.keys())[list(scores.values()).index(highscore)]

    #Check for equals (draw)
    for player in scores:
        if scores[player] != highscore:
            draw = False
            break
    
    #Check if draw or win and how many players
    if draw == True and len(scores) > 1:
        windeclaration = "It's a draw!"
    else:
        windeclaration = "The winner is %s" % winner
    
    #Statement to be printed
    return windeclaration
    