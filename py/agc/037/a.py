S = input()

cnt = 0
prev = ''
i = 0
while i < len(S):
    if i == len(S) - 1 and S[i] == prev:
        break
    if S[i] == prev:
        cnt += 1
        prev = S[i: i + 2]
        i += 2
    else:
        cnt += 1
        prev = S[i]
        i += 1
print(cnt)
