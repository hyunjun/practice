#   https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

#   https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   Wrong Answer
    def distanceK0(self, root, target, K):
        if root is None or target is None or K < 0:
            return []
        if 0 == K:
            return target
        '''
        1. find the target node, with depth from root
            5, depth = 1
        2. from target node, 5, level order traverse to find the depth is K
        3. from root node, level order traverse to find the depth is K - 1
            if node is the same as the target node, it would be discarded
        '''
        depth, targetNode, parentDict, q = 0, None, {}, [(0, None, root)]
        while q:
            curDepth, parent, node = q.pop(0)
            parentDict[node] = parent
            if node is target:
                depth, targetNode = curDepth, node
                break
            if node.left:
                q.append((curDepth + 1, node, node.left))
            if node.right:
                q.append((curDepth + 1, node, node.right))
        res, q = [], [(0, targetNode)]
        while q:
            curDepth, node = q.pop(0)
            if K == curDepth:
                res.append(node.val)
            if node.left:
                q.append((curDepth + 1, node.left))
            if node.right:
                q.append((curDepth + 1, node.right))
        node, exclusiveSet, steps = targetNode, set(), 0
        while node in parentDict:
            exclusiveSet.add(node)
            node = parentDict[node]
            steps += 1
        steps -= 1
        q = [(0, root)]
        while q:
            curDepth, node = q.pop(0)
            if node is targetNode:
                continue
            if K - steps == curDepth and node not in exclusiveSet:
                res.append(node.val)
            if node.left:
                q.append((curDepth + 1, node.left))
            if node.right:
                q.append((curDepth + 1, node.right))
        return res

    #   runtime; 40ms, 97.82%
    #   memory; 12.9MB, 100.00%
    def distanceK(self, root, target, K):
        if root is None or target is None or K < 0:
            return []
        if 0 == K:
            return [target.val]
        graphs, q = defaultdict(list), [(None, root)]
        while q:
            parent, node = q.pop(0)
            if parent:
                graphs[parent.val].append(node.val)
                graphs[node.val].append(parent.val)
            if node.left:
                q.append((node, node.left))
            if node.right:
                q.append((node, node.right))
        visited, res = set(), [target.val]
        while K:
            nextNodes = []
            for node in res:
                if node in visited:
                    continue
                visited.add(node)
                for n in graphs[node]:
                    if n in visited:
                        continue
                    nextNodes.append(n)
            K -= 1
            res = nextNodes
        return res


s = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root2 = TreeNode(0)
root2.left = TreeNode(1)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(2)
root3 = TreeNode(0)
root3.left = TreeNode(2)
root3.right = TreeNode(1)
root3.right.left = TreeNode(3)
root4 = TreeNode(0)
root4.left = TreeNode(1)
root4.right = TreeNode(2)
root4.left.right = TreeNode(3)
root4.right.right = TreeNode(5)
root4.left.right.left = TreeNode(4)
data = [(root1, root1.left, 2, [7, 4, 1]),
        (root2, root2.left.right, 1, [1]),
        (root3, root3.right.left, 3, [2]),
        (root4, root4.left.right, 3, [2]),
        ]
for root, target, K, expected in data:
    real = s.distanceK(root, target, K)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(root, target, K, expected, real, expected == real))
