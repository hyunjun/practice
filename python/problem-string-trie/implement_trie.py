#   https://leetcode.com/problems/implement-trie-prefix-tree


from collections import defaultdict


INF_DICT = lambda: defaultdict(INF_DICT)


#   91.98%
class Trie0

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


#   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329
#   runtime; 132ms, 91.79%
#   memory; 27.2MB
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['$'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c in t:
                t = t[c]
            else:
                return False
        return '$' in t and t['$'] == True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c in t:
                t = t[c]
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
