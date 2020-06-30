#   https://leetcode.com/problems/word-search-ii

#   https://leetcode.com/problems/word-search-ii/discuss/712993/Python-3-Trie-solution-(DFS)


from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.node = defaultdict(dict)

    def insert(self, word):
        node = self.node
        for c in word:
            if c not in node:
                node[c] = defaultdict(dict)
            node = node[c]
        node['*'] = True

    def search(self, word):
        node = self.node
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return '*' in node and node['*']


class Solution:
    #   Time Limit Exceeded
    def findWords0(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        
        def traverse(word, visited, r=-1, c=-1):
            if r == -1 and c == -1:
                for r in range(R):
                    for c in range(C):
                        if board[r][c] == word[0]:
                            visited.add((r, c))
                            if 1 == len(word) or traverse(word[1:], visited, r, c):
                                return True
                            visited.remove((r, c))
            else:
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited:
                        continue
                    if board[nr][nc] == word[0]:
                        visited.add((nr, nc))
                        if 1 == len(word) or traverse(word[1:], visited, nr, nc):
                            return True
                        visited.remove((nr, nc))
            return False
        
        return [word for word in words if traverse(word, set())]

    #   Time Limit Exceeded
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        
        d = {}
        def traverse(word, stack, visited, r, c):
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited:
                    continue
                if board[nr][nc] == word[0]:
                    stack.append(word[0])
                    visited.add((nr, nc))
                    d[''.join(stack)] = (stack[:], visited.copy(), r, c)
                    if 1 == len(word) or traverse(word[1:], stack, visited, nr, nc):
                        return True
                    visited.remove((nr, nc))
                    stack.pop()
            return False
        
        self.res = set()
        for word in words:
            isCached = False
            for i in range(len(word) - 1, 1, -1):
                if word[:i] in d:
                    stack, visited, r, c = d[word[:i]]
                    if traverse(word[i:], stack, visited, r, c):
                        isCached = True
                        self.res.add(word)
                        break
            if isCached:
                continue
            for r in range(R):
                for c in range(C):
                    if board[r][c] == word[0]:
                        if traverse(word[1:], [word[0]], set([(r, c)]), r, c):
                            self.res.add(word)
        return list(self.res)

    #   Time Limit Exceeded
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        
        def traverse(word, i, visited, r, c):
            if i == len(word):
                return True
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if not (0 <= nr < R) or not (0 <= nc < C) or visited[nr][nc]:
                    continue
                if board[nr][nc] == word[i]:
                    visited[nr][nc] = True
                    if traverse(word, i + 1, visited, nr, nc):
                        return True
                    visited[nr][nc] = False
            return False
        
        self.res = set()
        for word in words:
            for r in range(R):
                for c in range(C):
                    if board[r][c] == word[0]:
                        visited = [[False] * C for _ in range(R)]
                        visited[r][c] = True
                        if traverse(word, 1, visited, r, c):
                            self.res.add(word)
                        visited[r][c] = False
        return list(self.res)

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3376
    #   runtime; 272ms, 88.16%
    #   memory; 29MB, 60.87%
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        #for word in words:
        #    print(word, trie.search(word))

        R, C, self.res = len(board), len(board[0]), set()
        
        def traverse(acc, node, visited, r, c):
            if '*' in node and node['*']:
                #print(acc, board[r][c], node['*'])
                self.res.add(''.join(acc))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if not (0 <= nr < R) or not (0 <= nc < C) or visited[nr][nc]:
                    continue
                nextLetter = board[nr][nc]
                if nextLetter in node:
                    visited[nr][nc] = True
                    acc.append(nextLetter)
                    traverse(acc, node[nextLetter], visited, nr, nc)
                    acc.pop()
                    visited[nr][nc] = False
        
        for r in range(R):
            for c in range(C):
                letter = board[r][c]
                if letter in trie.node:
                    #print(board[r][c], trie.node[board[r][c]].keys())
                    visited = [[False] * C for _ in range(R)]
                    visited[r][c] = True
                    traverse([letter], trie.node[letter], visited, r, c)
                    visited[r][c] = False
        return list(self.res)


s = Solution()
board0 = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
board1 = [
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["b","c","d","e"],
    ["f","g","h","i"],
    ["j","k","l","m"],
    ["n","o","p","q"],
    ["r","s","t","u"],
    ["v","w","x","y"],
    ["z","z","z","z"]
]
data = [(board0, ["oath","pea","eat","rain"], ["eat","oath"]),
        ([["a","a"]], ["aaa"], []),
        ([["a","b"],["a","a"]], ["aba","baa","bab","aaab","aaa","aaaa","aaba"], ["aaa","aaab","aaba","aba","baa"]),
        (board1, ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaac"], ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaac"]),
        ]
for board, words, expect in data:
    real = s.findWords(board, words)
    for b in board:
        print(b)
    print(f'{words} expect {expect} real {real} result {sorted(expect) == sorted(real)}')
'''
ab
aa
'''
