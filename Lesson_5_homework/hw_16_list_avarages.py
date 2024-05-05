# There is a list of at least two float elements.
#
# Create a new list. It should contain elements of initial list, and between them should be added average of that elements.

# option 1
lst = [1.3, 2, 3, 4, 5]
lst_with_averages = []
i = 0

for digit in lst[:-1]:
    lst_with_averages.append(digit)
    average_digits = (digit + lst[i + 1]) / 2
    lst_with_averages.append(average_digits)
    i += 1

lst_with_averages.append(lst[-1])
print(lst_with_averages)

# option 2
lst = [1.3, 2, 3, 4, 5]
lst_with_averages = []
lst_with_originals = []

for digit in range(len(lst) - 1):

    average_digits = (lst[digit] + lst[digit + 1]) / 2
    lst_with_averages.append(average_digits)

new_list = [num for pair in zip(lst[:], lst_with_averages) for num in pair]

new_list.append(lst[-1])

print(new_list)

