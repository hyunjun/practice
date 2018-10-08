#   https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards

#   https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solution


class Solution:
    #   32.04%
    def hasGroupsSizeZ(self, deck):
        if deck is None or len(deck) <= 1:
            return False

        d = {}
        for i in deck:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        counts = d.values()
        if 1 == len(counts):
            return True
        if 1 in counts:
            return False

        minCount = min(counts)
        divisors = [minCount]
        for p in range(2, minCount // 2 + 1):
            if 0 == minCount % p:
                divisors.append(p)

        for c in counts:
            hasDivisor = False
            for d in divisors:
                if 0 == c % d:
                    hasDivisor = True
                    break
            if False == hasDivisor:
                return False
        return True


s = Solution()
data = [([1, 2, 3, 4, 4, 3, 2, 1], True), #  [1,1],[2,2],[3,3],[4,4]
        ([1, 1, 1, 2, 2, 2, 3, 3], False),
        ([1], False),
        ([1, 1], True),
        ([1, 1, 2, 2, 2, 2], True),# [1,1],[2,2],[2,2]
        ([1, 1, 1, 1, 2, 2, 2, 2, 2, 2], True),
        ([0, 0, 0, 0, 0, 1, 1, 2, 3, 4], False),
        ]
for deck, expected in data:
    real = s.hasGroupsSizeZ(deck)
    print('{}, expected {}, real {}, result {}'.format(deck, expected, real, expected == real))
