import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


H, W = MI()

if H == 1 or W == 1:
    print(1)
elif H % 2 == 0 and W % 2 == 0:
    print((H * W) // 2)
elif H % 2 == 0 and W % 2 != 0:
    print((H * (W - 1)) // 2 + (H // 2))
elif W % 2 == 0 and H % 2 != 0:
    print((W * (H - 1)) // 2 + (W // 2))
else:
    print(((W - 1) * (H - 1)) // 2 + (W // 2) + (H // 2) + 1)