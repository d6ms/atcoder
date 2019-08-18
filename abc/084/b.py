A, B = map(int, input().split())
S = input()

for i in range(A):
    if 48 > ord(S[i]) or ord(S[i]) > 57:
        print('No')
        exit(0)
if S[A] != '-':
    print('No')
    exit(0)
for i in range(A + 1, len(S)):
    if 48 > ord(S[i]) or ord(S[i]) > 57:
        print('No')
        exit(0)
print('Yes')