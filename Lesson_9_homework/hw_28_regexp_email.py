# Write function using regular expressions that takes email as string, and returns True if the string is a valid address, otherwise False.
#
# Valid address is considered:
#
# - '@' comes before '.'
#
# - the string does not start with '@' and does not end with '.'
#
# - symbols except '@' and '.' should be letters and decimal digits
#
# - containing only one '@' and only one '.'
#
# email = "aaa@bbb.ccc"  # True

import re


def email_validation(my_email: str) -> bool:
    pattern = r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$'
    match = re.match(pattern, my_email)
    return bool(match)


# Test data
my_email = "aaa@bbb.ccc"
print(email_validation(my_email))  # True

my_email = "aaa@@bbb..ccc"
print(email_validation(my_email))  # False

my_email = "@aaabbbccccom."
print(email_validation(my_email))  # False

my_email = "aaa.bbb@ccccom"
print(email_validation(my_email))  # False

my_email = "aaa@bbbccc"
print(email_validation(my_email))  # False

my_email = "aaa@.ccc"
print(email_validation(my_email))  # False

my_email = "aaa@bbb."
print(email_validation(my_email))  # False

my_email = "@bbb.ccc"
print(email_validation(my_email))  # False

my_email = "aaa@bbb.ccc."
print(email_validation(my_email))  # False

my_email = "aaa@bbb@ccc.com"
print(email_validation(my_email))  # False