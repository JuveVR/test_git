# There's a list that could contain numbers and nested lists, that could contain numbers and nested lists, that could contain...
#
# Write function that takes list described above, and returns flat list consisting of all list elements.
#
# P.S You can't convert list to string, remove square brackets and split it back by whitespaces:)

# option 1
def linearize_list(any_lst):
    unpacked_list = []

    for element in any_lst:
        if isinstance(element, list):
            unpacked_list.extend(linearize_list(element))
        else:
            unpacked_list.append(element)

    return unpacked_list


# option 2
def linearize_list_gen(any_lst):
    for item in any_lst:
        if isinstance(item, list):
            yield from linearize_list_gen(item)
        else:
            yield item


lst = [1, 2, [3, 4, [5,[5.1, 5.2, 5.3], 6], 7], 8, [9, [10]], 11]
print(linearize_list(lst))
print(list(linearize_list_gen(lst)))




