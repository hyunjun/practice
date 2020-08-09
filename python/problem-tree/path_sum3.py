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

    #   runtime; 244ms, 67.76%
    def pathSum1(self, root, _sum):
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

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3417
    #   runtime; 408ms, 46.21%
    #   memory; 38.9MB
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        
        def getSum(acc, node):
            if node is None:
                return
            acc = [a + node.val for a in acc]
            acc.append(node.val)
            print(acc, node.val)
            for a in acc:
                if a == sum:
                    self.cnt += 1
            getSum(acc[:], node.left)
            getSum(acc[:], node.right)
        
        getSum([], root)
        
        return self.cnt


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
