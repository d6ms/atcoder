S = input()

NS = ('N' in S and 'S' in S) or ('N' not in S and 'S' not in S)
EW = ('E' in S and 'W' in S) or ('E' not in S and 'W' not in S)

if NS and EW:
    print('Yes')
else:
    print('No')
