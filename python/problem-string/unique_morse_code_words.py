#   https://leetcode.com/problems/unique-morse-code-words

#   https://leetcode.com/problems/unique-morse-code-words/solution


from typing import List


class Solution:
    morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    #   runtime; 48ms, 11.26%
    def uniqueMorseRepresentations0(self, words):
        s = set()
        [s.add(''.join([Solution.morseCodes[ord(c) - ord('a')] for c in word])) for word in words]
        return len(s)

    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3540
    #   runtime; 36ms, 51.88%
    #   memory; 14.2MB
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformed, morseCodes = set(), [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            transformed.add(''.join(morseCodes[ord(c) - ord('a')] for c in word))
        return len(transformed)


s = Solution()
data = [(['gin', 'zen', 'gig', 'msg'], 2),
        ]
for words, expected in data:
    real = s.uniqueMorseRepresentations(words)
    print('{}, expected {}, real {}, result {}'.format(words, expected, real, expected == real))
