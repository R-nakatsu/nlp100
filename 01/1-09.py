import random

words = ""

word1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word_split = word1.split(" ")

for i in range(len(word_split)):
    if len(word_split[i]) > 4:
        word = word_split[i]
        inter = word[1:-1]
        print(inter)
        inter1 = ''.join(random.sample(inter, len(inter)))
        word2 = word[0] + inter1 + word[-1]
        words += word2
        words += " "
    else:
        words += word_split[i]
        words += " "
print(words)
