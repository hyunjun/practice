#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5698217712812032


from collections import defaultdict


def longest_substring_with_k_distinct(s, k):
    if s is None or 0 == len(s):
        return 0

    i, substr, maxLen = 0, defaultdict(int), -float('inf')
    for j, c in enumerate(s):
        substr[c] += 1
        while k < len([c for c, cnt in substr.items() if 0 < cnt]):
            substr[s[i]] -= 1
            i += 1
        maxLen = max(maxLen, j - i + 1)
    return maxLen


data = [('araaci', 2, 4), # araa
        ('araaci', 1, 2), # aa
        ('cbbebi', 3, 5), # cbbeb, bbebi
        ]
for s, k, expected in data:
    real = longest_substring_with_k_distinct(s, k)
    print('{}, {}, expected {}, real {}, result {}'.format(s, k, expected, real, expected == real))
