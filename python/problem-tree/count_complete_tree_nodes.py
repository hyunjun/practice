#   https://leetcode.com/problems/count-complete-tree-nodes


from TreeNode import TreeNode


class Solution:
    #   runtime; 140ms, 30.32%
    #   memory; 15.2MB, 66.50%
    def countNodes0(self, root):
        if root is None:
            return 0
        cnt, q = 0, [root]
        while q:
            node = q.pop(0)
            cnt += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return cnt

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3369
    #   runtime; 104ms, 23.81%
    #   memory; 21.1MB
    def countNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def count(node):
            if node is None:
                return
            self.res += 1
            count(node.left)
            count(node.right)
        
        count(root)
        return self.res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
data = [(root, 6),
        ]
for root, expect in data:
    real = s.countNodes(root)
    print(f'{root} expect {expect} real {real} result {expect == real}')
