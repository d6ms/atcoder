import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7

N = I()
C = input()
print(max(C.count('1'), C.count('2'), C.count('3'), C.count('4')), min(C.count('1'), C.count('2'), C.count('3'), C.count('4')))