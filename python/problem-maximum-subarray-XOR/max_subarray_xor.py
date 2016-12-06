#   http://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
from copy import deepcopy

def subset(arr):
    if 0 == len(arr):
        return [[]]
    else:
        last = arr.pop()
        subset_n_1 = subset(arr)
        cur_subset = deepcopy(subset_n_1)
        [item.append(last) for item in cur_subset]
        subset_n_1.extend(cur_subset)
        return subset_n_1


def max_subarray_xor(arr):
    candidates, max_val = [], 0
    for indices in subset(range(len(arr))):
        candidate_arr = [arr[idx] for idx in indices]
        if 0 == len(candidate_arr):
            continue
        val = reduce(lambda a, b: a ^ b, candidate_arr)
        # print candidate_arr, val, max_val, candidates
        if max_val < val:
            candidates = [candidate_arr]
            max_val = val
        elif max_val == val:
            candidates.append(candidate_arr)
    # print candidates
    return sorted(candidates, key=lambda t: len(t), reverse=True)[0]

data = [([1, 2, 3, 4], 7),
        ([8, 1, 2, 12, 7, 6], 15),
        ([4, 6], 6)]

for arr, max_val in data:
    print 'inp {}\ttarget max value {}\tmax subarray {}'.format(arr, max_val, max_subarray_xor(arr))
