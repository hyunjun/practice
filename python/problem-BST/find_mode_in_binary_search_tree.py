#   https://leetcode.com/problems/find-mode-in-binary-search-tree

#   https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98104/Simple-Python-Explanation


from TreeNode import TreeNode


class Solution:
    #   15.43%
    def findMode(self, root):
        cur, stack, cntDict = root, [], {}
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.val in cntDict:
                    cntDict[cur.val] += 1
                else:
                    cntDict[cur.val] = 1
                cur = cur.right
        res, maxCnt = [], None
        for val, cnt in sorted(cntDict.items(), key=lambda t: -t[1]):
            if 0 == len(res):
                res.append(val)
                maxCnt = cnt
            else:
                if maxCnt == cnt:
                    res.append(val)
        return res


s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(s.findMode(root))
