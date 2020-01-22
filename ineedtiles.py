# This program calculates how many tiles you will need when tilling a wall or floor (in m2)


length = float(input("Enter Room Length: ")) #allows user inputs
width = float(input("Enter Room Width: ")) #allows user inputs

# length = 3.5
# width = 2.3

area =  length * width

needed = area * 1.05 # Required + 5%

print("You need", needed, "tiles in metres squared.") # String 