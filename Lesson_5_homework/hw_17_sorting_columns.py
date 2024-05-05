# There is a two-dimensional list of Latin letters. Sort the letters by columns.
#
# We assume that the list is rectangular.
#
# DO NOT use built-in functions map and zip

crazy_letters = [
    ['a', 'c', 'e'],
    ['f', 'b', 'a'],
    ['a', 'n', 'k'],
    ['e', 'l', 'i']
]

iter_columns = len(crazy_letters[0])
extracted_letters = [[line[i] for line in crazy_letters] for i in range(iter_columns)]

for vertical in extracted_letters:
    vertical.sort()

packed_letters = [[line[i] for line in extracted_letters] for i in range(len(extracted_letters[0]))]

for line in packed_letters:
    print(line)