def cipher(word):
    l = ""
    for w in range(len(word)):
        w2 = word[w]
        if w2.islower() == True:
            word_numder = 219 - ord(w2)
            m = chr(word_numder)
            l += m
        else:
            l += w2
    return l


words1 = "I am so Happy"

result = cipher(words1)
print(result)

result = cipher(result)
print(result)