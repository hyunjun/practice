import random


arrs = [ [], [5], [5, 5], [4, 5], [5, 6, 6], [ 0, 3, 5, 1, 5, 5 ] ]


def get_max_and_num(arr):
    if arr is None or len(arr) == 0:
        return (-1, -1)
    cand = arr[:1][0]
    num = 0
    for a in arr:
        if a == cand:
            num += 1
        elif cand < a:
            cand = a
            num = 1
    return (cand, num)


def get_index_of_max(arr, maximum, num):
    if arr is None or len(arr) == 0:
        return -1
    occurence = -1
    last_idx = -1
    for i, a in enumerate(arr):
        if a == maximum:
            occurence += 1
            if occurence == random.randint(0, num-1):
                return i
            last_idx = i
    return last_idx


def get_index_of_max2(arr):
    if arr is None or len(arr) == 0:
        return -1
    idxHash = {}
    maxVal = arr[:1][0]
    for i, a in enumerate(arr):
        if a not in idxHash:
            l = []
            l.append(i)
            idxHash[a] = l
        else:
            l = idxHash[a]
            l.append(i)
            idxHash[a] = l
        if maxVal < a:
            maxVal = a
    l = idxHash[maxVal]
    cnt = len(l)
    return l.pop(random.randint(0, cnt-1))


if __name__ == "__main__":
    for arr in arrs:
        maximum, num = get_max_and_num(arr)
        if maximum != -1:
            print(arr, "=> max %d's index %d" % (maximum, get_index_of_max(arr, maximum, num)))

    for arr in arrs:
        print(arr, "=> max value's index %d" % get_index_of_max2(arr))

