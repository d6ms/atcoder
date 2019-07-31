from string import ascii_lowercase


S = input()

if S[0] != 'A':
    print('WA')
    exit(0)
if len(list(filter(lambda e: e == 'C', S[2:-1]))) != 1:
    print('WA')
    exit(0)
if any([c not in ascii_lowercase for c in S[1:S[2:-1].index('C') + 2]]) or any([c not in ascii_lowercase for c in S[S[2:-1].index('C') + 3:]]):
    print('WA')
    exit(0)
print('AC')
