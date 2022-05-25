'''Name: Amiteash Paul    NetId: ap6444
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Assignment 1B - Kilim Moroccan Carpet Generator - User Interface
Description: User Application to create Kilim Rug using patterns from rugModule
Date: 14/02/2022
'''

#Import rugModule
import rugModule

#Welcome and Provide Instructions to User
print("Welcome to the Kilim Carpet Generator\n")
print("To begin, please enter width, height and character to print your pattern when prompted.\n")

#Request User Input on width, height, and printing character
max_width = int(input("Enter width of pattern: "))
max_height = int(input("Enter height of pattern: "))
char = str(input("Enter printing character: "))

#Trigger rugModule.global variables to define global variables max_width and char using user input
rugModule.globalvars(max_width, char)


#Height and width were used to approximately scale a small pre-defined pattern (size=10*10) to user-defined size
#Pattern composed of rectangle, followed by newline, square, diamond, square, newline and another rectangle (symmetrical pattern)
#Pre-defined pattern starts here

#Checking for remainder >5 to print appropriate height rectangle in scaled figure
if (max_height % 10) > 5:
    rugModule.rectangle((max_height // 10 + 1), max_width)
else:
    rugModule.rectangle((max_height // 10), max_width)

#Print newline
print()

#Print checkered square
rugModule.checksquare((max_height // 5))

#Print diamond
rugModule.diamond((max_height // 5))

#Print square
rugModule.checksquare((max_height // 5))

#Print newline
print()

#Checking for remainder >5 again and printing rectangle
if (max_height % 10) > 5:
    rugModule.rectangle((max_height // 10 + 1), max_width)
else:
    rugModule.rectangle((max_height // 10), max_width)
