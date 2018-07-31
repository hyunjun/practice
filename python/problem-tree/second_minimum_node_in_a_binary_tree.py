#   https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

#   https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/solution


from TreeNode import TreeNode


class Solution:
    #   Wrong Answer
    def findSecondMinimumValue0(self, root):
        if root is None or (root.left is None and root.right is None) or (root.left.val == root.right.val):
            return -1
        return max(root.left.val, root.right.val)

    #   17.41%
    def findSecondMinimumValue(self, root):
        if root is None or (root.left is None and root.right is None):
            return -1
        queue, valSet = [root], set()
        while queue:
            cur = queue.pop(0)
            valSet.add(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res = sorted(list(valSet))
        if 1 < len(res):
            return res[1]
        return -1


s = Solution()

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(s.findSecondMinimumValue(root))

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(s.findSecondMinimumValue(root))
