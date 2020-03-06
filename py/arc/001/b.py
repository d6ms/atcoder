import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7

A, B = MI()
x = abs(B - A)

ans = float('inf')
for i in range(-40, 41):
    for j in range(-8, 9):
        for k in range(-4, 5):
            if i + j * 5 + k * 10 == x:
                ans = min(ans, abs(i) + abs(j) + abs(k))
print(ans)