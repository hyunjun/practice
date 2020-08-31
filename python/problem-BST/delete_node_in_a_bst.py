#   https://leetcode.com/problems/delete-node-in-a-bst

#   https://leetcode.com/problems/delete-node-in-a-bst/discuss/93374/Simple-Python-Solution-With-Explanation


from TreeNode import TreeNode


class Solution:
    def deleteNode0(self, root, key):
        if root is None:
            return None

        #   1. search key node
        isKeyFound, parent, cur, queue = False, None, None, [(None, root)]
        while queue:
            parent, cur = queue[0]
            del queue[0]
            if key == cur.val:
                isKeyFound = True
                break
            if cur.left:
                queue.append((cur, cur.left))
            if cur.right:
                queue.append((cur, cur.right))

        if False == isKeyFound:
            return root

        #   2. delete key node and link
        isLeft = True
        while cur:
            if cur.left:
                cur.val = cur.left.val
                parent = cur
                cur = cur.left
                isLeft = True
            elif cur.right:
                cur.val = cur.right.val
                parent = cur
                cur = cur.right
                isLeft = False
            else:
                if parent:
                    if isLeft:
                        parent.left = None
                    else:
                        parent.right = None
                if root is cur:
                    root = None
                else:
                    print('delete {}'.format(cur.val))
                    cur = None
        del cur

        return root

    #   0.0%
    def deleteNode1(self, root, key):
        if root is None:
            return None

        #   dfs로 삭제할 값만 제외하고 nodes에 val을 저장
        cur, stack, nodes = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur and cur.val != key:
                    nodes.append(cur.val)
                cur = cur.right

        if 0 == len(nodes):
            return None

        #   삭제할 node가 root인 경우는 가운데 node를 root index로 지정
        if root.val == key:
            rootIdx = len(nodes) // 2
        #   삭제할 node가 root가 아닌 경우 root의 값을 찾아 root index로 지정
        else:
            rootIdx = [i for i, val in enumerate(nodes) if val == root.val][0]
        #   BST를 유지하며 재귀적으로 left, right child를 연결하고 root를 반환
        return self.linkNode(nodes, rootIdx)

    def linkNode(self, nodes, idx):
        if 0 == len(nodes):
            return None
        nodes[idx] = TreeNode(nodes[idx])
        nodes[idx].left = self.linkNode(nodes[:idx], idx // 2)
        nodes[idx].right = self.linkNode(nodes[idx + 1:], (len(nodes) - idx - 1 - 1) // 2)
        return nodes[idx]

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3443
    #   runtime; 112ms, 27.32%
    #   memory; 17.7MB, 99.62%
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        stack, node, res = [], root, []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val != key:
                    res.append(node)
                node = node.right

        if 0 == len(res):
            return None

        def reconstruct(nodes, s, e):
            if s >= e:
                return None
            m = (s + e) // 2
            nodes[m].left, nodes[m].right = reconstruct(nodes, s, m), reconstruct(nodes, m + 1, e)
            return nodes[m]

        return reconstruct(res, 0, len(res))


s = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(root)
deleted = s.deleteNode(root, 3)
print(deleted, '\t3 is removed')

root = TreeNode(0)
print(root)
deleted = s.deleteNode(root, 0)
print(deleted, '\t0 is removed')

root = TreeNode(1)
print(root)
deleted = s.deleteNode(root, 0)
print(deleted, '\t0 is removed')

root = TreeNode(1)
root.right = TreeNode(2)
print(root)
deleted = s.deleteNode(root, 2)
print(deleted, '\t2 is removed')

root = TreeNode(1)
root.right = TreeNode(2)
print(root)
deleted = s.deleteNode(root, 1)
print(deleted, '\t1 is removed')

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
print(root)
deleted = s.deleteNode(root, 3)
print(deleted, '\t3 is removed')
