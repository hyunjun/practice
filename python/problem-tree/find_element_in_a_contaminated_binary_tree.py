#   https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree

#   https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/discuss/437115/Python-no-need-to-initialize-tree.-Top-down-search-by-binary


from TreeNode import TreeNode


#   runtime; 76ms, 90.16%
#   memory; 18.9MB, 100.00%
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = set()
        root.val = 0
        self.propagate(root, root.left, True)
        self.propagate(root, root.right, False)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.s

    def propagate(self, parent, node, isLeft):
        if node is None:
            return
        if isLeft:
            node.val = parent.val * 2 + 1
        else:
            node.val = parent.val * 2 + 2
        self.s.add(node.val)
        self.propagate(node, node.left, True)
        self.propagate(node, node.right, False)


root1 = TreeNode(-1)
root1.right = TreeNode(-1)

root2 = TreeNode(-1)
root2.left = TreeNode(-1)
root2.right = TreeNode(-1)
root2.left.left = TreeNode(-1)
root2.left.right = TreeNode(-1)

root3 = TreeNode(-1)
root3.right = TreeNode(-1)
root3.right.left = TreeNode(-1)
root3.right.left.left = TreeNode(-1)

data = [(root1, [1, 2], [False, True]),
        (root2, [1, 3, 5], [True, True, False]),
        (root3, [2, 3, 4, 5], [True, False, False, True])
        ]
for root, elems, expecteds in data:
    print(root)
    obj = FindElements(root)
    print(root)
    for i, elem in enumerate(elems):
        real = obj.find(elem)
        print(f'\t{elem}, expected {expecteds[i]}, real {real}, result {expecteds[i] == real}')

