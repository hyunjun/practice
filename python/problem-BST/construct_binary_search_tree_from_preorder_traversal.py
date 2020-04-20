#   https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal


from TreeNode import TreeNode

class Solution:
    #   runtime; 20ms, 100.00%
    #   memory; 10.9MB, 100.00%
    def bstFromPreorder0(self, preorder):
        def construct(l):
            if l is None or 0 == len(l):
                return None
            node = TreeNode(l[0])
            lIdx, rIdx = None, None
            for i, n in enumerate(l):
                if 0 == i:
                    continue
                if n < node.val and lIdx is None:
                    lIdx = i
                if node.val < n and rIdx is None:
                    rIdx = i
                    break
            if lIdx is not None:
                if rIdx is None:
                    rIdx = len(l)
                node.left = construct(l[lIdx:rIdx])
            if rIdx is not None:
                node.right = construct(l[rIdx:])
            return node
        return construct(preorder)

    #   runtime; 36ms, 100.00%
    #   memory; 10.6MB, 100.00%
    def bstFromPreorder(self, preorder):
        def construct(l):
            if l is None or 0 == len(l):
                return None
            node = TreeNode(l[0])
            node.left = construct([i for i in l if i < node.val])
            node.right = construct([i for i in l if node.val < i])
            return node
        return construct(preorder)

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305
    #   runtime; 40ms, 28.18%
    #   memory; 13.8MB
    def bstFromPreorder(self, preorder):
        if preorder is None or not (1 <= len(preorder) <= 100):
            return None

        def nodes(pres):
            if 0 == len(pres):
                return None
            node = TreeNode(pres[0])
            node.left, node.right = nodes([p for p in pres if p < pres[0]]), nodes([p for p in pres if p > pres[0]])
            return node

        return nodes(preorder)

s = Solution()
print(s.bstFromPreorder([8, 5, 1, 7, 10, 12]))
print(s.bstFromPreorder([4, 2]))
