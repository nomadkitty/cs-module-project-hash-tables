import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split(" ")
# wordsRange = re.findall('([A-Z][.?!]+)', words)
# print(wordsRange)


def build_index(words):
    index = {}
    star_words = []
    # loop through the split word list
    # add the next word to the word list of that index
    for idx in range(len(words) - 1):
        # check if the word is already in index
        if words[idx] in index:
            index[words[idx]].append(words[idx+1])
        # if not, add the key and append the next word
        else:
            index[words[idx]] = []
            index[words[idx]].append(words[idx+1])

    return index


# TODO: construct 5 random sentences
# Your code here
idx = build_index(words)
# print(idx)
s = random.choice(words)
print(" ".join(idx[s]), end=" ")
