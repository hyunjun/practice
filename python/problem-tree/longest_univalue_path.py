#   https://leetcode.com/problems/longest-univalue-path

#   https://leetcode.com/problems/longest-univalue-path/solution


from TreeNode import TreeNode


class Solution:
    #   Wrong Answer
    def longestUnivaluePath0(self, root):
        if root is None:
            return 0
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        print(res)
        s, e, maxLen = 0, 0, 0
        for i, r in enumerate(res):
            if 0 == i:
                continue
            if res[i - 1] != r:
                e = i
                print('{}[{}]~{}[{}]'.format(res[s], s, res[e], e))
                maxLen = max(maxLen, e - 1 - s)
                s = i
        maxLen = max(maxLen, len(res) - 1 - s)
        return maxLen

    #   Wrong Answer
    def longestUnivaluePath1(self, root):
        if root is None:
            return 0
        queue, maxVal = [(root, [])], 0
        while queue:
            cur, prevVals = queue.pop(0)
            prevVals.append(cur.val)
            if cur.left is None and cur.right is None:
                print(prevVals)
                cnt = 0
                for i, val in enumerate(prevVals):
                    if 0 == i:
                        continue
                    if prevVals[i - 1] == val:
                        cnt += 1
                        maxVal = max(maxVal, cnt)
                    else:
                        cnt = 0
            else:
                if cur.left:
                    queue.append((cur.left, prevVals[:]))
                if cur.right:
                    queue.append((cur.right, prevVals[:]))
        return maxVal

    #   Wrong Answer
    def longestUnivaluePath2(self, root):
        if root is None:
            return 0
        def getCount(node):
            if node is None:
                return 0
            lCount, rCount = 0, 0
            if node.left:
                if node.left.val == node.val:
                    lCount = 1 + getCount(node.left)
                else:
                    lCount = getCount(node.left)
            if node.right:
                if node.right.val == node.val:
                    rCount = 1 + getCount(node.right)
                else:
                    rCount = getCount(node.right)
            if node.left and node.right and node.val == node.left.val == node.right.val:
                return lCount + rCount
            return max(lCount, rCount)
        return getCount(root)

    #   Wrong Answer
    def longestUnivaluePath3(self, root):
        def getConnectedCount(node, val):
            if node is None:
                return 0
            lCount, rCount = 0, 0
            if node.left:
                if node.left.val == node.val == val:
                    lCount = 1 + getConnectedCount(node.left, val)
                else:
                    lCount = getConnectedCount(node.left, val)
            if node.right:
                if node.right.val == node.val == val:
                    rCount = 1 + getConnectedCount(node.right, val)
                else:
                    rCount = getConnectedCount(node.right, val)
            if node.left and node.right and val == node.val == node.left.val == node.right.val:
                return lCount + rCount
            return max(lCount, rCount)

        if root is None:
            return 0
        queue, candidates = [root], set()
        while queue:
            cur = queue.pop(0)
            if cur.left:
                if cur.val == cur.left.val:
                    candidates.add(cur.val)
                queue.append(cur.left)
            if cur.right:
                if cur.val == cur.right.val:
                    candidates.add(cur.val)
                queue.append(cur.right)
        print(candidates)
        maxLen = 0
        for cand in candidates:
            maxLen = max(maxLen, getConnectedCount(root, cand))
        return maxLen

    #   Wrong Answer
    def longestUnivaluePath(self, root):
        if root is None:
            return 0
        def combine(node):
            if node is None:
                return []
            res = []
            if node.left and node.right and node.left.val == node.right.val == node.val:
                lRes = combine(node.left)
                if 0 == len(lRes):
                    res.append(node.left.val)
                else:
                    res.extend(lRes)
                res.append(node.val)
                rRes = combine(node.right)
                if 0 == len(rRes):
                    res.append(node.right.val)
                else:
                    res.extend(rRes)
            elif node.left and node.left.val == node.val:
                lRes = combine(node.left)
                if 0 == len(lRes):
                    res.append(node.left.val)
                else:
                    res.extend(lRes)
                res.append(node.val)
            elif node.right and node.right.val == node.val:
                res.append(node.val)
                rRes = combine(node.right)
                if 0 == len(rRes):
                    res.append(node.right.val)
                else:
                    res.extend(rRes)
            return res
        queue, maxVal = [root], 0
        while queue:
            cur = queue.pop(0)
            maxVal = max(maxVal, len(combine(cur)) - 1)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return maxVal

    #   57.52%  solution
    def longestUnivaluePath(self, root):
        self.ans = 0
        def getLength(node):
            if node is None:
                return 0
            lLength, rLength = getLength(node.left), getLength(node.right)
            lChild, rChild = 0, 0
            if node.left and node.left.val == node.val:
                lChild = lLength + 1
            if node.right and node.right.val == node.val:
                rChild = rLength + 1
            self.ans = max(self.ans, lChild + rChild)
            return max(lChild, rChild)
        getLength(root)
        return self.ans


s = Solution()

'''
              5
             / \
            4   5
           / \   \
          1   1   5
'''
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(5)
print(s.longestUnivaluePath(root))

'''
              1
             / \
            4   5
           / \   \
          4   4   5
'''
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(5)
print(s.longestUnivaluePath(root))

'''
              1
             /
            4
           /
          4
         /
        1
'''
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(1)
print(s.longestUnivaluePath(root))

'''
              1
               \
                4
                 \
                  4
                   \
                    1
'''
root = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(s.longestUnivaluePath(root))

'''
              1
             / \
            2   2
           / \   \
          2   2   2
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(s.longestUnivaluePath(root))

'''
              1
             / \
            2   2
           / \
          2   2
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(2)
print(s.longestUnivaluePath(root))

'''
              1
             / \
            2   3
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.longestUnivaluePath(root))

'''
              4
             / \
           -7  -3
               / \
             -9  -3
                 /
                -4
'''
root = TreeNode(4)
root.left = TreeNode(-7)
root.right = TreeNode(-3)
root.right.left = TreeNode(-9)
root.right.right = TreeNode(-3)
root.right.right.left = TreeNode(-4)
print(s.longestUnivaluePath(root))
