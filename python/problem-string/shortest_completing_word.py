#   https://leetcode.com/problems/shortest-completing-word


class Solution:
    #   60.25%
    def shortestCompletingWord(self, licensePlate, words):
        plateDict = {}
        for c in licensePlate.lower():
            if not c.isalpha():
                continue
            if c in plateDict:
                plateDict[c] += 1
            else:
                plateDict[c] = 1

        def hasAllChars(pDict, w):
            wDict = {}
            for c in w:
                if c in wDict:
                    wDict[c] += 1
                else:
                    wDict[c] = 1
            print(pDict, wDict)
            for k, v in wDict.items():
                if k in pDict and pDict[k] <= v:
                    pDict[k] = 0
            cnt = set(pDict.values())
            if 1 == len(cnt) and 0 == list(cnt)[0]:
                return True
            print(cnt, len(cnt), list(cnt)[0])
            return False

        minLen, minIdx = 20, -1
        for i, word in enumerate(words):
            if hasAllChars(plateDict.copy(), word):
                if len(word) < minLen:
                    minLen, minIdx = len(word), i
        return words[minIdx]


s = Solution()
data = [("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),
        ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
        ("GrC8950", ["measure","other","every","base","according","level","meeting","none","marriage","rest"], "according"),
        ]
for licensePlate, words, expected in data:
    real = s.shortestCompletingWord(licensePlate, words)
    print('{}, {}, expected {}, real {}, result {}'.format(licensePlate, words, expected, real, expected == real))
