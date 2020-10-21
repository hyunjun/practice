#   https://leetcode.com/problems/asteroid-collision

#   https://leetcode.com/problems/asteroid-collision/solution


from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3502
    #   runtime; 140ms, 22.01%
    #   memory; 14.9MB
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if asteroids is None or len(asteroids) < 2 or all(a > 0 for a in asteroids) or all(a < 0 for a in asteroids):
            return asteroids
        i = 1
        while 0 < i < len(asteroids):
            l, r = i - 1, i
            if asteroids[l] > 0 and asteroids[r] < 0:
                sizeL, sizeR = asteroids[l], -1 * asteroids[r]
                if sizeL > sizeR:
                    asteroids.pop(r)
                elif sizeL < sizeR:
                    asteroids.pop(l)
                    i -= 1
                else:
                    asteroids.pop(r)
                    asteroids.pop(l)
                    i -= 2
                if i < 1:
                    i = 1
            else:
                i += 1
        return asteroids


s = Solution()
data = [([5,10,-5], [5,10]),
        ([8,-8], []),
        ([10,2,-5], [10]),
        ([-2,-1,1,2], [-2,-1,1,2]),
        ([1,-2,-2,1], [-2,-2,1]),
        ([1,-2,-2,1,-1], [-2,-2]),
        ]
for asteroids, expect in data:
    print(f'{asteroids}')
    real = s.asteroidCollision(asteroids)
    print(f'\texpect {expect} real {real} result {expect == real}')
