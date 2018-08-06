#   https://leetcode.com/problems/unique-morse-code-words

#   https://leetcode.com/problems/unique-morse-code-words/solution


class Solution:
    morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    #   11.26%
    def uniqueMorseRepresentations(self, words):
        s = set()
        [s.add(''.join([Solution.morseCodes[ord(c) - ord('a')] for c in word])) for word in words]
        return len(s)


s = Solution()
data = [(['gin', 'zen', 'gig', 'msg'], 2),
        ]
for words, expected in data:
    real = s.uniqueMorseRepresentations(words)
    print('{}, expected {}, real {}, result {}'.format(words, expected, real, expected == real))
