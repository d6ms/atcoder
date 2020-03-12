import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


H, W = MI()
print('#' * (W + 2))
for _ in range(H):
    print('#' + input() + '#')
print('#' * (W + 2))