# The program has a line `string`.
#
# Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.

 # option 1
o_string = "This tool is cool. But that owl owl owl owl owl is awful. MAGIC TOOLS Ltd."
words_list = o_string.split()
o_words = []
for word in words_list:
    lower_word = word.lower()
    if lower_word.find('o') >= 0:
        o_words.append(word)
print("Return:", end=" ")
print(*o_words)



# option 2 (almost the same ad 1)
o_words = []
for word in words_list:
    if 'O' in word.upper():
        o_words.append(word)
print("Result:", " ".join(o_words))