#   https://leetcode.com/problems/bulls-and-cows


from collections import defaultdict


class Solution:
    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455
    #   runtime; 44ms, 63.74%
    #   memory; 13.8MB, 62.57%
    def getHint(self, secret: str, guess: str) -> str:
        bullSet = set([i for i, s in enumerate(secret) if s == guess[i]])
        secretDict = defaultdict(list)
        for i, s in enumerate(secret):
            if i in bullSet:
                continue
            secretDict[s].append(i)
        guessDict = defaultdict(list)
        for i, g in enumerate(guess):
            if i in bullSet:
                continue
            guessDict[g].append(i)
        cow = sum([min(len(idxList), len(guessDict[s])) for s, idxList in secretDict.items()])
        return f'{len(bullSet)}A{cow}B'


s = Solution()
data = [('1807', '7810', '1A3B'),
        ('1123', '0111', '1A1B'),
        ]
for secret, guess, expect in data:
    real = s.getHint(secret, guess)
    print(f'{secret} {guess} expect {expect} real {real} result {expect == real}')
