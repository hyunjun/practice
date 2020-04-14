#   http://www.geeksforgeeks.org/trie-insert-and-search/


class Trie0:
    def __init__(self):
        self.root = {}

    def str2trie(self, strs):
        for s in strs:
            cur = self.root
            for ch in s:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['$'] = True

    def search(self, s):
        cur = self.root
        for ch in s:
            if ch not in cur:
                return False
            cur = cur[ch]
        return '$' in cur


class Trie1:
    def __init__(self):
        self.trie = {}

    def add(self, word):
        cur = self.trie
        for w in word:
            cur = cur.setdefault(w, {})
        cur['$'] = True

    def search(self, word):
        cur = self.trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return '$' in cur


from collections import defaultdict


class Trie2:
    def __init__(self):
        INF_DICT = lambda: defaultdict(INF_DICT)
        self.trie = INF_DICT()

    def add(self, word):
        n = self.trie
        for c in word:
            n = n[c]
        n['$'] = True

    def search(self, word):
        n = self.trie
        for c in word:
            if c not in n:
                return False
            n = n[c]
        return '$' in n


strs = ['bye', 'any', 'answer', 'there', 'their', 'the']
trie0 = Trie0()
trie0.str2trie(strs)

trie1 = Trie1()
for s in strs:
    trie1.add(s)

trie2 = Trie2()
for s in strs:
    trie2.add(s)


for s in strs:
    print(s, trie0.search(s), trie1.search(s), trie2.search(s))
print()
for word in ['by', 'the', 'and']:
    print(word, trie0.search(word), trie1.search(word), trie2.search(word))
