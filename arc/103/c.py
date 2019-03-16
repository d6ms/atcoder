
def solve(v):
    e = v[0::2]
    o = v[1::2]
    e_mode, e_mode2 = mode(e)
    o_mode, o_mode2 = mode(o)
    if e_mode != o_mode:
        return distance(e, o, e_mode, o_mode)
    else:
        if e_mode2 is None and o_mode2 is not None:
            return distance(e, o, e_mode, o_mode2)
        elif e_mode2 is not None and o_mode2 is None:
            return distance(e, o, e_mode2, o_mode)
        elif e_mode2 is None and o_mode is None:
            return len(e)
        else:
            return min(distance(e, o, e_mode, o_mode2), distance(e, o, e_mode2, o_mode))


def mode(arr):
    arr = sorted(arr)

    mode = None
    mode_count = 0
    mode2 = None
    mode2_count = 0

    curr_num = None
    curr_count = 0

    for num in arr:
        if curr_num is None:
            curr_num = num
            curr_count = 1
        elif curr_num == num:
            curr_count += 1
        else:
            if curr_count >= mode_count:
                mode2 = mode
                mode2_count = mode_count
                mode = curr_num
                mode_count = curr_count
            curr_num = num
            curr_count = 1
    if curr_count >= mode_count:
        mode2 = mode
        mode2_count = mode_count
        mode = curr_num
        mode_count = curr_count
    return mode, mode2


def distance(e, o, e_num, o_num):
    distance = 0
    for num in e:
        if num != e_num:
            distance += 1
    for num in o:
        if num != o_num:
            distance += 1
    return distance


n = map(int, input())
v = list(map(int, input().split()))

print(solve(v))
