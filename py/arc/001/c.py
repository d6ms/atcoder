import sys
from itertools import permutations

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


vacant_rows = list()
vacant_cols = {0, 1, 2, 3, 4, 5, 6, 7}
Q = set()
for i in range(8):
    line = input()
    if line.count('Q') > 1:
        print('No Answer')
        exit(0)
    idx = line.find('Q')
    if idx == -1:
        vacant_rows.append(i)
    else:
        if idx in vacant_cols:
            vacant_cols.remove(idx)
        Q.add((i, idx))
vacant_cols = list(vacant_cols)


def is_valid(queens):
    if len(set(i for i, j in queens)) < len(queens) or len(set(j for i, j in queens)) < len(queens):
        return False
    for i, j in queens:
        for t in range(1, 8):
            for ex, ey in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x, y = i + t * ex, j + t * ey
                if (x, y) in queens:
                    return False
    return True


def print_queens(queens):
    for i in range(8):
        for j in range(8):
            c = 'Q' if (i, j) in queens else '.'
            print(c, end='')
        print()


if not is_valid(Q):
    print('No Answer')
    exit(0)

for r0, r1, r2, r3, r4 in permutations(vacant_rows, 5):
    queens = set()
    for i, j in Q:
        queens.add((i, j))
    queens.add((r0, vacant_cols[0]))
    queens.add((r1, vacant_cols[1]))
    queens.add((r2, vacant_cols[2]))
    queens.add((r3, vacant_cols[3]))
    queens.add((r4, vacant_cols[4]))
    if is_valid(queens):
        print_queens(queens)
        exit(0)
print('No Answer')
