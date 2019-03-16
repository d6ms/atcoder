N, M = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]

A_B = sorted(A_B, key=lambda a_b: a_b[0]) # 価格の安い順に並べ替え

count = 0
amt = 0
for a_b in A_B:
    a = a_b[0]
    b = a_b[1]
    if count + b < M:
        count += b
        amt += a * b
        continue
    else:
        amt += ((M - count) * a)
        break

print(amt)