#   https://leetcode.com/problems/sum-of-all-odd-length-subarrays


from typing import List


class Solution:
    #   runtime; 68ms, 33.33%
    #   memory; 13.9MB, 33.33%
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, lenArr = 0, len(arr)
        for oddLen in range(1, lenArr + 1, 2):
            for i in range(lenArr - oddLen + 1):
                res += sum(arr[i:i + oddLen])
        return res


s = Solution()
data = [([1,4,2,5,3], 58),
        ([1,2], 3),
        ([10,11,12], 66),
        ]
for arr, expect in data:
    real = s.sumOddLengthSubarrays(arr)
    print(f'{arr} expect {expect} real {real} result {expect == real}')
