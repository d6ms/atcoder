def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


S = input()
S = ''.join(list(reversed(S)))
while len(S) > 0:
    if S[:7] == 'remaerd':
        S = S[7:]
    elif S[:6] == 'resare':
        S = S[6:]
    elif S[:5] in ['esare', 'maerd']:
        S = S[5:]
    else:
        print('NO')
        exit(0)
print('YES')
