#   https://leetcode.com/problems/implement-magic-dictionary

#   https://leetcode.com/problems/implement-magic-dictionary/solution


from collections import defaultdict

#   runtime; 28ms, 34.11%
#   memory; 10.9MB, 33.33%
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.orgD, self.oneDiffD = defaultdict(set), defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        #   time; O(len(dict) * len(word))
        for word in dict:
            key = len(word)
            self.orgD[key].add(word)
            for i in range(key):
                self.oneDiffD[key].add(word[:i] + '*' + word[i + 1:])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        key = len(word)
        #   time; o(len(word) * len(word))
        if word in self.orgD[key]:
            for w in self.orgD[key]:
                if w == word:
                    continue
                for i in range(key):
                    if word[:i] + '*' + word[i + 1:] == w[:i] + '*' + w[i + 1:]:
                        return True
            return False
        #   time; O(len(word))
        for i in range(key):
            if word[:i] + '*' + word[i + 1:] in self.oneDiffD[key]:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(['hello', 'leetcode'])
for word, expected in [('hello', False), ('hhllo', True), ('hell', False), ('leetcoded', False)]:
    real = obj.search(word)
    print('{}, expected {}, real {}, result {}'.format(word, expected, real, expected == real))
print()
obj = MagicDictionary()
obj.buildDict(['hello', 'hallo', 'leetcode'])
for word, expected in [('hello', True), ('hhllo', True), ('hell', False), ('leetcoded', False)]:
    real = obj.search(word)
    print('{}, expected {}, real {}, result {}'.format(word, expected, real, expected == real))
