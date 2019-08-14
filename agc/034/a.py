N, A, B, C, D = map(int, input().split())
S = '#' + input()

if '##' in S[A: C] or '##' in S[B: D]:
    print('No')
    exit(0)

if C > D:
    if '...' not in S[B - 1: D + 2]:
        print('No')
        exit(0)

print('Yes')
