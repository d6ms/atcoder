from collections import defaultdict

s = input()
x, y = map(int, input().split())

arr = list(map(len, s.split('T')))
EW = [arr[ew] for ew in range(0, len(arr), 2)]
NS = [arr[ns] for ns in range(1, len(arr), 2)]

# dp[i][j] := i回目までの移動で座標jにいることができるか
dp = [defaultdict(bool) for i in range(len(EW))]
dp[0][EW[0]] = True
for i in range(1, len(EW)):
    for prev in dp[i - 1].keys():
        dp[i][prev + EW[i]] = True
        dp[i][prev - EW[i]] = True
if not dp[-1][x]:
    print('No')
    exit(0)

if len(NS) > 0:
    dp = [defaultdict(bool) for i in range(len(NS))]
    dp[0][NS[0]] = True
    dp[0][-NS[0]] = True
    for i in range(1, len(NS)):
        for prev in dp[i - 1].keys():
            dp[i][prev + NS[i]] = True
            dp[i][prev - NS[i]] = True
    if not dp[-1][y]:
        print('No')
        exit(0)

print('Yes')
