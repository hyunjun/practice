class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        lVal, rVal = 'x', 'x'
        if self.left is None and self.right is None:
            lVal, rVal = '', ''
        if self.left:
            lVal = self.left
        if self.right:
            rVal = self.right
        return '({} {} {})'.format(lVal, self.val, rVal)

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class TreeNode2(TreeNode):
    def __init__(self, x):
        super(self.__class__, self).__init__(x)
        self.visited = False
