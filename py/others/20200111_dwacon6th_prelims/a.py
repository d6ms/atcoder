N = int(input())
ST = [tuple(input().split()) for _ in range(N)]
X = input()
flg = False
cnt = 0
for s, t in ST:
    if flg:
        cnt += int(t)
    else:
        if X == s:
            flg = True
print(cnt)