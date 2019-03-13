#   https://www.hackerrank.com/challenges/tree-huffman-decoding


def decodeHuff(root, s):
    d, q = {}, [([], root)]
    while q:
        nums, node = q.pop(0)
        if node.left is None and node.right is None:
            d[''.join(nums)] = node.data
        if node.left:
            nums.append('0')
            q.append((nums[:], node.left))
            nums.pop()
        if node.right:
            nums.append('1')
            q.append((nums[:], node.right))
            nums.pop()
    sIdx, res = 0, []
    for i, c in enumerate(s):
        if s[sIdx:i + 1] in d:
            res.append(d[s[sIdx:i + 1]])
            sIdx = i + 1
    print(''.join(res))
