#   https://leetcode.com/problems/rotate-array
#   30.55%

#   https://leetcode.com/problems/rotate-array/solution


class Solution:
    def rotate0(self, nums, k):
        if nums is None or 0 == len(nums) or k < 0:
            return
        n = len(nums)
        while n <= k:
            k -= n
        if 0 == k:
            return
        print('[0]', nums)
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print('[1]', nums)
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print('[2]', nums)
        l, r = k, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print('[3]', nums)

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496
    #   runtime; 52ms, 98.25%
    #   memory; 15.5MB
    def rotate1(self, nums, k):
        if nums is None or 0 == len(nums) or k <= 0:
            return
        print(len(nums), k, k % len(nums))
        k = k % len(nums) if k >= len(nums) else k
        if k == 0:
            return
        for i, a in enumerate(nums[-k:] + nums[:len(nums) - k]):
            nums[i] = a

    #   runtime; 56ms, 93.55%
    #   memory; 15.4MB
    def rotate(self, nums, k):
        if nums is None or 0 == len(nums) or k <= 0:
            return
        k = k % len(nums) if k >= len(nums) else k
        if k == 0:
            return

        def swaps(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swaps(0, len(nums) - k - 1)
        swaps(len(nums) - k, len(nums) - 1)
        swaps(0, len(nums) - 1)


s = Solution()
data = [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([-1, -100, 3, 99], 3, [-100, 3, 99, -1]),
        ([1, 2], 3, [2, 1]),
        ([1, 2], 2, [1, 2]),
        ([1, 2], 0, [1, 2]),
        ([1, 2, 3, 4, 5, 6], 1, [6, 1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5, 6, 7], 100, [6, 7, 1, 2, 3, 4, 5]),
        ]
for nums, k, expected in data:
    s.rotate(nums, k)
    print('expected {}, real {}, result {}'.format(expected, nums, expected == nums))
