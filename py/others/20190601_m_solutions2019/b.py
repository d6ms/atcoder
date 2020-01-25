S = input()

k = len(S)
win = S.count('o')
if win + 15 - k >= 8:
    print('YES')
else:
    print('NO')
