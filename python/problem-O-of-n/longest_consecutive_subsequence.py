#   https://leetcode.com/problems/longest-consecutive-sequence

#   https://leetcode.com/problems/longest-consecutive-sequence/solution


class Solution:
    #   Memory Error
    def longestConsecutive0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1
        _min, _max = nums[0], nums[0]
        for n in nums:
            _min = min(_min, n)
            _max = max(_max, n)
        arr = [None] * (_max - _min + 1)
        for i, n in enumerate(nums):
            arr[n - _min] = n
        maxCnt = 0
        for i, a in enumerate(arr):
            if a:
                if 0 == i or arr[i - 1] is None:
                    cur = 1
                elif arr[i - 1]:
                    cur += 1
            else:
                if arr[i - 1]:
                    maxCnt = max(maxCnt, cur)
        return maxCnt

    #   98.58%
    def longestConsecutive(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        maxConsecutiveNum, s = 1, set(nums)
        for n in nums:
            if n not in s:
                continue
            m, cur = n + 1, 1
            while m in s:
                s.remove(m)
                cur += 1
                m += 1
            m = n - 1
            while m in s:
                s.remove(m)
                cur += 1
                m -= 1
            maxConsecutiveNum = max(maxConsecutiveNum, cur)
        return maxConsecutiveNum


s = Solution()
data = [([100, 4, 200, 1, 3, 2], 4),
        ([-100, 4, 200, 1, 3, 2], 4),
        ([2147483646, -2147483647, 0, 2, 2147483644, -2147483645, 2147483645], 3),
        ]
for nums, expected in data:
    real = s.longestConsecutive(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
