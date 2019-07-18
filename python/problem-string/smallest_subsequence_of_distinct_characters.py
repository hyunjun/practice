#   https://leetcode.com/problems/smallest-subsequence-of-distinct-characters

#   https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/312599/Python3-concise-solution-with-stack-beats-95


from collections import defaultdict


class Solution:
    #   Wrong Answer
    def smallestSubsequence0(self, text: str) -> str:
        if text is None or 0 == len(text):
            return ''
        if 1 == len(text):
            return text

        charIndicesDict = defaultdict(list)
        for i, c in enumerate(text):
            if 0 < len(charIndicesDict[c]) and charIndicesDict[c][-1] + 1 == i:
                charIndicesDict[c].pop()
            charIndicesDict[c].append(i)
        fRes, bRes = [None] * len(text), [None] * len(text)
        for c, indices in charIndicesDict.copy().items():
            if 1 == len(indices):
                fRes[indices[0]] = c
                bRes[indices[0]] = c
                del charIndicesDict[c]
        for c, indices in sorted(charIndicesDict.items()):
            minStr = fRes[:]
            minStr[indices[0]] = c
            for i in range(1, len(indices)):
                tmp = fRes[:]
                tmp[indices[i]] = c
                if ''.join(t for t in tmp if t) < ''.join(m for m in minStr if m):
                    minStr = tmp
            fRes = minStr
        for c, indices in sorted(charIndicesDict.items(), reverse=True):
            minStr = bRes[:]
            minStr[indices[-1]] = c
            for i in range(len(indices) - 2, -1, -1):
                tmp = bRes[:]
                tmp[indices[i]] = c
                if ''.join(t for t in tmp if t) < ''.join(m for m in minStr if m):
                    minStr = tmp
            bRes = minStr

        fRes, bRes = ''.join(r for r in fRes if r), ''.join(r for r in bRes if r)
        if fRes < bRes:
            return fRes
        return bRes

    #   Wrong Answer
    def smallestSubsequence1(self, text: str) -> str:
        if text is None or 0 == len(text):
            return ''
        if 1 == len(text):
            return text
        p, n = [], []
        for c in text:
            if 0 == len(p) or c not in p:
                p.append(c)
            else:
                if p[-1] == c:
                    continue
                n = p[:]
                n.pop(n.index(c))
                n.append(c)
                if ''.join(n) < ''.join(p):
                    p = n
                n = []
        return ''.join(p)

    #   runtime; 36ms, 83.38%
    #   memory; 13MB, 100.00%
    def smallestSubsequence(self, text: str) -> str:
        if text is None or 0 == len(text):
            return ''
        if 1 == len(text):
            return text
        d = defaultdict(int)
        for i, c in enumerate(text):
            d[c] = i
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and d[stack[-1]] > i:
                stack.pop()
            if c not in stack:
                stack.append(c)
        return ''.join(stack)


s = Solution()
data = [('cdadabcc', 'adbc'),
        ('abcd', 'abcd'),
        ('ecbacba', 'eacb'),
        ('leetcode', 'letcod'),
        ('a', 'a'),
        ('bcbcbcababa', 'bca'),
        ("degbgjchgibedhgcdicccdhjjcegicgjejfbhijedbafgjigff", "bcdefhagji"),
        ]
for text, expected in data:
    real = s.smallestSubsequence(text)
    print(f'{text}, expected {expected}, real {real}, result {expected == real}')
