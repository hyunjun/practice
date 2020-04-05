#   https://leetcode.com/problems/search-in-rotated-sorted-array

#   https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/559929/C%2B%2B-Binary-search-complexity%3A-O(log-N)-No-need-to-find-pivot


from typing import List


class Solution:
    #   runtime; 84ms, 25.43%
    #   memory; 14.2MB, 6.29%
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or 0 == len(nums):
            return -1

        def _search(s, e):
            if s > e:
                return -1
            if s == e:
                if nums[s] == target:
                    return s
                else:
                    return -1
            m = (s + e) // 2
            if nums[m] == target:
                return m
            if nums[s] <= target <= nums[m - 1]:
                _bSearch(s, m - 1)
            if nums[m + 1] <= target <= nums[e]:
                _bSearch(m + 1, e)
            l, r = _search(s, m - 1), _search(m + 1, e)
            return max(l, r)

        def _bSearch(s, e):
            l, r = s, e
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        return _search(0, len(nums) - 1)


s = Solution()
data = [([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 1, 5),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([1], 2, -1),
        ([1, 3], 0, -1),
        ([1, 3], 1, 0),
        ([1, 3], 2, -1),
        ([1, 3], 3, 1),
        ([1, 3], 4, -1),
        ]
for nums, target, expected in data:
    real = s.search(nums, target)
    print(f'{nums} {target} expected {expected} real {real} result {expected == real}')
