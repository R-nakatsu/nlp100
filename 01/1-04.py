w = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = w.split(" ")
print(words)

s = {1,5,6,7,8,9,15,16,19}

dic = {}

for number, word in enumerate(words,1):
    if number in s:
        word2 = word[:1]
    else:
        word2 = word[:2]
    dic[word2] = number
print(dic)

# --------
# コメント
# --------
# L6: `in` の処理は set（集合型）のほうが早いですよ〜
# L15: nとk2が逆ではありませんか？ 文字列から数値への連想配列 だった気がします
# 変数名が気になります…