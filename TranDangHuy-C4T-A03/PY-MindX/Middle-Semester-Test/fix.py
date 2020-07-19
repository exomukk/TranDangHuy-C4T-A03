def reachTarget(target):
    target = abs(target)
    sum = 0
    step = 0
    while ((sum < target) or (sum - target) % 2 !=0 ):
        step = step + 1
        sum = sum + step

    return step



def steps(source, step, dest):
    if (abs(source) > (dest)):
        return 2 * abs(dest) - 1

    if (source == dest):
        return step

    pos = steps(source + step + 1, step + 1, dest)

    neg = steps(source - step - 1, step + 1, dest)

    return min(pos, neg)
    