# TLEになったのでC++で書き直した
from collections import deque

N = int(input())
A = [deque() for _ in range(N + 1)]
for i in range(1, N + 1):
    for e in map(int, input().split()):
        A[i].append(e)

day = [1 for _ in range(N + 1)]
empty_queues = 0
while empty_queues < N:
    matched = False
    for i in range(1, N + 1):
        if len(A[i]) == 0:
            continue
        competitor = A[i].popleft()
        cp = A[competitor].popleft()
        if cp == i:
            matched = True
            date = max(day[i], day[competitor]) + 1
            day[i] = date
            day[competitor] = date
            if len(A[i]) == 0:
                empty_queues += 1
            if len(A[competitor]) == 0:
                empty_queues += 1
        else:
            A[i].appendleft(competitor)
            A[competitor].appendleft(cp)
    if not matched:
        print(-1)
        exit(0)
print(max(day[1:]) - 1)
