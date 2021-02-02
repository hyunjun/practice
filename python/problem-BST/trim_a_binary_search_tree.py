#   https://leetcode.com/problems/trim-a-binary-search-tree

#   https://leetcode.com/problems/trim-a-binary-search-tree/solution


from TreeNode import TreeNode


class Solution:
    #   Cannot process skewed tree
    def trimBST0(self, root, L, R):
        if root is None:
            return None
        def cutLeft(node):
            if node is None:
                return
            if L == node.val:
                node.left = None
            elif node.val < L:
                node = node.right
                cutLeft(node)
            elif node.left and node.left.val < L:
                node.left = node.left.right
            else:
                cutLeft(node.left)
        def cutRight(node):
            if node is None:
                return
            if R == node.val:
                node.right = None
            elif R < node.val:
                node = node.left
                cutRight(node)
            elif node.right and R < node.right.val:
                node.right = node.right.left
            else:
                cutRight(node.right)
        cutLeft(root)
        cutRight(root)
        return root

    #   Wrong Answer
    def trimBST1(self, root, L, R):
        if root is None:
            return None
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if L <= cur.val <= R:
                    res.append(cur)
                cur = cur.right
        print([r.val for r in res])
        res[0].left = res[-1].right = None
        if L <= root.val <= R:
            for i, r in enumerate(res):
                if r.val <= root.val:
                    print(r.left.val if r.left else 'x', r.val)
                    if r.left and r.left.val < L:
                        if 0 <= i - 1 and res[i - 1]:
                            r.left = res[i - 1]
                elif root.val <= r.val:
                    if r.right and R < r.right.val:
                        if i + 1 < len(res) and res[i + 1]:
                            r.right = res[i + 1]
            return root
        root = None
        if res[0].right:
            return res[0]
        return res[-1]

    #   Wrong Answer
    def trimBST2(self, root, L, R):
        if root is None:
            return None
        cur, stack, res, maxLevel = (root, 0), [], [], 0
        while cur[0] or stack:
            if cur[0]:
                stack.append(cur)
                if cur[0].left:
                    cur = (cur[0].left, cur[1] + 1)
                else:
                    cur = (None, None)
            else:
                cur = stack.pop()
                if L <= cur[0].val <= R:
                    res.append(cur)
                    maxLevel = max(maxLevel, cur[1])
                if cur[0].right:
                    cur = (cur[0].right, cur[1] + 1)
                else:
                    cur = (None, None)
        print([(r.val, level) for r, level in res])
        res[0][0].left = res[-1][0].right = None
        if L <= root.val <= R:
            for i, (r, level) in enumerate(res):
                if r.val <= root.val:
                    print(r.left.val if r.left else 'x', r.val)
                    if r.left and r.left.val < L:
                        if 0 <= i - 1 and res[i - 1][0]:
                            r.left = res[i - 1][0]
                elif root.val <= r.val:
                    if r.right and R < r.right.val:
                        if i + 1 < len(res) and res[i + 1][0]:
                            r.right = res[i + 1][0]
            return root
        root = None
        minVal, minNode = maxLevel, None
        for r, level in res:
            if level <= minVal:
                minVal = level
                minNode = r
        return minNode

    #   Wrong Answer
    def trimBST3(self, root, L, R):
        if root is None:
            return None

        def cut(node):
            if node is None:
                return None
            if L == node.val:
                node.left = None
            elif node.left:
                if node.left.val < L:
                    node.left = cut(node.left.right)
                else:
                    node.left = cut(node.left)
            if R == node.val:
                node.right = None
            elif node.right:
                if R < node.right.val:
                    node.right = cut(node.right.left)
                else:
                    node.right = cut(node.right)
            return node

        queue = [root]
        while queue:
            cur = queue.pop(0)
            if L <= cur.val <= R:
                return cut(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return None

    #   Wrong Answer
    def trimBST4(self, root, L, R):
        if root is None:
            return None

        def cut(node):
            if node is None:
                return None
            if L == node.val:
                node.left = None
            elif node.left:
                if node.left.val < L:
                    node.left = cut(node.left.right)
                else:
                    node.left = cut(node.left)
            if R == node.val:
                node.right = None
            elif node.right:
                if R < node.right.val:
                    node.right = cut(node.right.left)
                else:
                    node.right = cut(node.right)
            return node

        queue = [root]
        while queue:
            cur = queue.pop(0)
            if L <= cur.val <= R:
                return cut(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return None

    #   19.71%
    def trimBST5(self, root, L, R):
        if root is None:
            return None

        def cut(node):
            if node is None:
                return None
            if node.val < L:
                node = cut(node.right)
            elif L == node.val:
                node.left = None
                node.right = cut(node.right)
            elif R == node.val:
                node.left = cut(node.left)
                node.right = None
            elif R < node.val:
                node = cut(node.left)
            else:
                node.left = cut(node.left)
                node.right = cut(node.right)
            return node

        queue = [root]
        while queue:
            cur = queue.pop(0)
            if L <= cur.val <= R:
                return cut(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return None

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626
    #   runtime; 100ms
    #   memory; 18.3MB, 57.39%
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None

        if low <= root.val <= high:
            root.left, root.right = self.trimBST(root.left, low, high), self.trimBST(root.right, low, high)
            return root

        lRet, rRet = self.trimBST(root.left, low, high), self.trimBST(root.right, low, high)

        if lRet:
            return lRet
        return rRet


s = Solution()

'''
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
     \
      2
'''
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
res = s.trimBST(root, 1, 2)
print(str(res) == '(x 1 ( 2 ))')

'''
Input: 
    3
   / \
  0   4
   \
   2
  /
 1

  L = 1
  R = 3

Output: 
      3
     / 
    2   
   /
  1
'''
root = TreeNode(3)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
res = s.trimBST(root, 1, 3)
print(str(res) == '((( 1 ) 2 x) 3 x)')

root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(0)
res = s.trimBST(root, 1, 2)
print(str(res) == '(( 1 ) 2 x)')

root = TreeNode(0)
root.right = TreeNode(1)
root.right.right = TreeNode(2)
root.right.right.right = TreeNode(3)
res = s.trimBST(root, 1, 2)
print(str(res) == '(x 1 ( 2 ))')

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
res = s.trimBST(root, 1, 2)
print(str(res) == '(x 1 ( 2 ))')
res = s.trimBST(root, 3, 4)
print(str(res) == '(x 3 ( 4 ))')

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)
res = s.trimBST(root, 1, 4)
print(str(res) == '((( 1 ) 2 ( 3 )) 4 x)')

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.left.right = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
res = s.trimBST(root, 1, 4)
print(str(res) == '((x 1 ( 2 )) 3 ( 4 ))')

root = TreeNode(1)
root.right = TreeNode(2)
res = s.trimBST(root, 2, 4)
print(str(res) == '( 2 )')

root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.right = TreeNode(4)
res = s.trimBST(root, 1, 1)
print(str(res) == '( 1 )')
