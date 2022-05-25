'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 2 - Battleship - User Interface
Description: User Application to play Battleship against a single ship
Date: 02/28/2022
'''

#Import battleshipModule
import battleshipModule

#Initialization
#User input for initializing grid
while True:

	gridSize = input("Enter side length of grid here (4-10): ")
	shipSize = input("Enter length of ship here (2-4): ")

	#Check if input is numerical
	if (gridSize.isnumeric() == False) or (shipSize.isnumeric() == False) or (int(gridSize) <= 0) or (int(shipSize) <= 0):
		print("Enter whole number values only!")
		continue
	else:
		gridSize = int(gridSize)
		shipSize = int(shipSize)

	#Check if dimensions are within given ranges

	if (gridSize in range(4, 11)) and (shipSize in range(2, 5)) and (shipSize <= 3 * gridSize /5):
		break

	else:
		print("Invalid Input. Check dimensions.")

#Define global variables
battleshipModule.globalvars(gridSize, shipSize)

#Create board
battleshipModule.boardgen()

#Create hidden board
battleshipModule.hiddenboardgen()

#Generate and print grid
battleshipModule.printgrid()

#Place ships
battleshipModule.shiploc()

#Game Phase
battleshipModule.play()

#Exit
print("\nThank you for playing Battleship!")
print("Program designed by Amiteash Paul.")
print('''Based on the popular board game "Battleship" by Milton Bradley and Hasbro.''')
