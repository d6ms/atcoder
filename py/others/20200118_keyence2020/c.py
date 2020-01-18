N, K, S = map(int, input().split())
if S == 10 ** 9:
    ans = [10 ** 9] * K
    ans.extend([1] * (N - K))
else:
    ans = [S] * K
    ans.extend([S + 1] * (N - K))
print(' '.join([str(x) for x in ans]))