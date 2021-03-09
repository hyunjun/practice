#   https://leetcode.com/problems/add-one-row-to-tree

#   https://leetcode.com/problems/add-one-row-to-tree/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 40ms, 97.65%
    #   memory; 13.7MB, 0.00%
    def addOneRow0(self, root, v, d):
        if root is None or d < 1:
            return None
        if 1 == d:
            node = TreeNode(v)
            node.left = root
            return node
        q = [(1, root)]
        while q:
            lv, node = q.pop(0)
            if lv < d - 1:
                if node.left:
                    q.append((lv + 1, node.left))
                if node.right:
                    q.append((lv + 1, node.right))
            elif lv == d - 1:
                curLeft, curRight = node.left, node.right
                node.left, node.right = TreeNode(v), TreeNode(v)
                node.left.left, node.right.right = curLeft, curRight
        return root

    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666
    #   runtime: 52ms, 82.23%
    #   memory: 16.1MB, 89.12%
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if root is None or d < 1:
            return None
        if d == 1:
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        q = [(root, 1)]
        while q:
            n, depth = q.pop(0)
            if depth == d - 1:
                newNode = TreeNode(v)
                newNode.left = n.left
                n.left = newNode
                newNode = TreeNode(v)
                newNode.right = n.right
                n.right = newNode
            else:
                if n.left:
                    q.append((n.left, depth + 1))
                if n.right:
                    q.append((n.right, depth + 1))
        return root


s = Solution()

root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(1)
root1.right.left = TreeNode(5)
print(s.addOneRow(root1, 1, 2))

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(1)
print(s.addOneRow(root2, 1, 3))
