# There is a list consisting of integer numbers.
#
# Create three lists:
#
# - to the first list add numbers that are only divisible by 3, but not divisible by 5
#
# - to the second list add numbers that are divisible by 5, but not divisible by 3
#
# - to the third list add numbers that are divisible by both 3 and 5

input_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 25, 18]

lst1 = []
lst2 = []
lst3 = []

for num in input_lst:
    if num % 3 == 0 and num % 5 != 0:
        lst1.append(num)
    if num % 5 == 0 and num % 3 != 0:
        lst2.append(num)
    if num % 3 == 0 and num % 5 == 0:
        lst3.append(num)

print("Numbers divisible by 3 but not 5:", lst1)
print("Numbers divisible by 5 but not 3:", lst2)
print("Numbers divisible by both 3 and 5:", lst3)
