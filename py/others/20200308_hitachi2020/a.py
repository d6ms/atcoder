import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


S = input()
if len(S) % 2 != 0:
    print('No')
    exit(0)
for i, c in enumerate(S):
    if i % 2 == 0 and c != 'h':
        print('No')
        exit(0)
    if i % 2 != 0 and c != 'i':
        print('No')
        exit(0)
print('Yes')