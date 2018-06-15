#   https://leetcode.com/problems/path-sum-iii


from TreeNode import TreeNode


class Solution:

    #   Time Limit Exceeded
    #   e.g. 모든 노드가 0이고, _sum도 0인 경우
    def pathSum0(self, root, _sum):
        if root is None:
            return 0
        queue, result = [(root, [])], 0
        while queue:
            cur, prevList = queue[0]
            del queue[0]
            prevList.append(cur.val)
            for i in range(len(prevList)):
                if sum(prevList[i:]) == _sum:
                    result += 1
            if cur.left:
                queue.append((cur.left, prevList[:]))
            if cur.right:
                queue.append((cur.right, prevList[:]))
        return result

    #   67.76%
    def pathSum(self, root, _sum):
        if root is None:
            return 0
        queue, result = [(root, [0])], 0
        while queue:
            cur, prevList = queue[0]
            del queue[0]
            for i, p in enumerate(prevList):
                prevList[i] += cur.val
                if prevList[i] == _sum:
                    result += 1
            prevList.append(0)
            if cur.left:
                queue.append((cur.left, prevList[:]))
            if cur.right:
                queue.append((cur.right, prevList[:]))
        return result


s = Solution()

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
print(s.pathSum(root, 8))
