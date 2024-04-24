# User enters height and width of rectangle (integer numbers), and any symbol.
#
# Output a rectangle made up of the entered character of a given size.
#
# There are NO spaces at the end of lines.

#Option 1"

rec_height = int(input("Hello! Enter height of rectangular: "))
rec_width = int(input("Enter width of rectangular: "))
brick = input("Enter symbol to build rectangular with: ")

print((brick * rec_width + '\n') * rec_height, end = '')

print("------Option--Divider-------")

#Option 2
row = (brick * rec_width)
for i in range(rec_height):
    print(row, end='\n' )

print("------Option--Divider-------")

#Option 3
for i in range(rec_height):
    for j in range(rec_width):
        print(brick, end='')
    print()

