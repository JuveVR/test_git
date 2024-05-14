# Write function that takes list of numbers, and returns the second largest number.
#
# If there's no second largest number in the list (empty list is passed, or list contains only the same number), function should return None.
#
# You should NOT use max/min built-n functions, sort/sorted.
#
# Write implementation that performs only one pass through the list (complexity O(n)).

def second_biggest(lst):
    if len(lst) < 2 or len(set(lst)) == 1:
        return None

    biggest = second_biggest = float('-inf')

    for num in lst:
        if num > biggest:
            second_biggest = biggest
            biggest = num
        elif num > second_biggest and num != biggest:
            second_biggest = num

    if second_biggest == float('-inf'):
        return None
    else:
        return second_biggest


# Example usage:
my_list = [4, 4, 4, 4, 5]
print(second_biggest(my_list))
