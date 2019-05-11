#   https://www.geeksforgeeks.org/amazon-sde-ii-interview-experience


#   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#   runtime; 36ms, 98.94%
#   memory; 13.8MB, 5.06%
def find_range(nums, k):
    if nums is None or 0 == len(nums):
        return [-1, -1]

    def lower_bound():
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k and (m == 0 or (0 <= m - 1 and nums[m - 1] < k)):
                return m
            if k <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1

    def upper_bound():
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k and (m == len(nums) - 1 or (m + 1 < len(nums) and k < nums[m + 1])):
                return m
            if nums[m] <= k:
                l = m + 1
            else:
                r = m - 1
        return -1

    return [lower_bound(), upper_bound()]


data = [([1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 100, 100, 100, 100], 3, [5, 12]),
        ([1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 100, 100, 100, 100], 1, [0, 3]),
        ([1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 100, 100, 100, 100], 2, [4, 4]),
        ([1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 100, 100, 100, 100], 5, [13, 15]),
        ([1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 100, 100, 100, 100], 100, [16, 19]),
        ]
for nums, k, expected in data:
    real = find_range(nums, k)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
