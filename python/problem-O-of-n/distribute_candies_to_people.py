#   https://leetcode.com/problems/distribute-candies-to-people

#   https://leetcode.com/problems/distribute-candies-to-people/solution


from typing import List


class Solution:
    #   runtime; 36ms, 91.11%
    #   memory; 13.3MB, 100.00%
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        loop, dist = 0, num_people * (num_people + 1) // 2
        while dist <= candies:
            candies -= dist
            loop += 1
            dist += num_people * num_people
        if 0 < loop:
            base = loop * (loop - 1) // 2 * num_people
            res = [base + (i + 1) * loop for i in range(num_people)]
        else:
            res = [0] * num_people
        for i in range(1, num_people + 1):
            cur = i + num_people * loop
            if cur <= candies:
                res[i - 1] += cur
                candies -= cur
            else:
                res[i - 1] += candies
                break
        return res


s = Solution()
data = [(7, 4, [1, 2, 3, 1]),
        (10, 3, [5, 2, 3]),
        (60, 4, [15, 18, 15, 12]),
        (80, 4, [17, 18, 21, 24]),
        ]
for candies, num_people, expected in data:
    real = s.distributeCandies(candies, num_people)
    print(f'{candies}, {num_people}, expected {expected}, real {real}, result {expected == real}')
