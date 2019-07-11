N = int(input())
L = list(map(int, input().split()))

longest = max(L)
if longest < sum(L) - longest:
    print('Yes')
else:
    print('No')