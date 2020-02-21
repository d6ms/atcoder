def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N, K = MI()
A = LMI()
A.sort(key=lambda x: abs(x))

cnt = 0
for i, a in enumerate(A):
    if cnt < K <= cnt + (N - i - 1):
        offset = K - cnt
        cand = [a * b for b in A[i + 1:]]
        cand.sort()
        print(cand[offset - 1])
        exit(0)
    cnt += N - (i + 1)