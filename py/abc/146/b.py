
N = int(input())
S = input()
ans = []
for i, c in enumerate(S):
    num = ord(c) + N
    if num > ord('Z'):
        num -= 26
    ans.append(chr(num))
print(''.join(ans))


