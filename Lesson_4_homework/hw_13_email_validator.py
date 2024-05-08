# There's a string with email address.
#
# Print True if the string is a valid address, otherwise False.
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
# Specify strings for testing your code in comments.
#
# DO NOT use regular expressions.

email = "iamem22ail@i.ua"
# Check if '@' and '.' exist in the string
if email.find("@") < 0 or email.find(".") < 0:
    print(False)
else:
    # Check that the string does not start with '@' and does not end with '.'
    if email.endswith(".") or email.startswith("@"):
        print(False)
    else:
        dots = 0
        ats = 0
        # Iterate through each symbol
        for i in email:
            # Check if symbols except '@' and '.' are letters and decimal digits
            if not (i.isalnum() or i in ['@', '.']):
                print(False)
                break
            # Count '@' and '.'
            if i == '@':
                ats += 1
            elif i == '.':
                dots += 1

        # Check that '@' and '.' are single in the string
        if dots != 1 or ats != 1:
            print(False)
        else:
            # Check that '@' comes before '.'
            if email.find("@") > email.find("."):
                print(False)
            else:
                print(True)

""" Values for testing validation :
iamem22ail@i.ua
iamemaili.ua
iamemail@iua
iamem23ailiua
iamemailiua.@
@iamemailiu.a
.iamemailiu@a
iamemailiu@a.
@iamemailiu@.
..iamemailiu@@a
.iamemailiu@@a
..iamemailiu@a
iamemai#l@i.ua
iamem0,3ai@i.ua
iamem22ail.i@ua
"""




