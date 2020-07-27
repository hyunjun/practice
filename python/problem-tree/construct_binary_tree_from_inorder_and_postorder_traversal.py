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

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3403
    #   runtime; 204ms, 38.71%
    #   memory; 87.5MB, 32.32%
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder is None or 0 == len(inorder) or postorder is None or 0 == len(postorder) or len(inorder) != len(postorder):
            return None
        node = TreeNode(postorder[-1])
        idx = inorder.index(node.val)
        node.left, node.right = self.buildTree(inorder[:idx], postorder[:idx]), self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return node


s = Solution()
print(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
