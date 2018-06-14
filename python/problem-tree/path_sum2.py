#   https://leetcode.com/problems/path-sum-ii
#   95.14%


from TreeNode import TreeNode


class Solution:
    def pathSum(self, root, _sum):
        if root is None:
            return []
        queue, result = [(root, [])], []
        while queue:
            cur, prevList = queue[0]
            del queue[0]
            prevList.append(cur.val)
            if cur.left is None and cur.right is None:
                if sum(prevList) == _sum:
                    result.append(prevList)
            if cur.left:
                queue.append((cur.left, prevList[:]))
            if cur.right:
                queue.append((cur.right, prevList[:]))
        return result


s = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(s.pathSum(root, 22))
