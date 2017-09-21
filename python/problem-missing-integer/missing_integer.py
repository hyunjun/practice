#   demo from codility.com

def missing_integer(nums):
    if nums is None or 0 == len(nums):
        return 1

    max_num = snd_max_num = 0 if nums[0] < 1 else nums[0]
    for n in nums:
        if max_num < n:
            snd_max_num = max_num
            max_num = n
        elif snd_max_num < n:
            snd_max_num = n

    if 0 < snd_max_num:
        if max_num - snd_max_num <= 1:
            return max_num + 1
        return snd_max_num + 1
    return 1


cases = [([1, 3, 6, 4, 1, 2], 5), ([1, 2, 3], 4), ([-1, -3], 1), ([-1], 1), ([10], 11)]
for nums, expected in cases:
    real = missing_integer(nums)
    print('{}\texpected {}\treal {}\tresult {}'.format(nums, expected, real, expected == real))
