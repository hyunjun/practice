#   https://leetcode.com/problems/find-all-duplicates-in-an-array

#   https://medium.com/solvingalgo/solving-algorithmic-problems-find-a-duplicate-in-an-array-3d9edad5ad41


from typing import List


class Solution:
    #   runtime; 168ms, 78,59%
    #   memory; 19.9MB, 100.00%
    def findDuplicates0(self, nums):
        if nums is None or 0 == len(nums):
            return []
        s, res = set(), []
        for n in nums:
            if n in s:
                res.append(n)
            else:
                s.add(n)
        return res

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414
    #   runtime; 544ms, 25.20%
    #   memory; 21MB
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        sortedNums, res = [None] * len(nums), []
        for n in nums:
            if sortedNums[n - 1] is None:
                sortedNums[n - 1] = n
            else:
                res.append(n)
        return res

    #   runtime; 860ms
    #   memory; 20.7MB
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, res = 0, set()
        while i < len(nums):
            n = nums[i]
            if n == nums[n - 1]:
                if i != n - 1:
                    res.add(n)
                i += 1
                continue
            nums[i], nums[n - 1] = nums[n - 1], nums[i]
        return list(res)
            
            
s = Solution()
data = [([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]), 
        ]
for nums, expect in data:
    real = s.findDuplicates(nums)
    print(f'{nums}, expect {expect}, real {real}, result {expect == real}')
'''
i
1 2 3 4 5 6 7 8
4 3 2 7 8 2 3 1
7     4
3           7
2   3
3 2
        1     8
1       3
'''
