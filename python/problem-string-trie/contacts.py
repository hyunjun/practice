#   https://www.hackerrank.com/challenges/contacts


from collections import defaultdict

#   Timeout 8/11 test cases
class Trie0:
    def __init__(self):
        T = lambda: defaultdict(T)
        self.t = T()

    def add(self, word):
        #reduce(dict.__getitem__, self.t, word)['$'] = True
        trie = self.t
        for c in word:
            trie = trie[c]
        trie['$'] = True
        #print(self.t)

    def find(self, word):
        trie = self.t
        for c in word:
            if c not in trie:
                return 0
            trie = trie[c]
        q, cnt = [trie], 0
        while q:
            t = q.pop(0)
            for k, v in t.items():
                #print(k, v)
                if '$' == k:
                    cnt += 1
                if isinstance(v, dict):
                    q.append(v)
        return cnt


#   Timeout 8/11 test cases
class Trie1:
    def __init__(self):
        T = lambda: defaultdict(T)
        self.t = T()

    def add(self, word):
        #reduce(dict.__getitem__, self.t, word)['$'] = True
        trie = self.t
        for c in word:
            trie = trie[c]
        trie = trie['$']
        #print(self.t)

    def find(self, word):
        trie = self.t
        for c in word:
            if c not in trie:
                return 0
            trie = trie[c]
        q, cnt = [trie], 0
        while q:
            t = q.pop(0)
            if '$' in t:
                cnt += 1
            for v in t.values():
                #print(k, v)
                q.append(v)
        return cnt


class Trie:
    def __init__(self):
        T = lambda: defaultdict(T)
        self.t = T()
        self.d = defaultdict(int)

    def add(self, word):
        #reduce(dict.__getitem__, self.t, word)['$'] = True
        trie = self.t
        for i, c in enumerate(word):
            self.d[word[:i + 1]] += 1
            trie = trie[c]
        trie = trie['$']
        #print(self.t)
        #print(self.d)

    def find(self, word):
        return self.d[word]


def contacts(queries):
    trie, res = Trie(), []
    for cmd, param in queries:
        if cmd == 'add':
            trie.add(param)
        elif cmd == 'find':
            res.append(trie.find(param))
    return res


data = [([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']], [2, 0]),
        ([['add', 's'], ['add', 'ss'], ['add', 'sss'], ['add', 'ssss'], ['add', 'sssss'], ['find', 's'], ['find', 'ss'], ['find', 'sss'], ['find', 'ssss'], ['find', 'sssss'], ['find', 'ssssss']], [5, 4, 3, 2, 1, 0]),
        ([['add', 'eouecvksgllpvfxfvndu'], ['find', 'zivh'], ['add', 'uugxgcrtujxzyjysqrhu'], ['find', 'of'], ['add', 'ryhlozedmgzcmjdfjhte'], ['find', 'uqaqv'], ['add', 'ibfzenldsdltkjbbsccq'], ['find', 'bmcop'], ['add', 'vvxwlttswneoosvgfezt'], ['find', 've'], ['add', 'qimoqjtjypqupwwrueew'], ['find', 'ccyc'], ['add', 'nkaetboylnjbxxvhzupk'], ['find', 'lre'], ['add', 'rdzddgjryupsyhhbjtmx'], ['find', 'hhn'], ['add', 'kudnlccqbvkizsfdbwxy'], ['find', 'yyr'], ['add', 'jgahjespbkxxeqnzwpjr'], ['find', 'grbhb'], ['add', 'pxmfimxotqanodwuuymt'], ['find', 'jll'], ['add', 'xyqempeevmdgwqxlbebd'], ['find', 'lkhd'], ['add', 'omjehsuaphqktuflmxib'], ['find', 'a'], ['add', 'cgdlbhaoxbtreiiovzva'], ['find', 'cy'], ['add', 'vnrbpfrouudmbndecxxb'], ['find', 'hwaxg'], ['add', 'gvcctdvzeivycyyqlxsp'], ['find', 'adgx'], ['add', 'qkqfnxgpaocdvqvqfvnl'], ['find', 'p']], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
        ]
for queries, expected in data:
    real = contacts(queries)
    if len(queries) < 10:
        print('{}, expected {}, real {}, result {}'.format(queries, expected, real, expected == real))
    else:
        print('{}..., expected {}, real {}, result {}'.format(queries[:10], expected, real, expected == real))
'''

N, queries = int(input()), []
for i in range(N):
    queries.append(input().strip().split(' '))
res = contacts(queries)
print('\n'.join([str(r) for r in res]))
'''
