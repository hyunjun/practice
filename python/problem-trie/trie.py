#   http://www.geeksforgeeks.org/trie-insert-and-search/

def str2trie(strs):
    root = {}
    for s in strs:
        cur = root
        for ch in s:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
    return root


def search(root, s):
    cur = root
    for ch in s:
        if ch not in cur:
            return False
        cur = cur[ch]
    return True

strs = ['bye', 'any', 'answer', 'there', 'their']
trie_root = str2trie(strs)
for s in strs:
    print(s, search(trie_root, s))
print('and', search(trie_root, 'and'))
