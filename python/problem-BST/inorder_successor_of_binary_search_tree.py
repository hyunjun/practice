#   https://codebasil.com/problems/inorder-successor-of-binary-search-tree


from TreeNode import TreeNode


def inOrderSuccessor(root, inputNode):
    stack, n, res, idx = [], root, [], -1
    while stack or n:
        if n:
            stack.append(n)
            n = n.left
        else:
            n = stack.pop()
            res.append(n)
            if n.val == inputNode.val:
                idx = len(res)
            elif idx == len(res) - 1:
                return n
            n = n.right
    #for i, r in enumerate(res):
    #   if r.val == inputNode.val and i + 1 < len(res):
    #       return res[i + 1]
    return None
