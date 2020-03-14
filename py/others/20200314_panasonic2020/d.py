import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


s = 'abcdefghijklmnop'
N = I()

for c1 in range(1):
    if N == 1:
        print(s[c1])
        continue
    for c2 in range(2):
        if N == 2:
            print(s[c1]+s[c2])
            continue
        for c3 in range(max(c1, c2) + 2):
            if N == 3:
                print(s[c1] + s[c2] + s[c3])
                continue
            for c4 in range(max(c1, c2, c3) + 2):
                if N == 4:
                    print(s[c1] + s[c2] + s[c3] + s[c4])
                    continue
                for c5 in range(max(c1, c2, c3, c4) + 2):
                    if N == 5:
                        print(s[c1] + s[c2] + s[c3] + s[c4] + s[c5] )
                        continue
                    for c6 in range(max(c1, c2, c3, c4, c5) + 2):
                        if N == 6:
                            print(s[c1] + s[c2] + s[c3] + s[c4] + s[c5] + s[c6])
                            continue
                        for c7 in range(max(c1, c2, c3, c4, c5, c6) + 2):
                            if N == 7:
                                print(s[c1] + s[c2] + s[c3] + s[c4] + s[c5] + s[c6] + s[c7] )
                                continue
                            for c8 in range(max(c1, c2, c3, c4, c5, c6, c7) + 2):
                                if N == 8:
                                    print(s[c1] + s[c2] + s[c3] + s[c4] + s[c5] + s[c6] + s[c7] + s[c8])
                                    continue
                                for c9 in range(max(c1, c2, c3, c4, c5, c6, c7, c8) + 2):
                                    if N == 9:
                                        print(s[c1]+s[c2]+s[c3]+s[c4]+s[c5]+s[c6]+s[c7]+s[c8]+s[c9])
                                        continue
                                    for c10 in range(max(c1, c2, c3, c4, c5, c6, c7, c8, c9) + 2):
                                        print(s[c1]+s[c2]+s[c3]+s[c4]+s[c5]+s[c6]+s[c7]+s[c8]+s[c9]+s[c10])
