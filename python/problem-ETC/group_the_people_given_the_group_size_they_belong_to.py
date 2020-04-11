#   https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 80ms, 59.01%
    #   memory; 14.1MB, 100.00%
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        if groupSizes is None or not (1 <= len(groupSizes) <= 500):
            return []
        d = defaultdict(list)
        for i, n in enumerate(groupSizes):
            d[n].append(i)
        res = []
        for gs, indices in sorted(d.items(), key=lambda t: t[0]):
            if len(indices) <= gs:
                res.append(indices)
            else:
                for i in range(0, len(indices), gs):
                    res.append(indices[i:i + gs])
        return res


s = Solution()
data = [[3, 3, 3, 3, 3, 1, 3],
        [2, 1, 3, 3, 3, 2],
        ]
for groupSize in data:
    print(groupSize, s.groupThePeople(groupSize))
