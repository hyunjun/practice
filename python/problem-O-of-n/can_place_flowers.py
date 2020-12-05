#   https://leetcode.com/problems/can-place-flowers

#   https://leetcode.com/problems/can-place-flowers/solution


from typing import List


class Solution:
    #   15.33%
    def canPlaceFlowers0(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            if (i - 1 < 0 or 0 <= i - 1 and 0 == flowerbed[i - 1]) and \
                0 == flowerbed[i] and (i + 1 < len(flowerbed) and \
                0 == flowerbed[i + 1] or len(flowerbed) <= i + 1):
                flowerbed[i] = 1
                n -= 1
                i += 2
            else:
                i += 1
        return n <= 0

    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555
    #   runtime; 168ms, 41.51%
    #   memory; 14.6MB, 26.13%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if 1 == l and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1
        if 1 < l and flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if 1 < l and flowerbed[l - 2] == flowerbed[l - 1] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1
        for i in range(1, l - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

s = Solution()
data = [([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([1,0,0,0,0,1],  2, False),
        ([0,0,1,0,1], 1, True),
        ([0], 1, True),
        ]
for flowerbed, n, expected in data:
    print('before {}, {}'.format(flowerbed, n))
    real = s.canPlaceFlowers(flowerbed, n)
    print('after  {}, {}, expected {}, real {}, result {}'.format(flowerbed, n, expected, real, expected == real))
