def solve(candidates):
    curr_time = 0
    candidates = sorted(candidates)
    while len(candidates) > 0:
        if curr_time % 10 != 0:
            curr_time += 10 - (curr_time % 10)
        losses = list(map(lambda c: calc_loss(curr_time, c), candidates))
        min_loss = losses[0]
        min_loss_candidate_idx = 0
        for i, loss in enumerate(losses):
            if loss <= min_loss:
                min_loss = loss
                min_loss_candidate_idx = i
        dish = candidates.pop(min_loss_candidate_idx)
        curr_time += dish
    return curr_time


def calc_loss(curr_time, candidate):
    return (10 - ((curr_time + candidate) % 10)) % 10


candidates = []
for _ in range(5):
    candidates.append(int(input()))

print(solve(candidates))