def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

N = I()
A = [I() for _ in range(N)]

seen = set()
i = 0
light = 1
while light != 2:
    seen.add(light)
    light = A[light - 1]
    if light in seen:
        print(-1)
        exit(0)
    i += 1
print(i)
