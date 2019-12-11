#   https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal


from TreeNode import TreeNode
from typing import List


class Solution:
    #   runtime; 44ms, 96.25%
    #   memory; 12.8MB, 100.00%
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre is None or 0 == len(pre) or post is None or 0 == len(post):
            return None

        def construct(pres, posts):
            if pres is None or 0 == len(pres) or posts is None or 0 == len(posts):
                return None
            print(pres, posts)
            node = TreeNode(pres[0])
            if 2 <= len(pres) and 2 <= len(posts):
                leftVal, rightVal = pres[1], posts[-2]
                if leftVal == rightVal:
                    node.left = construct(pres[1:], posts[:-1])
                else:
                    lIdx, rIdx = pres.index(rightVal), posts.index(leftVal)
                    node.left = construct(pres[1:lIdx], posts[:rIdx + 1])
                    node.right = construct(pres[lIdx:], posts[rIdx + 1:-1])
            return node

        return construct(pre, post)


s = Solution()
data = [([1,2,4,5,3,6,7], [4,5,2,6,7,3,1], [1,2,3,4,5,6,7]),
        ]
for pre, post, expected in data:
    real = s.constructFromPrePost(pre, post)
    print(f'{pre} {post} expected {expected} real {real} result {expected == real}')
