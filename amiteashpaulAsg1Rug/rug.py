'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 1 - Rug Application
Description: Program to create a patterned rug design using nested loops 
Date: 14/02/2022
'''

#Row
for row in range(1):
    for col in range(21):
        print("#", end="")
    print()

#Checkerboard
for row in range(2):
    for sp in range(2):
        print(" ", end="")
    
    for check in range(4):
        for col in range(3):
            print("#", end="")
            print("", end="")
        print("  ", end="")
    print()

#Row
for row in range(1):
    for col in range(21):
        print("#", end="")
    print()
print()

#Diamond between 2 squares
for row in range(4):
    
    #Printing first part of first square
    if row >= 2:
        for col in range(3):
            print("#", end="")
            print(" ", end="")
        for sp in range(4-row):
            print(" ", end="")

    #Or print spaces
    else:
        for sp in range(10-row):
            print(" ", end="")
    
    #Printing the first half of diamond (upward-pointing triangle)
    for col in range(row + 1):
        print("#", end="")
        print(" ", end="")

    #Printing first part of second square
    if row >= 2:
        for sp in range(4-row):
            print(" ", end="")
        for col in range(3):
            print("#", end="")
            print(" ", end="")
    print()

for row in range(3, 0, -1):
    #Printing second part of first square
    if row >= 3:
        for col in range(3):
            print("#", end="")
            print(" ", end="")
        for sp in range(5-row):
            print(" ", end="")

    #Or print spaces
    else:
        for sp in range(10-row+1):
            print(" ", end="")
    
    #Printing the second half of diamond (downward-pointing triangle)
    for col in range(row, 0, -1):
        print("#", end="")
        print(" ", end="")
    
    #Printing second part of second square
    if row >= 3:
        for sp in range(5-row):
            print(" ", end="")
        for col in range(3):
            print("#", end="")
            print(" ", end="")    
    print()
print()

#Row
for row in range(1):
    for col in range(21):
        print("#", end="")
    print()

#Checkerboard
for row in range(2):
    for sp in range(2):
        print(" ", end="")
    
    for check in range(4):
        for col in range(3):
            print("#", end="")
            print("", end="")
        print("  ", end="")
    print()

#Row
for row in range(1):
    for col in range(21):
        print("#", end="")
    print()
    