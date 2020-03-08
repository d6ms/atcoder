import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


A, B = MI()
for i in range(20000):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        exit(0)
print(-1)