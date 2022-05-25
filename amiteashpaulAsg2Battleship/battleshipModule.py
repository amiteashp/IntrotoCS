'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 2 - Battleship - Module
Description: Module to play Battleship
Date: 02/28/2022
'''


#Import important modules
import random
import os


#Global constants
HIT = " X "
MISS = " # "
board = []
hiddenboard = []
prevguess = []


#Global Variables
def globalvars(gridSize, shipSize):
    global grid_width
    grid_width = gridSize
    global ship_length
    ship_length = shipSize


#Create Board
def boardgen():
    #Add rows
    for row in range(grid_width):
        rowList = []

        #Add columns
        for col in range(grid_width):
            rowList.append(" ")
        
        board.append(rowList)


#Create Hidden Board
def hiddenboardgen():
    #Add rows
    for row in range(grid_width):
        rowList = []

        #Add columns
        for col in range(grid_width):
            rowList.append("0")
        
        hiddenboard.append(rowList)


#Print Grid
def printgrid():

    #Print column names
    print("   ", end = "")
    for col in range(grid_width):
        print("  ", end = "")
        print(chr(65 + col), end = "")
        print(" ", end = "")
    print()

    #Print rows
    for row in range(grid_width):
        print("   ", end = "")

        #Print lines
        for col in range(grid_width):
            print("+---", end = "")
        print("+")

        #Print row numbers
        print((row + 1), end = "")

        #Count digits
        digit_count = 0
        for digit in str(row + 1):
            digit_count +=1
        
        #Adjust spaces on digit number
        for sp in range(3 - digit_count):
            print(" ", end = "")

        #Print cell contents
        for col in range(grid_width):
            print("|",  end = "")
            print(" ", end = "")
            print(board[row][col], end="")
            print(" ", end = "")
        print("|")

    #Last Row
    print("  ", end = " ")
    for col in range(grid_width):
        print("+---", end = "")
    print("+")


#Place ship at beginning of game
def shiploc():
    #Choose orientation randomly
    orientation = random.choice(["hor", "ver"])

    #Trigger corresponding function
    if (orientation == "hor"):
        shiploc_horizontal()
    elif (orientation == "ver"):
        shiploc_vertical()


#Place ship horizontally
def shiploc_horizontal():
    startrow = random.randint(0, (grid_width - 1))
    startcol = random.randint(0, (grid_width - ship_length))

    for unit in range(ship_length):
        hiddenboard[startrow][startcol + unit] = "1"

#Place ship horizontally
def shiploc_vertical():
    startrow = random.randint(0, (grid_width - ship_length))
    startcol = random.randint(0, (grid_width - 1))

    for unit in range(ship_length):
        hiddenboard[startrow + unit][startcol] = "1"

def play():
    
    #Declare important variables
    win = False
    turn_count = 0
    correct = 0

    #Welcome and Instructions (step-by-step)
    print()
    input("Greetings Commander! (Press Enter to continue)")
    input("An enemy ship has invaded our waters. You must sink it with haste.")
    input("Air Surveillance reports that the ship is %i units long and is oriented either vertically or horizontally on the grid." % ship_length)
    input("Enter the target coordinates to shoot a square on the grid.")
    input("The enemy ship will sink and you will win when it reaches 0 health.")
    print("Our nation's safety depends on you. Good Luck Commander!")

    while not win:
        
        #Print turn count and ship healthpoints
        print()
        print("Shots fired =", turn_count, "/", (grid_width ** 2))
        print("Ship Health at " + str((ship_length - correct) / ship_length * 100) + "%")

        #Ask user for guess
        guess = input("Enter coordinates of target here (e.g. A1): ")

        #Check if guess is
        if type(guess) != str:
            continue

        #Check if guess has been repeated
        if guess in prevguess:
            print("Warning: Repeated shelling of same location not recommended. Please choose new coordinates.")
            continue

        #Convert guess into list of coordinates
        coordinate = ["A", "0"]
        for letter in guess:
            if (letter.isalpha() == True):
                coordinate.pop(0)
                coordinate.insert(0, letter)
            
            if (letter.isnumeric() == True):
                coordinate.pop(1)
                ycoord = guess[1:]
                coordinate.insert(1, ycoord)

        #Check if guess has proper formatting (capital letter followed by number)
        if not(65 <= ord(coordinate[0]) <= 90) or (coordinate[1].isnumeric() == False):
            print("Warning: Invalid Input. Coordinates must be uppercase letter followed by number (e.g. A1).")
            continue

        #Adjust coordinates to list indices
        row = int(coordinate[1]) - 1
        col = (ord(coordinate[0]) - 65)

        #Check if guess is out of board
        if not(0 <= row <= (grid_width - 1)) or not(0 <= col <= (grid_width - 1)):
            print("Warning: Entered coordinates are out of firing range. Please choose new coordinates.")
            continue

        #Add guess into list of previous guesses
        prevguess.append(guess)

        #Update turn counter
        turn_count += 1

        #Match coordinates with hidden board, mark on visible and hidden boards
        if (hiddenboard[row][col] == "1"):
            board[row][col] = "X"
            hiddenboard[row][col] = "0"
            correct += 1
        else:
            board[row][col] = "#"

        #Check if win condition fulfilled
        shipcount = 0
        for rowList in hiddenboard:
            count = rowList.count("1")
            shipcount += count
        
        if shipcount == 0:
            win = True

        #Clear screen
        os.system("clear")

        #Print grid
        printgrid()
    
    #Win message
    print("\nYou won!")
    print("You took ", turn_count, " tries to win the game, out of a maximum of ", (grid_width ** 2), ".", sep = "")
