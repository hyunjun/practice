#   https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards


from typing import List


class Solution:
    def maxScore0(self, cardPoints: List[int], k: int) -> int:
        if cardPoints is None or not (1 <= len(cardPoints) <= 10 ** 5) or not (1 <= k <= len(cardPoints)):
            return 0

        if len(cardPoints) == k:
            return sum(cardPoints)

        def add(acc, arr, cnt):
            if cnt == 0:
                return acc
            else:
                return max(add(acc + arr[0], arr[1:], cnt - 1), add(acc + arr[-1], arr[:-1], cnt - 1))

        return add(0, cardPoints, k)

    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        if cardPoints is None or not (1 <= len(cardPoints) <= 10 ** 5) or not (1 <= k <= len(cardPoints)):
            return 0

        if len(cardPoints) == k:
            return sum(cardPoints)

        score = 0
        for l in range(k, -1, -1):
            r = k - l
            score = max(score, sum(cardPoints[:l]) + sum(cardPoints[len(cardPoints) - r:]))
        return score

    #   runtime; 564ms, 25.00%
    #   memory; 27.1MB, 100.00%
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if cardPoints is None or not (1 <= len(cardPoints) <= 10 ** 5) or not (1 <= k <= len(cardPoints)):
            return 0

        totalLen = len(cardPoints)
        if totalLen == k:
            return sum(cardPoints)

        sumL, sumR = sum(cardPoints[:k]), 0
        r = totalLen - 1
        score = sumL + sumR
        for l in range(k - 1, -1, -1):
            sumL -= cardPoints[l]
            sumR += cardPoints[r]
            score = max(score, sumL + sumR)
            r -= 1
        return score


s = Solution()
data = [([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([1, 1000, 1], 1, 1),
        ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202),
        ]
for cardPoints, k, expected in data:
    real = s.maxScore(cardPoints, k)
    print(f'{cardPoints} {k} expected {expected} real {real} result {expected == real}')
