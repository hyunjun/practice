#   https://leetcode.com/problems/delete-operation-for-two-strings

#   https://leetcode.com/problems/delete-operation-for-two-strings/solution
#   https://www.youtube.com/watch?v=10WnvBk9sZc


from collections import defaultdict


class Solution:
    #   runtime; 544ms, 5.18%
    #   memory; 40MB, 6.11%
    def minDistance0(self, word1, word2):
        if (word1 is None or 0 == len(word1)) and (word2 is None or 0 == len(word2)):
            return 0
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)

        d = defaultdict(int)
        def count(w1, w2):
            if 0 == len(w1):
                return len(w2)
            if 0 == len(w2):
                return len(w1)
            if (w1, w2) in d:
                return d[(w1, w2)]
            if w1[0] == w2[0]:
                cnt = count(w1[1:], w2[1:])
            else:
                lCnt, rCnt = 1 + count(w1[1:], w2), 1 + count(w1, w2[1:])
                cnt = min(lCnt, rCnt)
            d[(w1, w2)] = cnt
            return cnt

        return count(word1, word2)

    #   runtime; 272ms, 90.36%
    #   memory; 15MB, 74.73%
    def minDistance(self, word1, word2):
        if (word1 is None or 0 == len(word1)) and (word2 is None or 0 == len(word2)):
            return 0
        if word1 is None or 0 == len(word1):
            return len(word2)
        if word2 is None or 0 == len(word2):
            return len(word1)

        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


s = Solution()
data = [('sea', 'eat', 2),
        ('sloeaq', 'soeq', 2),
        ('question', 'astique', 9),
        ("dinitrophenylhydrazine", "acetylphenylhydrazine", 11),
        ]
for word1, word2, expected in data:
    real = s.minDistance(word1, word2)
    print('{}, {}, expected {}, real {}, result {}'.format(word1, word2, expected, real, expected == real))
