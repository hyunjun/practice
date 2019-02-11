#   https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal


from TreeNode import TreeNode

class Solution:
    #   runtime; 220ms, 45.25%
    #   memory; 83.7MB, 5.22%
    def buildTree(self, preorder, inorder):
        #   [3, 9, 20, 15, 7] -> 3, left, right 
        #   [9, 3, 15, 20, 7] -> left, 3, right
        #   left, right -> return node

        def buildNode(_preorder, _inorder):
            if 0 == len(_preorder) and 0 == len(_inorder):
                return None
            if 1 == len(_preorder) and 1 == len(_inorder):
                return TreeNode(_preorder[0])
            val = _preorder[0]
            node, idx = TreeNode(val), _inorder.index(val)
            node.left = buildNode(_preorder[1:1 + idx], _inorder[:idx])
            node.right = buildNode(_preorder[1 + idx:], _inorder[1 + idx:])
            return node

        return buildNode(preorder, inorder)


s = Solution()
print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
