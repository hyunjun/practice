#   https://leetcode.com/problems/find-all-anagrams-in-a-string

#   https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/132699/Beat-99.06-Python3


from collections import Counter
from copy import copy
from typing import List


class Solution:
    def checkAnagramAndIdx(self, d, s):
        for i, c in enumerate(s):
            if c in d:
                d[c] -= 1
            else:
                return False, i
        return all([i == 0 for i in d.values()]), 0

    #   Time Limit Exceeded
    def findAnagrams0(self, s, p):
        if (s and p is None) or (s is None and p) or len(s) < len(p):
            return []
        d = {}
        for c in p:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        pLen, result = len(p), []
        i = 0
        while i < len(s) - pLen + 1:
            isAnagram, moveIdx = self.checkAnagramAndIdx(copy(d), s[i:i + len(p)])
            if isAnagram:
                result.append(i)
            i += 1 + moveIdx
        return result

    def isAnagram(self, sCounts, pCounts):
        for i in range(26):
            if sCounts[i] != pCounts[i]:
                return False
        return True

    #   65.03%
    def findAnagrams1(self, s, p):
        if (s and p is None) or (s is None and p) or len(s) < len(p):
            return []
        result, sCounts, pCounts = [], [0] * 26, [0] * 26
        sLen, pLen = len(s), len(p)
        for c in p:
            pCounts[ord(c) - 97] += 1
        for i in range(pLen - 1):
            sCounts[ord(s[i]) - 97] += 1
        i = 0
        while i < sLen - pLen + 1:
            addIdx = i + pLen - 1
            if 0 == pCounts[ord(s[addIdx]) - 97]:
                sCounts = [0] * 26
                for j in range(addIdx + 1, addIdx + pLen):
                    if sLen <= j:
                        break
                    sCounts[ord(s[j]) - 97] += 1
                i = addIdx + 1
                continue
            sCounts[ord(s[addIdx]) - 97] += 1
            if self.isAnagram(sCounts, pCounts):
                result.append(i)
            sCounts[ord(s[i]) - 97] -= 1
            i += 1
        return result

    #   https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332
    #   runtime; 7468ms, 9.26%
    #   memory; 15MB
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        if s is None or not (0 <= len(s) <= 20100) or p is None or not (0 < len(p) <= 20100):
            if s is not None and 0 == len(s) and p is not None:
                return [i for i in range(len(p))]
            return []
        pLen, pCounter, res = len(p), Counter(p), []
        for i, c in enumerate(s):
            if c not in pCounter.keys() or i - pLen < -1:
                continue
            cCounter = Counter(s[i - pLen + 1:i + 1])
            if cCounter == pCounter:
                res.append(i - pLen + 1)
        return res

    #   runtime; 5076ms, 14.34%
    #   memory; 14.6MB
    def findAnagrams3(self, s: str, p: str) -> List[int]:
        if s is None or not (0 <= len(s) <= 20100) or p is None or not (0 < len(p) <= 20100):
            if s is not None and 0 == len(s) and p is not None:
                return [i for i in range(len(p))]
            return []
        pLen, pCounter, res = len(p), Counter(p), []
        sLen, sCounter = len(s), Counter()
        i = 0
        while i < sLen - pLen + 1:
            if s[i] in pCounter.keys():
                if Counter(s[i:i + pLen]) == pCounter:
                    res.append(i)
                if i + pLen < sLen and s[i + pLen] in pCounter.keys():
                    i += 1
                else:
                    i += pLen
            else:
                i += 1
        return res


solution = Solution()
data = [('cbaebabacd', 'abc', [0, 6]),
        ('abab', 'ab', [0, 1, 2]),
        ("qhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgyqhievofjucdnmbpxazrlktwsgy", "qhie", [0, 26, 52, 78, 104, 130, 156, 182, 208, 234, 260, 286, 312, 338, 364, 390, 416, 442, 468, 494, 520, 546, 572, 598, 624, 650, 676, 702, 728, 754, 780, 806, 832, 858, 884, 910, 936, 962, 988, 1014, 1040, 1066, 1092, 1118, 1144, 1170, 1196, 1222, 1248, 1274, 1300, 1326, 1352, 1378, 1404, 1430, 1456, 1482, 1508, 1534, 1560, 1586, 1612, 1638, 1664, 1690, 1716, 1742, 1768, 1794, 1820, 1846, 1872, 1898, 1924, 1950, 1976, 2002, 2028, 2054, 2080, 2106, 2132, 2158, 2184, 2210, 2236, 2262, 2288, 2314, 2340, 2366, 2392, 2418, 2444, 2470, 2496, 2522, 2548, 2574, 2600, 2626, 2652, 2678, 2704, 2730, 2756, 2782, 2808, 2834, 2860, 2886, 2912, 2938, 2964, 2990, 3016, 3042, 3068, 3094, 3120, 3146, 3172, 3198, 3224, 3250, 3276, 3302, 3328, 3354, 3380, 3406, 3432, 3458, 3484, 3510, 3536, 3562, 3588, 3614, 3640, 3666, 3692, 3718, 3744, 3770, 3796, 3822, 3848, 3874, 3900, 3926, 3952, 3978, 4004, 4030, 4056, 4082, 4108, 4134, 4160, 4186, 4212, 4238, 4264, 4290, 4316, 4342, 4368, 4394, 4420, 4446, 4472, 4498, 4524, 4550, 4576, 4602, 4628, 4654, 4680, 4706, 4732, 4758, 4784, 4810, 4836, 4862, 4888, 4914, 4940, 4966, 4992, 5018, 5044, 5070, 5096, 5122, 5148, 5174, 5200, 5226, 5252, 5278, 5304, 5330, 5356, 5382, 5408, 5434, 5460, 5486, 5512, 5538, 5564, 5590, 5616, 5642, 5668, 5694, 5720, 5746, 5772, 5798, 5824, 5850, 5876, 5902, 5928, 5954, 5980, 6006, 6032, 6058, 6084, 6110, 6136, 6162, 6188, 6214, 6240, 6266, 6292, 6318, 6344, 6370, 6396, 6422, 6448, 6474, 6500, 6526, 6552, 6578, 6604, 6630, 6656, 6682, 6708, 6734, 6760, 6786, 6812, 6838, 6864, 6890, 6916, 6942, 6968, 6994, 7020, 7046, 7072, 7098, 7124, 7150, 7176, 7202, 7228, 7254, 7280, 7306, 7332, 7358, 7384, 7410, 7436, 7462, 7488, 7514, 7540, 7566, 7592, 7618, 7644, 7670, 7696, 7722, 7748, 7774])
        ]
for s, p, expected in data:
    real = solution.findAnagrams(s, p)
    if len(s) < 20 and len(p) < 20:
        print('{}, {}, expected {}, real {}, result {}'.format(s, p, expected, real, expected == real))
    else:
        print('expected {}, real {}, result {}'.format(expected, real, expected == real))
