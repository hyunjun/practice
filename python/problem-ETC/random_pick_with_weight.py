#   https://leetcode.com/problems/random-pick-with-weight

#   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351

#   https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation-(update)
#   https://leetcode.com/problems/random-pick-with-weight/discuss/671889/Python-6-lines-Solution-with-Statistics-Explanation

from collections import defaultdict
from typing import List
import random


#   Time Limit Exceeded
class Solution1:
    def __init__(self, w: List[int]):
        self.val = []
        for i, n in enumerate(w):
            self.val.extend([i] * n)

    def pickIndex(self) -> int:
        return random.choice(self.val)

#   Wrong Answer
class Solution2:
    def __init__(self, w: List[int]):
        self.val, self.s = defaultdict(int), 0
        for i, n in enumerate(w):
            for j in range(self.s, self.s + n):
                self.val[j] = i
            self.s = n

    def pickIndex(self) -> int:
        return self.val[random.randint(0, self.s - 1)]

#   Time Limit Exceeded
class Solution3:
    def __init__(self, w: List[int]):
        self.nums = []
        for i, n in enumerate(w):
            self.nums.extend([i] * n)
        self.copied = self.nums.copy()

    def pickIndex(self) -> int:
        if 0 == len(self.copied):
            self.copied = self.nums.copy()
        idx = random.randint(0, len(self.copied) - 1)
        return self.copied.pop(idx)
