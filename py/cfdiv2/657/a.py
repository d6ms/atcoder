import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


def count_without_q(S):
    cnt = 0
    state = 0
    for i, c in enumerate(S):
        if c == 'a':
            state = state & int('0101010', 2)
            state = state >> 1
            state += 64
        elif c == 'b':
            state = state & int('1000100', 2)
            state = state >> 1
        elif c == 'c':
            state = state & int('0010000', 2)
            state = state >> 1
        else:
            state = 0
        # print(bin(state)[2:].zfill(7))
        if state & 1:
            cnt += 1
    return cnt

T = I()
for t in range(T):
    N = I()
    S = input()
    cnt = count_without_q(S)
    if cnt == 1:
        print('Yes')
        print(S.replace('?', 'd'))
        continue
    elif cnt > 1:
        print('No')
        continue

    achieved = False
    state = 0
    for i, c in enumerate(S):
        if c == 'a':
            state = state & int('0101010', 2)
            state = state >> 1
            state += 64
        elif c == 'b':
            state = state & int('1000100', 2)
            state = state >> 1
        elif c == 'c':
            state = state & int('0010000', 2)
            state = state >> 1
        elif c == '?':
            if achieved:
                state = 0
            state = state >> 1
            state += 64
        else:
            state = 0
        # print(bin(state)[2:].zfill(7))
        if state & 1:
            start, end = i - 6, i + 1
            if S[end:end+6] != 'bacaba' and S[start-6:start] != 'abacab':
                print('Yes')
                print((S[:start] + 'abacaba' + S[end:]).replace('?', 'd'))
                achieved = True
                break
    if not achieved:
        print('No')