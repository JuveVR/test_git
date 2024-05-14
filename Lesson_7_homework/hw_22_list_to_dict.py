# Write function lst2dict(lst) that takes list and returns dictionary.
#
# Dictionary should contain key-value pairs, where
#
# - key is list element on even position (0, 2, 4, ...)
#
# - value corresponding to this key is the list element, following after key
#
# If list has odd length, last item shouldn't be taken into account.

# option 1
my_list = [1, 2, 3, 4, 5, 7, 8]


def lst2dict(lst):
    new_dict = {}
    iter_lst = lst[:]
    if len(iter_lst) % 2 != 0:
        iter_lst.pop()
    for i in range(0, len(iter_lst), 2):
        new_dict[iter_lst[i]] = iter_lst[i + 1]
    return new_dict


print(lst2dict(my_list))


# option 2
my_list_2 = [1, 2, 3, 4, 5, 7, 8]


def lst2dict2(lst):
    length = len(lst)
    if len(lst) % 2 != 0:
        length -= 1
    new_dict_2 = {lst[i]: lst[i + 1] for i in range(0, length, 2)}
    return new_dict_2


print(lst2dict2(my_list_2))


