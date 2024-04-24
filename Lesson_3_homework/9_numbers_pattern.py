# Given the entered number n, derive a pattern from numbers
#
# n could be in range 1 <= n <= 9.
#
# There are NO spaces at the end of lines.
#
# DO NOT use methods of string type.
#
# You could solve this task for n > 9, but it would be task with * :)


n = int(input("Enter n: "))
if 1 <= n <= 9:
    pattern = (n-1)*" " + n*"123456789"
    pyramid = [pattern[i:i+n] for i in range(n)]
    pyramid = [d+d[-2::-1] for d in pyramid]
    for brick in pyramid:
        print(brick * 1)
else:
    print("Please enter n in range 1 <= n <= 9")
