# Write function that returns random string of specified length.
#
# String should consists only digits, small and capital Latin letters.
#
# Restrictions:
#
# - Don't use module string
#
# - Don't create manually list ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9] or string with all of these symbols.

import random


def generate_random_string(length: int) -> str:
    my_string = []
    for symbol in range(length):
        symbol_type = random.choice(['digit', 'upper', 'lower'])
        if symbol_type == 'digit':
            my_string.append(chr(random.randint(48, 57)))
        elif symbol_type == 'upper':
            my_string.append(chr(random.randint(65, 90)))
        else:
            my_string.append(chr(random.randint(97, 122)))
    return ''.join(my_string)

# Example usage:
length = 10
random_string = generate_random_string(length)
print(random_string)