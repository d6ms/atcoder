import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


S = input()
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        print(i + 1, i + 2)
        exit(0)
    if i < len(S) - 2:
        if S[i] == S[i + 2]:
            print(i + 1, i + 3)
            exit(0)
print(-1, -1)
