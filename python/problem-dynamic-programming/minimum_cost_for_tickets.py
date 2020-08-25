#   https://leetcode.com/problems/minimum-cost-for-tickets

#   https://leetcode.com/problems/minimum-cost-for-tickets/solution


from typing import List


class Solution:
    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3436
    #   runtime; 64ms, 34.48%
    #   memory; 14.1MB, 27.26%
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costDays, dp = [1, 7, 30], [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        for j in range(1, len(dp)):
            if j not in days:
                dp[j] = dp[j - 1]
                continue
            for i, cost in enumerate(costs):
                if 0 < j - costDays[i]:
                    dp[j] = min(dp[j], dp[j - costDays[i]] + cost)
                else:
                    dp[j] = min(dp[j], dp[0] + cost)
        return dp[-1]


s = Solution()
data = [([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 4, 6, 7, 8, 20], [7, 2, 15], 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
        ([1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45], 44),
        ([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99], [9,38,134], 423),
        ]
for days, costs, expect in data:
    real = s.mincostTickets(days, costs)
    print(f'{days} {costs} expect {expect} real {real} result {expect == real}')
