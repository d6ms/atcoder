N, K = map(int, input().split())
S = input()

target = ''
if S[K - 1] == 'A':
    target = 'a'
elif S[K - 1] == 'B':
    target = 'b'
elif S[K - 1] == 'C':
    target = 'c'
print(S[:K - 1] + target + S[K:])
