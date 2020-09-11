#   https://leetcode.com/problems/number-of-good-leaf-nodes-pairs


from TreeNode import TreeNode


class Solution:
    #   runtime; 8156ms, 5.02%
    #   memory; 14.5MB, 95.91%
    def countPairs(self, root: TreeNode, distance: int) -> int:

        q, parentDict, distDict, leaves = [(root, None, 0)], {}, {}, []
        while q:
            node, parent, dist = q.pop(0)
            parentDict[id(node)], distDict[id(node)] = id(parent) if parent else None, dist
            if node.left is None and node.right is None:
                leaves.append(id(node))
            else:
                if node.left:
                    q.append((node.left, node, dist + 1))
                if node.right:
                    q.append((node.right, node, dist + 1))

        def getCommonParent(id1, id2):
            parents, p = set(), id1
            while p is not None:
                parents.add(p)
                p = parentDict[p]
            p = id2
            while p is not None:
                if p in parents:
                    return p
                p = parentDict[p]
            return None

        cnt = 0
        for i, id1 in enumerate(leaves):
            for j in range(i + 1, len(leaves)):
                id2 = leaves[j]
                if distDict[id1] + distDict[id2] - 2 * distDict[getCommonParent(id1, id2)] <= distance:
                    cnt += 1
        return cnt


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
root3 = TreeNode(7)
root3.left = TreeNode(1)
root3.right = TreeNode(4)
root3.left.left = TreeNode(6)
root3.right.left = TreeNode(5)
root3.right.right = TreeNode(3)
root3.right.left.right = TreeNode(2)
root5 = TreeNode(1)
root5.left = TreeNode(1)
root5.right = TreeNode(1)
root6 = TreeNode(72)
root6.left = TreeNode(8)
root6.left.left = TreeNode(62)
root6.left.left.left = TreeNode(82)
root6.left.left.left.left = TreeNode(70)
root6.left.left.left.left.left = TreeNode(33)
root6.left.left.left.left.right = TreeNode(18)
root6.left.left.left.right = TreeNode(73)
root6.left.left.left.right.left = TreeNode(57)
root6.left.left.left.right.right = TreeNode(26)
root6.left.left.right = TreeNode(9)
root6.left.left.right.left = TreeNode(27)
root6.left.left.right.left.left = TreeNode(58)
root6.left.left.right.left.right = TreeNode(20)
root6.left.left.right.right = TreeNode(59)
root6.left.left.right.right.left = TreeNode(76)
root6.left.left.right.right.right = TreeNode(29)
root6.left.right = TreeNode(25)
root6.left.right.left = TreeNode(30)
root6.left.right.left.left = TreeNode(30)
root6.left.right.left.left.left = TreeNode(35)
root6.left.right.left.left.right = TreeNode(62)
root6.left.right.left.right = TreeNode(55)
root6.left.right.left.right.left = TreeNode(37)
root6.left.right.left.right.right = TreeNode(47)
root6.left.right.right = TreeNode(26)
root6.left.right.right.left = TreeNode(94)
root6.left.right.right.left.left = TreeNode(26)
root6.left.right.right.right = TreeNode(47)
root6.right = TreeNode(92)
root6.right.left = TreeNode(92)
root6.right.left.left = TreeNode(52)
root6.right.left.left.left = TreeNode(41)
root6.right.left.left.right = TreeNode(13)
root6.right.left.right = TreeNode(40)
root6.right.left.right.left = TreeNode(78)
root6.right.left.right.right = TreeNode(9)
root6.right.right = TreeNode(5)
root6.right.right.left = TreeNode(49)
root6.right.right.left.left = TreeNode(29)
root6.right.right.left.right = TreeNode(78)
root6.right.right.right = TreeNode(19)
root6.right.right.right.left = TreeNode(47)
root6.right.right.right.right = TreeNode(36)
data = [(root1, 3, 1),
        (root2, 3, 2),
        (root3, 3, 1),
        (TreeNode(100), 1, 0),
        (root5, 2, 1),
        (root6, 3, 11),
        ]
for root, distance, expect in data:
    real = s.countPairs(root, distance)
    print(f'{root} {distance} expect {expect} real {real} result {expect == real}')
