# The user enters a string. Print True if the string is a palindrome, otherwise False.
#
# A palindrome is a string that reads the same way from the left and from the right.
#
# If there are leading or trailing spaces in the line, they should not be taken into account.
#
# The check must be case-insensitive.
#
# Solve at least in TWO ways.

#Option 1
palindrome_check = input("Hello! Enter a palindrome: ")
clear = palindrome_check.strip().lower()               # remove leading/trailing spaces, lower case for case-insensitive comparison
clear_reversed = clear[::-1]

print(clear == clear_reversed)


#Option 2
clear_nml = ""
clear_rev = ""
for i in range(len(clear)):
    clear_nml += clear[i]
    clear_rev += clear[-i-1]

print(clear_nml == clear_rev)

#Option 3
clear = palindrome_check.strip().casefold()
clear_rev = ""
for i in clear:
    clear_rev = i + clear_rev

print(clear == clear_rev)


#Option 4
rev_ind = -1
toggle = 0
for i in clear:
    if i != clear[rev_ind]:
        toggle = 1
        break
    toggle = toggle - 1
if toggle == 1:
    print("True")
else:
    print("False")
