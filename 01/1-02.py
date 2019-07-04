w1 = "パトカー"
w2 = "タクシー"

r = ""

for word1, word2 in zip(w1,w2):
    r += word1 + word2

print(r)

# --------
# コメント
# --------
# L6: いいですね！ `zip`も使ってみましょうか