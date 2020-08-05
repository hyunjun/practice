#   https://leetcode.com/problems/add-and-search-word-data-structure-design


#   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3413
#   runtime; 484ms, 25.50%
#   memory; 24.3MB, 85.71%
class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['$'] = True

    def search(self, word: str) -> bool:
        return self._search(self.trie, word)
    
    def _search(self, trie: dict, word: str) -> bool:
        if trie is True:
            if 0 == len(word):
                return True
            return False
        for i, c in enumerate(word):
            if c == '.':
                for k in trie.keys():
                    if k == '$':
                        continue
                    if self._search(trie[k], word[i + 1:]):
                        return True
            if c not in trie:
                return False
            trie = trie[c]
        return '$' in trie and trie['$'] == True


data = [[('bad', 'dad', 'mad'),
         ('pad', False),
         ('bad', True),
         ('.ad', True),
         ('b..', True),
         ],
        [('a', 'a'),
         ('.', True),
         ('a', True),
         ('aa', False),
         ('a', True),
         ('.a', False),
         ('a.', False),
         ]
        ]
for items in data:
    print()
    w = WordDictionary()
    for i, item in enumerate(items):
        if 0 == i:
            for word in item:
                w.addWord(word)
            continue
        word, expect = item[0], item[1]
        real = w.search(word)
        print(f'{word} expect {expect} real {real} result {expect == real}')
