# Write function that takes several lists and returns list of tuples.
#
# Each tuple should be composed from elements of lists of the same index.
#
# Function also should have parameters with default values:
#
# full=False - by default "glue" lists by shortest, otherwise by longest
#
# default=None - if full=True, instead of missing elements add value from parameter default

from typing import List, Tuple, Any


def custom_zip(*sequences, full=False, default=None) -> List[Tuple[Any, ...]]:
    if full:
        max_length = max(len(item) for item in sequences)
        result = []
        for i in range(max_length):
            tuple_elements = tuple(item[i] if i < len(item) else default for item in sequences)
            result.append(tuple_elements)
        return result
    else:
        min_length = min(len(item) for item in sequences)
        return [tuple(item[i] for item in sequences) for i in range(min_length)]


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

# Example 1
print(custom_zip(seq1, seq2))
# Output: [(1, 9), (2, 8), (3, 7)]

# Example 2
print(custom_zip(seq1, seq2, full=True, default="Q"))
# Output: [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

# Example 3
print(custom_zip(seq1, seq2, default="W"))
# Output: [(1, 9), (2, 8), (3, 7)]
