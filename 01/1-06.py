def ngram(s,n):
    l = []
    for i in range(len(s)-n+1):
        l.append(s[i:n+i])
    return l

x = "paraparaparadise"
y = "paragraph"
x2 = set(ngram(x,2))
y2 = set(ngram(y,2))

union = x2.union(y2)
intersection = x2.intersection(y2)
difference_x = x2.difference(y2)
difference_y = y2.difference(x2)

print("和集合は",union,"積集合は",intersection,"XからYを引いた差集合は",difference_x,"YからXを引いた差集合は",difference_y)

word = 'se'

if word in union:
    print("seは、XおよびYに含まれています")
else:
    print("seは、XおよびYに含まれていません")