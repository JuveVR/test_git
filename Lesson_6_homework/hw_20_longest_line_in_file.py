# There is a text file. Print the longest line in file.
#
# If there's several lines of maximum length, print the last one.
#
# Do not use built-in max, sorted functions and file read/readlines method.

file_path = "Reve_ta_stogne.txt"
with open(file_path, "r") as my_file:

    longest_line = 0
    last_longest = ""

    for line in my_file:
        line_length = len(line.rstrip('\n'))
        if line_length >= longest_line:
            longest_line = line_length
            last_longest = line

    print(last_longest.rstrip('\n'))

