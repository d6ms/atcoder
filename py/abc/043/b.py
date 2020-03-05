import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


s = input()
stack = list()
for c in s:
    if c == 'B':
        if len(stack) > 0:
            stack.pop()
    else:
        stack.append(c)
print(''.join(stack))
