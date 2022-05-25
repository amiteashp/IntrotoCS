'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 1B - Kilim Moroccan Carpet Generator - Module
Description: Module to create Kilim Rug using nested loops
Date: 14/02/2022
'''

#Global Variables
def globalvars(max_width, printchar):
    global line_width
    line_width = max_width
    global char
    char = printchar

#Row
def row():
    for row in range(1):
        for col in range(int(line_width)):
            print(char, end="")
        print()

#Rectangle
def rectangle(rect_height, rect_width):
    doublinitspace = line_width - (2 * rect_width)
    for row in range(int(rect_height)):
        for sp in range(int((doublinitspace / 2) + (doublinitspace % 2))):
            print(" ", end="")
    for row in range(int(rect_height)):
        for col in range(int(rect_width)):
            print(char, end="")
        print()

#Checkerboard Rectangle
def checkerboard(checkheight, checklength, checkrepeat):
    for row in range(int(checkheight)):
        for sp in range(3):
            print(" ", end="")
    
        for check in range(int(checkrepeat)):
            for col in range(int(checklength)):
                print(char, end="")
            print(" ", end="")
        print()

#Checkered Square
def checksquare(sq_width):
    doublinitspace = line_width - (2 * sq_width)
    for row in range(int(sq_width)):
        for sp in range(int((doublinitspace / 2) + (doublinitspace % 2))):
            print(" ", end="")
    
        for col in range(int(sq_width)):
            print(char, end="")
            print(" ", end="")
        print()

#Upward-Facing Triangle
def uptriangle(tr_height):
    for row in range(int(tr_height)):
        for sp in range(int((line_width / 2) + (line_width % 2) - 1 - row)):
            print(" ", end="")
    
        for col in range(row + 1):
            print(char, end="")
            print(" ", end="")
        print()

#Downward-Facing Triangle
def downtriangle(tr_height):
    for row in range(int(tr_height), 0, -1):
        for sp in range(int((line_width / 2) + (line_width % 2) - row)):
            print(" ", end="")
    
        for col in range(row, 0, -1):
            print(char, end="")
            print(" ", end="")
        print()

#Diamond (comprised of upward-facing triangle and downward-facing triangle 1 row shorter)
def diamond(width):
    uptriangle(width)
    downtriangle(width-1)
