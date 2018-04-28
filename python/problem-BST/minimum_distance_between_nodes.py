#   https://leetcode.com/problems/minimum-distance-between-bst-nodes
#   100.00%


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root):
        queue, vals = [root], []
        while 0 < len(queue):
            cur = queue[0]
            vals.append(cur.val)
            del queue[0]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        vals.sort()
        ret = abs(vals[1] - vals[0])
        for i in range(2, len(vals)):
            ret = min(ret, abs(vals[i] - vals[i - 1]))
        return ret


s = Solution()

node0 = TreeNode(90)
node0.left = TreeNode(69)
node0.left.left = TreeNode(49)
node0.left.right = TreeNode(89)
node0.left.left.right = TreeNode(52)

print(s.minDiffInBST(node0))

node1 = TreeNode(27)
node1.left = TreeNode(34)
node1.left.left = TreeNode(58)
node1.left.left.right = TreeNode(50)
node1.left.left.right.right = TreeNode(44)

print(s.minDiffInBST(node1))
