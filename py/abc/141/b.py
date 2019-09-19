S = input()

for i, c in enumerate(S):
    if (i % 2 == 0 and c in 'RUD') or (i % 2 != 0 and c in 'LUD'):
        continue
    else:
        print('No')
        exit(0)
print('Yes')
