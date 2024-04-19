#Request two integer numbers from user.
#Output on one line expression with sum of numbers, and on another line - expression with product of numbers:


#option_1
a = input("Enter A: ")
b = input("Enter B: ")

print(a + " + " + b + " = " + str(int(a) + int(b)))
print(a + " * " + b + " = " + str(int(a) * int(b)))

#option_2
a = int(input("Enter A: "))
b = int(input("Enter B: "))
sum = str(a + b)
multiply = str(a * b)

print(str(a) + " + " + str(b) + " = " + sum)
print(str(a) + " * " + str(b) + " = " + multiply)