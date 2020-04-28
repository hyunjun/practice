#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313


from collections import defaultdict
from typing import List


#   runtime; 1668ms
#   memory; 56.7MB
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums, self.uniques, self.counter = [], [], defaultdict(int)
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if 0 < len(self.uniques):
            return self.uniques[0]
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.counter[value] += 1
        if 1 == self.counter[value]:
            self.uniques.append(value)
        else:
            while 0 < len(self.uniques) and self.counter[self.uniques[0]] > 1:
                self.uniques.pop(0)
