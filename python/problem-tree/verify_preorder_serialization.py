#   https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

#   https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/145320/Python-solution-beat-100
#   https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/137589/python-with-stack


from TreeNode import TreeNode


class Solution:
    #   Runtime Error
    def isValidSerialization0(self, preorder):
        if preorder is None or 0 == len(preorder):
            return False

        strs = preorder.split(',')
        i, valids = len(strs) - 1, []
        while 1 < i:
            if '#' == strs[i - 1] and '#' == strs[i]:
                valids.insert(0, (strs[i - 2], True))
                i -= 3
            else:
                valids.insert(0, (strs[i], False))
                i -= 1
        while -1 < i:
            valids.insert(0, (strs[i], False))
            i -= 1
        depth = int(math.log(len(valids) + 1, 2))
        depths = [None] * len(valids)
        depths[0] = depth
        print(valids, depth)
        for i, v in enumerate(valids):
            if v[1]:
                continue
            leftIdx = i + 1
            if len(valids) <= leftIdx:
                return False
            rightIdx = i + int(2 ** (depths[i] - 1))
            if len(valids) <= rightIdx:
                return False
            depths[leftIdx] = depths[i] - 1
            depths[rightIdx] = depths[i] - 1
            valids[i] = (valids[i][0], True)
        return True

    #   20.88%
    def isValidSerialization(self, preorder):
        if preorder is None or 0 == len(preorder):
            return False
        if 1 == len(preorder) and '#' == preorder[0]:
            return True
        root = TreeNode(preorder[0])
        stack = [root]
        strs = preorder.split(',')
        #   모두 stack에 넣고
        #   stack의 top이 left, right가 모두 None이 아닌 경우 stack에서 pop
        #   '#'인 경우도 일단은 valid한 node로 보고 넣는다
        for s in strs[1:]:
            cur = TreeNode(s)
            if 0 == len(stack):
                return False
            if stack[-1].left is None:
                stack[-1].left = cur
                if '#' != s:
                    stack.append(cur)
            else:
                stack[-1].right = cur
                if stack[-1].left and stack[-1].right:
                    stack.pop()
                if '#' != s:
                    stack.append(cur)
        #   level order로 보면서 '#'인 node가 child가 있는 경우는 False
        queue = [root]
        while queue:
            cur = queue[0]
            del queue[0]
            if '#' == cur.val and (cur.left or cur.right):
                return False
            if cur.left:
                if '#' == cur.left.val:
                    cur.left = None
                else:
                    queue.append(cur.left)
            if cur.right:
                if '#' == cur.right.val:
                    cur.right = None
                else:
                    queue.append(cur.right)
        #   stack에 남는 게 하나도 없어야 valid
        return 0 == len(stack)


s = Solution()
'''
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

       _9_
      /   \
     9     #
    / \
   9   69
  / \  / \
 19  # # #
/ \
# 9
 / \
 # #
'''
data = [('9,3,4,#,#,1,#,#,2,#,6,#,#', True),    #   see the first tree above
        ('3,2,1,#,#,#,#', True),    #   left skewed tree
        ('3,#,2,#,1,#,#', True),    #   right skewed tree
        ('1,#', False),
        ('9,#,#,1', False),
        ('9,9,9,19,#,9,#,#,#,9,#,69,#,#,#', True),  #   see the second tree above
        ('#', True),
        ('1', False),
        ('#,#,#', False),
        ]
for preorder, expected in data:
    real = s.isValidSerialization(preorder)
    print('{}, expected {}, real {}, result {}'.format(preorder, expected, real, expected == real))
