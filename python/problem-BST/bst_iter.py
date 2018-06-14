#   https://leetcode.com/problems/binary-search-tree-iterator
#   12.92%


from TreeNode import TreeNode


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

    s = Solution(root)
    while s.hasNext():
        print(s.next())
