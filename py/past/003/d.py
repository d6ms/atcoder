import sys

sys.setrecursionlimit(300000)


def I(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LMI(): return list(map(int, sys.stdin.readline().split()))


MOD = 10 ** 9 + 7
INF = float('inf')

N = I()

digits = ['.###..#..###.###.#.#.###.###.###.###.###.',
          '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
          '.#.#..#..###.###.###.###.###...#.###.###.',
          '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
          '.###.###.###.###...#.###.###...#.###.###.']
def get(dig, n):
    return ''.join(row[4 * n:4 *n +4]for row in dig)

S = [input() for _ in range(5)]
for d in range(len(S[0]) // 4):
    s = get(S, d)
    for i in range(10):
        if s == get(digits, i):
            print(i, end='')
            break