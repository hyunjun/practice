#   https://leetcode.com/problems/binary-search-tree-iterator


from TreeNode import TreeNode


#   runtime; 12.92%
class Solution:
    def __init__(self, root):
        self.cur = root
        self.stack = []
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left

    def hasNext(self):
        if self.cur is not None or 0 < len(self.stack):
            return True
        return False

    def next(self):
        while self.hasNext():
            if self.cur is not None:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.stack[-1]
                ret = self.cur
                del self.stack[-1]
                self.cur = self.cur.right
                if ret is not None:
                    return ret.val
        return None


#   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560
#   runtime; 76ms, 56.40%
#   memory; 20.4MB, 93.96%
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes, node, stack = [], root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.nodes.append(node)
                node = node.right

    def next(self) -> int:
        if self.hasNext():
            return self.nodes.pop(0).val
        return float('-inf')

    def hasNext(self) -> bool:
        return 0 < len(self.nodes)


if __name__ == '__main__':
    '''
      10
     /  \
     5   16
    /  \
    3  7
    '''
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(16)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    b = BSTIterator(root)
    while b.hasNext():
        print(b.next())
