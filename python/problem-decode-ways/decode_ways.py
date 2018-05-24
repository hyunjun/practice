#   https://leetcode.com/problems/decode-ways

#   https://leetcode.com/problems/decode-ways/discuss/30352/Accpeted-Python-DP-solution

class Solution:
    d = {'0': 0,
         '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1,
         '11': 2, '12': 2, '13': 2, '14': 2, '15': 2, '16': 2, '17': 2, '18': 2, '19': 2, '20': 1,
         '21': 2, '22': 2, '23': 2, '24': 2, '25': 2, '26': 2}

    #   time limit exceeded
    def numDecodingsRecur(self, s):
        if s is None or 0 == len(s) or s[0] == '0':
            return 0
        print(s)
        if s in Solution.d:
            return Solution.d[s]
        cnt = 0
        if '1' <= s[0] <= '9':
            cnt += self.numDecodings(s[1:])
        if '10' <= s[:2] <= '26':
            cnt += self.numDecodings(s[2:])
        return cnt

    #   time limit exceeded
    def numDecodingsIter(self, s):
        if s is None or 0 == len(s) or s[0] == '0':
            return 0
        if s in Solution.d:
            return Solution.d[s]
        totalCnt = 0
        queue = [s]
        while queue:
            cur = queue[0]
            del queue[0]
            if 0 == len(cur):
                totalCnt += 1
                continue
            if '1' <= cur[0] <= '9':
                queue.append(cur[1:])
            if '10' <= cur[:2] <= '26':
                queue.append(cur[2:])
        return totalCnt

    #   91.77% by dynamic programming
    def numDecodings(self, s):
        if s is None or 0 == len(s) or s[0] == '0':
            return 0
        if s in Solution.d:
            return Solution.d[s]
        counts = [0] * len(s)
        if '1' <= s[0] <= '9':
            counts[0] = 1
        if '1' <= s[1] <= '9':
            counts[1] += counts[0]
        if s[0:2] in Solution.d:
            counts[1] += 1
        for i in range(2, len(s)):
            if '1' <= s[i] <= '9':
                counts[i] += counts[i - 1]
            if s[i - 1:i + 1] in Solution.d:
                counts[i] += counts[i - 2]
        return counts[-1]


s = Solution()
cases = [('123', 3),
         ('1226', 5),
         ('1206', 1),
         ('301', 0),
         ('101', 1),
         ('611', 2),
         ('27', 1),
         ('4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948', 589824)
         ]
for msg, expected in cases:
    real = s.numDecodings(msg)
    print('{}\texpected {}\treal {}\tresult {}'.format(msg, expected, real, expected == real))
