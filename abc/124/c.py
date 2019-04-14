def solve(S):
    cnt0 = 0
    cnt1 = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '1':
                cnt1 += 1
            else:
                cnt0 += 1
        else:
            if S[i] == '1':
                cnt0 += 1
            else:
                cnt1 += 1
    return min(cnt0, cnt1)


S = input()
print(solve(S))