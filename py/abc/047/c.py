def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


S = input()
cnt1 = 0
cur = S[0]
for c in S:
    if cur != c:
        cnt1 += 1
        cur = c

cnt2 = 0
cur = S[-1]
for c in reversed(S):
    if cur != c:
        cnt2 += 1
        cur = c

print(min(cnt1, cnt2))
