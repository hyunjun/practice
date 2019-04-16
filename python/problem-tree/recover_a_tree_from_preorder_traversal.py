#   https://leetcode.com/problems/recover-a-tree-from-preorder-traversal


from TreeNode import TreeNode


class Solution:
    #   runtime; 336ms, 5.34%
    #   memory; 13.5MB, 100.00%
    def recoverFromPreorder0(self, S):
        if S is None or 0 == len(S):
            return None

        def construct(s, numDashes):
            i, indices = 1, []
            while i < len(s):
                if s[i - 1] != '-' and i + numDashes < len(s) and s[i + numDashes] != '-' and all([c == '-' for c in s[i:i + numDashes]]):
                    indices.append(i)
                    i += numDashes
                else:
                    i += 1
                if 2 == len(indices):
                    break
            if 0 == len(indices):
                node = TreeNode(s)
            else:
                node = TreeNode(s[:indices[0]])
                if 1 == len(indices):
                    node.left = construct(s[indices[0] + numDashes:], numDashes + 1)
                else:   #   2 == len(indices)
                    node.left = construct(s[indices[0] + numDashes:indices[1]], numDashes + 1)
                    node.right = construct(s[indices[1] + numDashes:], numDashes + 1)
            return node

        return construct(S, 1)

    #   runtime; 80ms, 81.98%
    #   memory; 13.6MB, 100.00%
    def recoverFromPreorder(self, S):
        if S is None or 0 == len(S):
            return None
        root, i, d = None, 0, {}
        while i < len(S):
            numDashes = 0
            while i < len(S) and S[i] == '-':
                numDashes += 1
                i += 1
            numDigits = 0
            while i < len(S) and S[i] != '-':
                numDigits += 1
                i += 1
            n = TreeNode(S[i - numDigits:i])
            if 0 < numDashes:
                p = d[numDashes - 1]
                if p.left is None:
                    p.left = n
                else:
                    p.right = n
            else:
                root = n
            d[numDashes] = n
        return root


s = Solution()
data = [('1-2--3--4-5--6--7', '((( 3 ) 2 ( 4 )) 1 (( 6 ) 5 ( 7 )))'),
        ('1-2--3---4-5--6---7', '(((( 4 ) 3 x) 2 x) 1 ((( 7 ) 6 x) 5 x))'),
        ('1-401--349---90--88', '(((( 90 ) 349 x) 401 ( 88 )) 1 x)'),
        ]
for S, expected in data:
    real = s.recoverFromPreorder(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == str(real)))
