#   https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters


from typing import List


class Solution:
    #   runtime; 184ms, 22.62%
    #   memory; 12.7MB, 100.00%
    def maxLength(self, arr: List[str]) -> int:
        if arr is None or 0 == len(arr):
            return 0

        arr = [a for a in arr if len(set(a)) == len(a)]
        if 0 == len(arr):
            return 0

        def hasCommonChar(accSet, word):
            return 0 < len(accSet.intersection(set(word)))

        def getMaxUniqConcat(acc, words):
            accStr = ''.join(a for a in acc)
            curLen, accSet = len(accStr), set(accStr)
            for i, word in enumerate(words):
                if hasCommonChar(accSet, word):
                    continue
                acc.append(word)
                curLen = max(curLen, getMaxUniqConcat(acc, words[i + 1:]))
                acc.pop()
            return curLen

        return getMaxUniqConcat([], arr)


s = Solution()
data = [(["un","iq","ue"], 4),
        (["cha","r","act","ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
        (["yy","bkhwmpbiisbldzknpm"], 0),
        ]
for arr, expected in data:
    real = s.maxLength(arr)
    print(f'{arr}, expected {expected}, real {real}, result {expected == real}')
