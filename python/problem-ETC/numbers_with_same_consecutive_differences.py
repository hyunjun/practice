#   https://leetcode.com/problems/numbers-with-same-consecutive-differences

#   https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution


from typing import List


class Solution:
    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428
    #   runtime; 72ms, 18.52%
    #   memory; 14.2MB, 22.68%
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.res = set()
        
        def getNumber(n, nums):
            if n <= 0:
                self.res.add(int(''.join(str(n) for n in nums)))
                return
            for diff in [K, -K]:
                if 0 <= nums[-1] + diff <= 9:
                    nums.append(nums[-1] + diff)
                    if n == 1:
                        strNum = ''.join(str(n) for n in nums)
                        if strNum[0] != '0':
                            self.res.add(int(strNum))
                    else:
                        getNumber(n - 1, nums[:])
                    nums.pop()

        nums = []
        for i in range(10):
            nums.append(i)
            getNumber(N - 1, nums)
            nums.pop()
            
        return sorted(list(self.res))


s = Solution()
data = [(3, 7, [181, 292, 707, 818, 929]),
        (2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]),
        (1, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
        ]
for N, K, expect in data:
    real = s.numsSameConsecDiff(N, K)
    print(f'{N} {K} expect {expect} real {real} result {expect == real}')
