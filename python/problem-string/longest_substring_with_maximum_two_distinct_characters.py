#   https://codebasil.com/problems/longest-substring-with-maximum-two-distinct-characters


from collections import defaultdict

def longestSubstringWithMaximumTwoDistinctCharacters(s):
    if s is None or 0 == len(s):
        return 0
    sIdx, contains, d, maxLen = 0, set(), defaultdict(int), 0
    for i, c in enumerate(s):
        contains.add(c)
        d[c] += 1
        while sIdx < i and len(contains) > 2:
            d[s[sIdx]] -= 1
            if d[s[sIdx]] == 0:
                contains.remove(s[sIdx])
            sIdx += 1
        maxLen = max(maxLen, sum(d[ch] for ch in contains))
    return maxLen


data = [('abcabbac', 4),
        ('ababaa', 6),
        ]
for s, expected in data:
    real = longestSubstringWithMaximumTwoDistinctCharacters(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
