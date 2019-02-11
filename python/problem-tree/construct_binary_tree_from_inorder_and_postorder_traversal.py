#   https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


from TreeNode import TreeNode

class Solution:
    #   runtime; 220ms, 52.16%
    #   memory; 83.8MB, 4.88%
    def buildTree(self, inorder, postorder):

        def buildNode(_inorder, _postorder):
            if 0 == len(_inorder) and 0 == len(_postorder):
                return None
            if 1 == len(_inorder) and 1 == len(_postorder):
                return TreeNode(_postorder[-1])
            val = _postorder[-1]
            node, idx = TreeNode(val), _inorder.index(val)
            node.left = buildNode(_inorder[:idx], _postorder[:idx])
            node.right = buildNode(_inorder[idx + 1:], _postorder[idx:-1])
            return node

        return buildNode(inorder, postorder)


s = Solution()
print(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
