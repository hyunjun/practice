#   https://leetcode.com/problems/letter-case-permutation


from typing import List


class Solution:
    #   runtime; 104ms
    def letterCasePermutation0(self, S):
        if S is None or 0 == len(S):
            return ['']
        res = [S]
        for i in range(len(S)):
            if '0' <= S[i] <= '9':
                continue
            j = len(res)
            while j:
                s = res[j - 1]
                if 'a' <= s[i] <= 'z':
                    res.append(s[:i] + chr(ord(s[i]) - (ord('a') - ord('A'))) + s[i + 1:])
                elif 'A' <= s[i] <= 'Z':
                    res.append(s[:i] + chr(ord(s[i]) + (ord('a') - ord('A'))) + s[i + 1:])
                j -= 1
        return res

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642
    #   runtime; 68ms, 32.24%
    #   memory; 15.3MB, 36.80%
    def letterCasePermutation(self, S: str) -> List[str]:
        queue, result = [(S, 0)], []
        while queue:
            s, idx = queue.pop(0)
            if idx >= len(s):
                result.append(s)
                continue
            while idx < len(s) and '0' <= s[idx] <= '9':
                idx += 1
            queue.append((s, idx + 1))
            if idx < len(s):
                if 'a' <= s[idx] <= 'z':
                    queue.append((s[:idx] + s[idx].upper() + s[idx + 1:], idx + 1))
                elif 'A' <= s[idx] <= 'Z':
                    queue.append((s[:idx] + s[idx].lower() + s[idx + 1:], idx + 1))
        return result


s = Solution()
data = [("a1b2", ["a1b2","a1B2","A1b2","A1B2"]),
        ("3z4", ["3z4","3Z4"]),
        ("12345", ["12345"]),
        ("0", ["0"]),
        ]
for S, expect in data:
    real = s.letterCasePermutation(S)
    print(f'{S} expect {expect} real {real} result {expect == real}')
