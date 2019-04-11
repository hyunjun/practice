#   https://leetcode.com/problems/maximum-binary-tree-ii


from TreeNode import TreeNode


class Solution:
    #   runtime; 44ms, 43.13%
    #   memory; 13.2MB, 100.00%
    def insertIntoMaxTree(self, root, val):
        if root is None:
            return None

        n, stack, arr = root, [], []
        while n or stack:
            if n:
                stack.append(n)
                n = n.left
            else:
                n = stack.pop()
                arr.append(n.val)
                n = n.right
        arr.append(val)

        def construct(A):
            if A is None or 0 == len(A):
                return None
            maxIdx, maxVal = 0, A[0]
            for i, a in enumerate(A):
                if maxVal < a:
                    maxIdx, maxVal = i, a
            root = TreeNode(maxVal)
            root.left = construct(A[:maxIdx])
            root.right = construct(A[maxIdx + 1:])
            return root

        return construct(arr)


s = Solution()
root1 = TreeNode(4)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
print(s.insertIntoMaxTree(root1, 5))
root2 = TreeNode(5)
root2.left = TreeNode(2)
root2.left.right = TreeNode(1)
root2.right = TreeNode(4)
print(s.insertIntoMaxTree(root2, 3))
