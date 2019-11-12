keys = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'

S = input()
i = keys.find(S)
print(['Do', None, 'Re', None, 'Mi', 'Fa', None, 'So', None, 'La', None, 'Si'][i % 12])