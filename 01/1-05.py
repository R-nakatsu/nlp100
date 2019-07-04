def ngram(target,n):
    l = []
    for s in range(len(target)-n+1):
        l.append(target[s:s+n])
    return l

word = "I am an NLPer"
print(ngram(word,2))

word2 = word.split(" ")
print(ngram(word2,2))

# --------
# コメント
# --------
# 完璧です :+1: …が、変数名が…