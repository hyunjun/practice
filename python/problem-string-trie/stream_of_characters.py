#   https://leetcode.com/problems/stream-of-characters


from typing import List


#   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3434
#   runtime; 1176ms, 43.57%
#   memory; 37.9MB, 59.81%
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie, self.accumulated, self.wordSet, self.maxDepth = {}, [], set(), 0
        for w in words:
            self.insert(w[::-1])

    def insert(self, word):
        trie, self.maxDepth = self.trie, max(self.maxDepth, len(word))
        for c in word:
            self.wordSet.add(c)
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['$'] = True

    def search(self, word):
        trie = self.trie
        for c in word:
            if '$' in trie and trie['$']:
                return True
            if c not in trie:
                return False
            trie = trie[c]
        return '$' in trie and trie['$']

    def query(self, letter: str) -> bool:
        if letter not in self.trie and letter not in self.wordSet:
            return False
        self.accumulated.insert(0, letter)
        if self.maxDepth < len(self.accumulated):
            self.accumulated.pop()
        return self.search(''.join(self.accumulated))


data = [(["cd","f","kl"], [('a', False), ('b', False), ('c', False), ('d', True), ('e', False), ('f', True), ('g', False), ('h', False), ('i', False), ('j', False), ('k', False), ('l', True)]),
        (["ab","ba","aaab","abab","baa"],[('a', False),('a', False),('a', False),('a', False),('a', False),('b', True),('a', True),('b', True),('a', True),('b', True),('b', False),('b', False),('a', True),('b', True),('a', True),('b', True),('b', False),('b', False),('b', False),('a', True),('b', True),('a', True),('b', True),('a', True),('a', True),('a', False),('b', True),('a', True),('a', True),("a", False)]),
        ]
for d, checks in data:
    s = StreamChecker(d)
    print(f'{d}')
    for letter, expect in checks:
        real = s.query(letter)
        print(f'\t{letter} expect {expect} real {real} result {expect == real}')
