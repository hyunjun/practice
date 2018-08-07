#   https://leetcode.com/problems/can-place-flowers

#   https://leetcode.com/problems/can-place-flowers/solution


class Solution:
    #   15.33%
    def canPlaceFlowers(self, flowerbed, n):
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


s = Solution()
data = [([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ]
for flowerbed, n, expected in data:
    print('before {}, {}'.format(flowerbed, n))
    real = s.canPlaceFlowers(flowerbed, n)
    print('after  {}, {}, expected {}, real {}, result {}'.format(flowerbed, n, expected, real, expected == real))
