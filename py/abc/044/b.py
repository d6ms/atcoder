import sys
from collections import Counter

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


w = input()
counter = Counter(w)
for c, num in counter.items():
    if num % 2 != 0:
        print('No')
        exit(0)
print('Yes')