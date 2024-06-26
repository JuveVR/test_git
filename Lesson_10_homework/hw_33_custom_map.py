# Write function, that takes function and several lists (number of lists should be the number of parameters for function).
#
# Function should return list of results of applying a function to corresponding elements of lists.
#
# If passed lists have different length, result should be formed by shortest one.

def custom_map(function: callable, *lists):
    shortest_list = min(len(lst) for lst in lists)
    return [function(*items) for items in zip(*[lst[:shortest_list] for lst in lists])]


# Example 1
print(custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]]))


# Example 2
print(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0]))


# Example 3
print(custom_map(len, [[], (2, 4), [1, 3, 5, 7]]))


# Example 4
print(custom_map(lambda x, y, z: x + y + z, [1, 2, 3, 7], [3, 5, 0, 5, 9], [1, 2, 3]))
