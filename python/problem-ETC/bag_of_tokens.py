#   https://leetcode.com/problems/bag-of-tokens

#   https://leetcode.com/problems/bag-of-tokens/solution


from typing import List


class Solution:
    #   Time Limit Exceed
    def bagOfTokensScore0(self, tokens: List[int], P: int) -> int:

        self.maxScore = 0

        def getScore(leftTokens, power, score, isUp):
            self.maxScore = max(self.maxScore, score)
            if isUp:
                for i, token in enumerate(leftTokens):
                    if power >= token:
                        getScore(leftTokens[:i] + leftTokens[i + 1:], power - token, score + 1, True)
                        getScore(leftTokens[:i] + leftTokens[i + 1:], power - token, score + 1, False)
            else:
                for i, token in enumerate(leftTokens):
                    if score > 0:
                        getScore(leftTokens[:i] + leftTokens[i + 1:], power + token, score - 1, True)
                        getScore(leftTokens[:i] + leftTokens[i + 1:], power + token, score - 1, False)

        getScore(tokens, P, 0, True)
        getScore(tokens, P, 0, False)

        return self.maxScore

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3506
    #   runtime; 132ms
    #   memory; 14.2MB
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        tokens.sort()
        while True:
            if sum(tokens) <= P:
                return score + len(tokens)
            if sum(tokens) - max(tokens) <= P:
                return score + len(tokens) - 1
            if P < tokens[0]:
                break
            minToken = tokens.pop(0)
            P -= minToken
            score += 1
            if 0 < len(tokens):
                maxToken = tokens.pop()
                P += maxToken
                score -= 1
        return score


s = Solution()
data = [([100], 50, 0),
        ([100, 200], 150, 1),
        ([100, 200, 300, 400], 200, 2),
        ([52,65,35,88,28,1,4,68,56,95], 94, 5),
        ([90,69,47], 10, 0),
        ]
for tokens, P, expect in data:
    real = s.bagOfTokensScore(tokens, P)
    print(f'{tokens} {P} expect {expect} real {real} result {expect == real}')
'''
if sum(l) < P:
    return len(l)
if sum(l) - max(l) < P:
    return len(l) - 1
if sum(l) - min(l) - max(l) < P + max(l):
    return len(l) - 2
[47 69 90]  10

'''
