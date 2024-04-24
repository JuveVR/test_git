#Output the maximum number of 3 user-entered numbers.

#DO NOT use built-in functions. Use only flow control instructions (ifs, loops)

a = int(input("Hello! Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

user_numbers = [a, b, c]
highest = user_numbers[0]

for number in user_numbers:
    if number > highest:
        highest = number

print("The highest number is : " + str(highest))


