#   https://leetcode.com/problems/implement-trie-prefix-tree
#   91.98%

from collections import defaultdict


INF_DICT = lambda: defaultdict(INF_DICT)


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = INF_DICT()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n = self.trie
        for c in word:
            n = n[c]
        n['$'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        n = self.trie
        for c in word:
            if c in n:
                n = n[c]
            else:
                return False
        return '$' in n

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n = self.trie
        for c in prefix:
            if c in n:
                n = n[c]
            else:
                return False
        return True


#  Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('hello')
print(obj.search('hell'))
print(obj.search('helloa'))
print(obj.search('hello'))
print(obj.startsWith('hell'))
print(obj.startsWith('helloa'))
print(obj.startsWith('hello'))
print(obj.trie)
