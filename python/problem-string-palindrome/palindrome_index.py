#   https://www.hackerrank.com/challenges/palindrome-index
#   https://medium.com/@mannycodes/how-to-solve-the-palindrome-index-code-challenge-1754f47dc8dd


from collections import defaultdict


#   Timeout
def palindromeIndex0(s):

    def isPalindrome(_s):
        return _s == _s[::-1]

    if isPalindrome(s):
        return -1

    cntDict, idxDict = defaultdict(int), defaultdict(list)
    for i, c in enumerate(s):
        cntDict[c] += 1
        idxDict[c].append(i)
    for c, cnt in sorted(cntDict.items(), key=lambda t:t[1]):
        for idx in idxDict[c]:
            if isPalindrome(s[:idx] + s[idx + 1:]):
                return idx
    return -1


#   Timeout
def palindromeIndex1(s):

    def isPalindrome(_s):
        return _s == _s[::-1]

    if isPalindrome(s):
        return -1

    for i, c in enumerate(s):
        if isPalindrome(s[:i] + s[i + 1:]):
            return i
    return -1

def palindromeIndex(s):

    def isPalindrome(_s):
        return _s == _s[::-1]

    if isPalindrome(s):
        return -1

    l, r = 0, len(s) - 1
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1
    if isPalindrome(s[:l] + s[l + 1:]):
        return l
    if isPalindrome(s[:r] + s[r + 1:]):
        return r
    return -1


data = [('aaab', 3),
        ('aaaba', 3),
        ('baa', 0),
        ('aaa', -1),
        ]
for s, expected in data:
    real = palindromeIndex(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
