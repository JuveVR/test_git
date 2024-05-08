# The program has a string `sentences`.
#
# The string consists of sentences.
#
# A 'sentence' is a set of characters delimited by periods(. or ...) or the beginning of a line and a period.
#
# Return list with number of words in each sentence.
#
# A 'word' is a set of characters between two spaces or the beginning of a line and a space.
#
# DO NOT use regular expressions.





# Option 1
sentences = "Hello all all all. Here's pretty cold and hot... Choose yourself. Choose yourself."

# Split into sentences.
sentences_list = []
iter_sentence = ''
for symbol in sentences:
    if symbol == '.':
        if iter_sentence.strip():
            sentences_list.append(iter_sentence.strip())
        iter_sentence = ''
    else:
        iter_sentence += symbol

# Split into words
words = []
for sentence in sentences_list:
    word_count = len(sentence.split())
    words.append(word_count)

print(words)

# Option 2

sep = ['.', '...']
sentences_list = []
sentence_str = ""
sep = ['.', '...']

for i in sentences:
    if i in sep:
        sentences = sentences.replace(i, ",")
    sentences_list = sentences.split(',')
    sentences_list.pop()

words_list = []

# Count words in each sentence
for sentence in sentences_list:
    words = sentence.split()
    word_count = len(words)
    if word_count > 0:
        words_list.append(word_count)

print(words_list)