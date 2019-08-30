T = int(input())
Q = [tuple(map(int, input().split())) for _ in range(T)]

for A, B, C, D in Q:
    if A < B:
        print('No')
        continue
    if B > D:
        print('No')
        continue
    if C >= B:
        print('Yes')
        continue
    # B <= A, B <= D, B <= C である
    # 解説見ればこのあとの実装はできるが、理解できない