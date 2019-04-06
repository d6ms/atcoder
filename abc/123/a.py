a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

flg = True
for x, y in [(a, b), (a, c), (a, d), (a, e), (b, c), (b, d), (b, e), (c, d), (c, e), (d, e)]:
    if y - x <= k:
        continue
    else:
        flg = False
        break
if flg:
    print("Yay!")
else:
    print(":(")
