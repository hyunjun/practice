#   https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/
#   time complexity limit O(n), space complexity limit O(1)
#   Being no space complexity limit, it's very easy


def removed_two_items(nums):
    if nums is None or 0 == len(nums):
        return []

    xored = nums[0]
    for n in nums[1:]:
        xored ^= n
        #print(n, xored)
    idx_a, idx_b, a, b, check = -1, -1, 0, 0, xored & -xored
    for i, n in enumerate(nums):
        if n & check:
            a ^= n
            #print(n, n & check, a)
            idx_a = i
        else:
            b ^= n
            #print(n, n & check, b)
            idx_b = i

    if idx_a < idx_b:
        return [a, b]
    return [b, a]


data = [([2, 1, 5, 6, 6, 1], [2, 5]), ([9, 9, 4, 3], [4, 3])]

for nums, oup in data:
    real = removed_two_items(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, oup, real, oup == real))
