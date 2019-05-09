#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5654100301578240


from collections import defaultdict


#   Wrong Answer
def find_subsets0(nums):
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    subsets, distinctNums = [], sorted(list(d.keys()))
    for i in range(2 ** len(distinctNums)):
        indices = []
        for b in range(31, -1, -1):
            if (2 ** b) & i:
                indices.append(b)
        subsets.append([distinctNums[i] for i in indices])
    duplicateSets = []
    for subset in subsets:
        tmp = subset[:]
        for n, cnt in d.items():
            if n not in subset or 1 == cnt:
                continue
            for c in range(2, cnt + 1):
                tmp.append(n)
                duplicateSets.append(tmp[:])
    subsets.extend(duplicateSets)
    return subsets


#   https://leetcode.com/problems/subsets-ii
#   runtime; 52ms, 43.38%
#   memory; 13.4MB, 5.47%
def find_subsets(nums):
    subsets = [[]]
    for n in sorted(nums):
        for subset in subsets.copy():
            tmp = subset[:]
            tmp.append(n)
            if tmp in subsets:
                continue
            subsets.append(tmp)
    return subsets


data = [([1, 3, 3], [[], [1], [3], [1,3], [3,3], [1,3,3]]),
        ([1, 5, 3, 3], [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]]),
        ([1,1,2,2], [[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]),
        ([4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]),
        ]
for nums, expected in data:
    real = find_subsets(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, sorted([sorted(e) for e in expected]) == sorted([sorted(r) for r in real])))
    print(sorted([sorted(e) for e in expected]))
    print(sorted([sorted(r) for r in real]))
