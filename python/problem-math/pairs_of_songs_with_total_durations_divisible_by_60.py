#   https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

#   https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution


from collections import Counter
from typing import List


class Solution:
    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559
    #   runtime; 248ms, 15.97%
    #   memory; 18.8MB
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        time.sort()
        start, end = time[0] + time[1], time[-2] + time[-1]
        while start % 60 != 0:
            start += 1
        while end % 60 != 0:
            end -= 1
        res, c, sixties, checked = 0, Counter(time), [n for n in range(start, end + 1, 60)], set()
        for t, cnt in c.items():
            for s in sixties:
                if t > s:
                    continue
                target = s - t
                if target in c and (t, target) not in checked and (target, t) not in checked:
                    if target == t and cnt > 1:
                        res += cnt * (cnt - 1) // 2
                    elif target != t:
                        res += cnt * c[target]
                    checked.add((t, target))
                    checked.add((target, t))
        return res


s = Solution()
data = [([60], 0),
        ([30,20,150,100,40], 3),
        ([60,60,60], 3),
        ([15,63,451,213,37,209,343,319], 1),
        ]
for time, expect in data:
    real = s.numPairsDivisibleBy60(time)
    print(f'{time} expect {expect} real {real} result {expect == real}')
'''
1. sort
2. min range = [0] + [1], max range [-2] + [-1]
3. get 60 divisible nums in range
4. check
'''
