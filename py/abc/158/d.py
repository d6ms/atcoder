import sys
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


q = deque()
for c in input():
    q.append(c)

rev = False
for _ in range(I()):
    query = input()
    if query.startswith('1'):
        rev = not rev
        continue
    _, f, c = query.split()
    right = f == '2'
    right = not right if rev else right
    if right:
        q.append(c)
    else:
        q.appendleft(c)

if rev:
    print(''.join(reversed(q)))
else:
    print(''.join(q))
