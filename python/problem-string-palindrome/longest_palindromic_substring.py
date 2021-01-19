#   https://leetcode.com/problems/longest-palindromic-substring

#   https://leetcode.com/problems/longest-palindromic-substring/solution


def is_palindrome(s):
    return s == s[::-1]


#   Time Limit Exceeded
def longest_palindrome0(s):
    max_len, max_str = 1, s[0]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i : j + 1]):
                if max_len < j + 1 - i:
                    max_len = j + 1 - i
                    max_str = s[i : j + 1]
    return max_str


#   32.39%
def longest_palindrome1(s):
    if is_palindrome(s):
        return s

    max_len, max_str, idx_dict = 1, s[0], {}
    for i, c in enumerate(s):
        if c in idx_dict:
            l_idx_list = idx_dict[c]
            for l_idx in l_idx_list:
                if is_palindrome(s[l_idx : i + 1]):
                    if max_len < i + 1 - l_idx:
                        max_len = i + 1 - l_idx
                        max_str = s[l_idx : i + 1]
            l_idx_list.append(i)
            idx_dict[c] = l_idx_list
        else:
            idx_dict[c] = [i]
    return max_str


#   26.89%
def longest_palindrome(s):
    if is_palindrome(s):
        return s

    idx_list_dict = {}
    for i, c in enumerate(s):
        if c in idx_list_dict:
            idx_list_dict[c].append(i)
        else:
            idx_list_dict[c] = [i]

    max_len, max_str = 1, s[0]
    for c, idx_list in idx_list_dict.items():
        idx_list_len = len(idx_list)
        for i in range(0, idx_list_len):
            start_idx = idx_list[i]
            for j in range(idx_list_len - 1, -1, -1):
                end_idx = idx_list[j]
                cand = s[start_idx:end_idx + 1]
                if is_palindrome(cand):
                    if max_len < len(cand):
                        max_len = len(cand)
                        max_str = cand
    return max_str


from collections import defaultdict


class Solution:
    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609
    #   runtime; 3300ms, 30.47%
    #   memory; 14.3MB, 63.00%
    def longestPalindrome0(self, s: str) -> str:
        if s is None or 0 == len(s):
            return ''
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        maxS, maxE = 0, 1
        for c, indices in sorted(d.items(), key=lambda t: -(t[1][-1] - t[1][0])):
            for i, idx in enumerate(indices):
                for j in range(len(indices) - 1, i, -1):
                    cand = s[idx:indices[j] + 1]
                    if cand == cand[::-1] and indices[j] + 1 - idx > maxE - maxS:
                        maxS, maxE = idx, indices[j] + 1
        return s[maxS:maxE]

    #   runtime; 1176ms, 51.10%
    #   memory; 14.4MB, 39.87%
    def longestPalindrome(self, s: str) -> str:
        if s is None or 0 == len(s):
            return ''
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        maxS, maxE = 0, 1
        for c, indices in sorted(d.items(), key=lambda t: -(t[1][-1] - t[1][0])):
            for i, idx in enumerate(indices):
                for j in range(len(indices) - 1, i, -1):
                    if indices[j] + 1 - idx <= maxE - maxS:
                        continue
                    cand = s[idx:indices[j] + 1]
                    if cand == cand[::-1]:
                        maxS, maxE = idx, indices[j] + 1
        return s[maxS:maxE]


solution = Solution()
data = [('babad', 'bab'),
        ('cbbd', 'bb'),
        ('babbd', 'bab'),
        ('bbbad', 'bbb'),
        ('klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc', 'wnsnw'),
        ('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
        ]
for s, expect in data:
    real = solution.longestPalindrome(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
