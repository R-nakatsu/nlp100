w = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = []

words = w.replace(",","").replace(".","").split(" ")
print(words)

for word in words:
    l.append(len(word))

print(l)

# --------
# コメント
# --------
# アルゴリズム的には完璧です！あとは変数名が少しきになる程度
# w2 -> words, i -> word とかはどうでしょうか
# ちなみに、i は index の i なので、今回のようにリストの中身を直接受ける場合は不適切です。1-02.pyは逆に適切です