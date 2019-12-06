S = input()

if len(S) == 2:
    print(S)
else:
    print(''.join(list(reversed(list(S)))))
