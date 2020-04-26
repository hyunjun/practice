#   https://leetcode.com/problems/random-pick-index

#   https://leetcode.com/problems/random-pick-index/discuss/597400/Python-O(1)-and-Sampling


from collections import defaultdict
from typing import List
import random


#   runtime; 440ms, 8.04%
#   memory; 23.6MB, 33.33%
class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, n in enumerate(nums):
            self.indices[n].append(i)

    def pick(self, target: int) -> int:
        if target not in self.indices:
            return -1
        indexList = self.indices[target]
        return indexList[random.randint(0, len(indexList) - 1)]


s = Solution([1, 2, 3, 3, 3])
print(0 == s.pick(1))
print(1 == s.pick(2))
print(2 == s.pick(3) or 3 == s.pick(3) or 4 == s.pick(3))
