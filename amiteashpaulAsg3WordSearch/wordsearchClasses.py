'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 2 - Word Search - Classes
Description: Module containing classes for Word Search
Date: 04/25/2022
'''

import csv
from copy import *

board = []

#Board
class Board:
    def __init__(self, file):
        self.boardgen(file)
        self.dimensions = []
        self.words = []
        self.dimensions = self.getdimensions()
        self.words = self.getwords()
        self.length = int(self.dimensions[0])
        self.width = int(self.dimensions[1])

    #Required for Board[index]
    def __getitem__(self, index):
        return board[index]

    #Required for Board.pop(index)
    def pop(self, index):
        board.pop(index)

    #Generate board from file
    def boardgen(self, rfile):
        with open(rfile, "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            global board
            board = list(csv_reader)
    
    #Generate words from first row of file
    def getwords(self):
        for row in range(1):
            for col in range(len(board[row])):
                self.words.append(board[row][col])
        #Pop out the dimensions
        self.words.pop(0)
        self.words.pop(0)
        return self.words
    
    #Generate dimensions from first row of file
    def getdimensions(self):
        for row in range(1):
            for col in range(2):
                self.dimensions.append(int(board[row][col]))
        return self.dimensions

    def print(self):
       raise NotImplementedError
    
    #Search words in grid
    def search(self, word, direction, row, col):
        foundword = []
        #Keep searching to left
        if direction == "left":
            for letter in range(len(word)):
                #To prevent IndexError
                if (col - letter < 0):
                    break
                nextletter = board[row][col - letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter) 
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching to upper left diagonal
        elif direction == "upleft":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row - letter < 0) or (col - letter < 0):
                    break
                nextletter = board[row - letter][col - letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching upwards
        elif direction == "up":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row - letter < 0):
                    break
                nextletter = board[row - letter][col].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching to upper right diagonal
        elif direction == "upright":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row - letter < 0) or (col + letter >= self.width):
                    break
                nextletter = board[row - letter][col + letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching to right
        elif direction == "right":
            for letter in range(len(word)):
                #To prevent IndexError
                if (col + letter >= self.width):
                    break
                nextletter = board[row][col + letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter) 
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching to lower right diagonal
        elif direction == "downright":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row + letter >= self.length) or (col + letter >= self.width):
                    break
                nextletter = board[row + letter][col + letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching downwards
        elif direction == "down":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row + letter >= self.length):
                    break
                nextletter = board[row + letter][col].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None
        #Keep searching to lower left diagonal
        elif direction == "downleft":
            for letter in range(len(word)):
                #To prevent IndexError
                if (row + letter >= self.length) or (col - letter < 0):
                    break
                nextletter = board[row + letter][col - letter].lower()
                if word[letter] == nextletter:
                    foundword.append(nextletter)   
            if foundword == list(word):
                return direction
            else:
                return None

    #Update words in grid
    def update(self, word, direction, row, col):
        #Keep searching and capitalizing to left
        if direction == "left":
            for letter in range(len(word)):
                nextletter = board[row][col - letter].lower()
                if word[letter] == nextletter:
                    board[row][col - letter] = nextletter.upper()
        #Keep searching and capitalizing to upper left diagonal
        elif direction == "upleft":
            for letter in range(len(word)):
                nextletter = board[row - letter][col - letter].lower()
                if word[letter] == nextletter:
                    board[row - letter][col - letter] = nextletter.upper()
        #Keep searching and capitalizing upwards
        elif direction == "up":
            for letter in range(len(word)):
                nextletter = board[row - letter][col].lower()
                if word[letter] == nextletter:
                    board[row - letter][col] = nextletter.upper()
        #Keep searching and capitalizing to upper right diagonal
        elif direction == "upright":
            for letter in range(len(word)):
                nextletter = board[row - letter][col + letter].lower()
                if word[letter] == nextletter:
                    board[row - letter][col + letter] = nextletter.upper()
        #Keep searching and capitalizing to right
        elif direction == "right":
            for letter in range(len(word)):
                nextletter = board[row][col + letter].lower()
                if word[letter] == nextletter:
                    board[row][col + letter] = nextletter.upper()

        #Keep searching and capitalizing to lower right diagonal
        elif direction == "downright":
            for letter in range(len(word)):
                nextletter = board[row + letter][col + letter].lower()
                if word[letter] == nextletter:
                    board[row + letter][col + letter] = nextletter.upper()
        #Keep searching and capitalizing downwards
        elif direction == "down":
            for letter in range(len(word)):
                nextletter = board[row + letter][col].lower()
                if word[letter] == nextletter:
                    board[row + letter][col] = nextletter.upper()
        #Keep searching and capitalizing to lower left diagonal
        elif direction == "downleft":
            for letter in range(len(word)):
                nextletter = board[row + letter][col - letter].lower()
                if word[letter] == nextletter:
                    board[row + letter][col - letter] = nextletter.upper()


#Visible Board - Subclass of Board
class VisBoard(Board):
    def __init__(self, file):
        super().__init__(file)
        self.visboard = copy(board)
        self.visboard.pop(0)

    #Print the Visible Board
    def print(self):
        for row in self.visboard:
            for col in range(self.width):
                print("+---", end = "")
            print("+")

            for col in row[0:self.width]:
                print("|", end = " ")
                print(col, end = " ")
            print("|")

        #Last Row
        for col in range(self.width):
            print("+---", end = "")
        print("+")
        