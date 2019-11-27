# 小手先の高速化してみたけどTLE
from collections import defaultdict
import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    t = input().strip()

    charset = set()
    for c in t:
        charset.add(c)
    for c in charset:
        if c not in s:
            print(-1)
            exit(0)

    d = defaultdict(list)  # d[c] := cはsの何番目に出現するか
    for i, c in enumerate(s):
        d[c].append(i + 1)

    ans = 0
    S = s
    at = 0
    for c in t:
        found = False
        while not found:
            for i in d[c]:
                if i > at:
                    ans += i - at
                    at = i
                    found = True
                    break
            if not found:
                ans += len(S) - at
                at = 0
    print(ans)


if __name__ == '__main__':
    main()
