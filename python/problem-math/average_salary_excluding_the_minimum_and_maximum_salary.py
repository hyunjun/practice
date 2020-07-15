#   https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary


from typing import List


class Solution:
    #   runtime; 32ms, 78.03%
    #   memory; 13.9MB, 25.00%
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)


s = Solution()
data = [([4000,3000,1000,2000], 2500.00000),
        ([1000,2000,3000], 2000.00000),
        ([6000,5000,4000,3000,2000,1000], 3500.00000),
        ([8000,9000,2000,3000,6000,1000], 4750.00000),
        ]
for salary, expect in data:
    real = s.average(salary)
    print(f'{salary} expect {expect} real {real} result {expect == real}')
