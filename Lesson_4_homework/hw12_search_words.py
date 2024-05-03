# The program has a line `string`.
#
# Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.

 # option 1
o_string = "This tool is cool. But that owl oowl oowl owl owl is awful. MAGIC TOOLS Ltd."
words_list = o_string.split()
o_words = []
for word in words_list:
    if word.lower().count('o') == 2:
        o_words.append(word.lower().title())
print("Return:", end=" ")
print(*o_words)

# option 2 (almost the same as 1)
o_words = []
for word in words_list:
    if word.lower().count('o') == 2:
        o_words.append(word.lower())

print("Result:", " ".join(word.title() for word in o_words))
