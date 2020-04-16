#   https://leetcode.com/problems/linked-list-in-binary-tree


from ListNode import ListNode
from TreeNode import TreeNode


class Solution:
    #   runtime; 788ms, 5.04%
    #   memory; 17.7MB, 100.00%
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None and root is None:
            return True
        if head is None or root is None:
            return False

        nodes, node = [], head
        while node:
            nodes.append(node.val)
            node = node.next
        nodesStr = ' '.join(str(n) for n in nodes)

        queue = [([], root)]
        while queue:
            parents, node = queue.pop()
            parents.append(node.val)
            if nodesStr in ' '.join(str(p) for p in parents):
                return True
            if node.left:
                queue.append((parents[::], node.left))
            if node.right:
                queue.append((parents[::], node.right))
            parents.pop()

        return False


s = Solution()
head1 = ListNode(4)
head1.next = ListNode(2)
head1.next.next = ListNode(8)
root1 = TreeNode(1)
root1.left = TreeNode(4)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(2)
root1.right.left.left = TreeNode(6)
root1.right.left.right = TreeNode(8)
root1.right.left.right.left = TreeNode(1)
root1.right.left.right.right = TreeNode(3)
head2 = ListNode(1)
head2.next = ListNode(4)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(6)
head3 = ListNode(1)
head3.next = ListNode(4)
head3.next.next = ListNode(2)
head3.next.next.next = ListNode(6)
head3.next.next.next.next = ListNode(8)
data = [(head1, root1, True),
        (head2, root1, True),
        (head3, root1, False),
        ]
for head, root, expected in data:
    real = s.isSubPath(head, root)
    print(f'{head} {root} expected {expected} real {real} result {expected == real}')
