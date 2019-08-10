from heapq import heappush, heappop
from collections import defaultdict


N, M = map(int, input().split())
d = defaultdict(list)  # {deadline: [rewards]}
for _ in range(N):
    A, B = map(int, input().split())
    deadline = M - A
    d[deadline].append(B)

ans = list()
for day in range(M + 1):
    rewards = d.get(day)
    if rewards is None or len(rewards) == 0:
        continue
    for reward in rewards:
        if len(ans) <= day:
            heappush(ans, reward)
        else:
            min_reward = heappop(ans)
            if reward > min_reward:
                heappush(ans, reward)
            else:
                heappush(ans, min_reward)

print(sum(ans))
