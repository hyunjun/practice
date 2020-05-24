#   https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length


class Solution:
    #   runtime; 256ms, 33.33%
    #   memory; 14.8MB, 100.00%
    def maxVowels(self, s: str, k: int) -> int:
        if s is None or not (1 <= len(s) <= 10 ** 5) or k is None or not (1 <= k <= len(s)):
            return 0
        d, cnt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}, 0
        for i in range(k):
            if s[i] in d.keys():
                d[s[i]] += 1
                cnt += 1
        if cnt == k:
            return cnt
        maxCnt = cnt
        for i in range(k, len(s)):
            if s[i - k] in d.keys():
                d[s[i - k]] -= 1
                cnt -= 1
            if s[i] in d.keys():
                d[s[i]] += 1
                cnt += 1
            if cnt == k:
                return cnt
            maxCnt = max(maxCnt, cnt)
        return maxCnt


solution = Solution()
data = [("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("rhythms", 4, 0),
        ("tryhard", 4, 1),
        ]
for s, k, expect in data:
    real = solution.maxVowels(s, k)
    print(f'{s} {k} expect {expect} real {real} result {expect == real}')
