#   https://leetcode.com/problems/queue-reconstruction-by-height

#   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 164ms, 32.62%
    #   memory; 14.4MB, 9.21%
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if people is None or 0 == len(people):
            return []
        res, people = [], sorted(people, key=lambda t: (-t[0], t[1]))
        for h, k in people:
            res.insert(k, [h, k])
        return res


s = Solution()
data = [([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),
        ]
for people, expect in data:
    real = s.reconstructQueue(people)
    print(f'{people} expect {expect} real {real} result {expect == real}')
