#   https://leetcode.com/problems/reverse-vowels-of-a-string
#   26.84%


class Solution:

    def reverseVowels(self, s):
        if s is None or 0 == len(s):
            return s
        l, r = 0, len(s) - 1
        vowels, sList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], list(s)
        while l < r:
            while l < r and not (sList[l] in vowels):
                l += 1
            while l < r and not (sList[r] in vowels):
                r -= 1
            print('l idx {}, {}, r idx {}, {}'.format(l, sList[l], r, sList[r]))
            if sList[l] in vowels and sList[r] in vowels and sList[l] != sList[r]:
                sList[l], sList[r] = sList[r], sList[l]
            l += 1
            r -= 1
        return ''.join(sList)


solution = Solution()
data = [('hello', 'holle'),
        ('leetcode', 'leotcede'),
        ('a.', 'a.'),
        ('aA', 'Aa'),
        (' apG0i4maAs::sA0m4i0Gp0', ' ipG0A4mAas::si0m4a0Gp0')
        ]
for s, expected in data:
    real = solution.reverseVowels(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
