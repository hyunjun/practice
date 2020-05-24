#   https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if sentence is None or not (1 <= len(sentence) <= 100) or searchWord is None or not (1 <= len(searchWord) <= 10):
            return -1
        swLen = len(searchWord)
        for i, word in enumerate(sentence.split(' ')):
            if searchWord == word[:swLen]:
                return i + 1
        return -1


s = Solution()
data = [("i love eating burger", "burg", 4),
        ("this problem is an easy problem", "pro", 2),
        ("i am tired", "you", -1),
        ("i use triple pillow", "pill", 4),
        ("hello from the other side", "they", -1),
        ]
for sentence, searchWord, expect in data:
    real = s.isPrefixOfWord(sentence, searchWord)
    print(f'{sentence} {searchWord} expect {expect} real {real} result {expect == real}')
