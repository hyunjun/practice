# https://leetcode.com/problems/single-element-in-a-sorted-array


from typing import List


class Solution:
    #   runtime; 72ms, 69.50%
    #   memory; 16.1MB
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums) or len(nums) % 2 == 0:
            return float('-inf')

        totLen = len(nums)

        def getSingle(l, r):
            m = (l + r) // 2
            if l == r or 0 <= m - 1 and m + 1 < totLen and nums[m - 1] != nums[m] != nums[m + 1]:
                return nums[m]
            if (r - m) % 2 == 0 and m + 2 < totLen and nums[m + 1] == nums[m + 2]:
                return getSingle(l, m)
            if (m - l + 1) % 2 == 0 and 0 <= m - 1 and nums[m - 1] == nums[m]:
                return getSingle(m + 1, r)
            if (m - l) % 2 == 0 and 0 <= m - 2 and nums[m - 2] == nums[m - 1]:
                return getSingle(m, r)
            if (r - m + 1) % 2 == 0 and m + 1 < totLen and nums[m] == nums[m + 1]:
                return getSingle(l, m - 1)

        return getSingle(0, totLen - 1)


def search_single_element(arr, l, r):
    if arr is None or 0 == len(arr) or r < l:
        return None
    if 1 == len(arr):
        return arr[0]

    mid = (l + r) // 2
    if 0 < mid and arr[mid - 1] != arr[mid] and mid < len(arr) - 1 and arr[mid] != arr[mid + 1]:
        return arr[mid]

    l_r = mid - 1
    while l < l_r and arr[l_r] == arr[mid]:
        l_r -= 1
    l_ret = search_single_element(arr, l, l_r)
    if l_ret is not None:
        return l_ret

    r_l = mid + 1
    while r_l < r and arr[mid] == arr[r_l]:
        r_l += 1
    r_ret = search_single_element(arr, r_l, r)
    return r_ret


def search_single_element2(arr):
    def _search_single_element(arr, l, r):
        if 1 == r - l:
            return arr[l]
        pivot = l + (r - l) // 4 * 2 # pivot을 무조건 짝수로 만들기 위한 technique

        # 문제의 조건이 단 하나만 한 번 출현하고 나머지는 두 개씩 존재한다고 하기 때문에 가능한 풀이. 멋지다
        if arr[pivot] == arr[pivot + 1]:
            return _search_single_element(arr, pivot + 2, r)
        return _search_single_element(arr, l, pivot + 1)
    return _search_single_element(arr, 0, len(arr))


s = Solution()
data = [([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([1, 1, 2, 2, 3, 3, 4, 8, 8], 4),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([3, 3, 7, 10, 10, 11, 11], 7),
        ([1], 1),
        ]
for nums, expected in data:
    real, real1, real2 = s.singleNonDuplicate(nums), search_single_element(nums, 0, len(nums) - 1), search_single_element2(nums)
    print(f'{nums} expected {expected} real {real} real1 {real1} real2 {real2} result {expected == real == real1 == real2}')
