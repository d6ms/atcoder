N = input()
S = input()
mid = len(S) // 2
if S[:mid] == S[mid:]:
    print('Yes')
else:
    print('No')
