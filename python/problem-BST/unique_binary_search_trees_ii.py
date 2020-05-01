#   https://leetcode.com/problems/unique-binary-search-trees-ii

#   https://en.wikipedia.org/wiki/Catalan_number
#   결과의 갯수가 catalan number


from TreeNode import TreeNode

class Solution:

    #   runtime; 48ms, 79.19%
    #   memory; 14.9MB, 100.00%
    def generateTrees0(self, n):
        if n <= 0:
            return []

        def generateNumTrees(nums):
            if len(nums) < 1:
                return []
            if 1 == len(nums):
                return [TreeNode(nums[0])]
            res = []
            print(nums)
            for i, n in enumerate(nums):
                lList, rList = nums[:i], nums[i + 1:]
                print('\t', lList, rList)
                if 0 == len(lList) and 0 == len(rList):
                    res.append(TreeNode(n))
                elif 0 == len(lList):
                    for rNode in generateNumTrees(rList):
                        node = TreeNode(n)
                        node.right = rNode
                        res.append(node)
                elif 0 == len(rList):
                    for lNode in generateNumTrees(lList):
                        node = TreeNode(n)
                        node.left = lNode
                        res.append(node)
                else:
                    for lNode in generateNumTrees(lList):
                        for rNode in generateNumTrees(rList):
                            node = TreeNode(n)
                            node.left, node.right = lNode, rNode
                            res.append(node)
            return res

        return generateNumTrees([i for i in range(1, n + 1)])

    #   https://leetcode.com/explore/featured/card/recursion-i/253/conclusion/2384
    #   runtime; 56ms, 84.15%
    #   memory; 15.2MB
    def generateTrees(self, n):
        if n is 0:
            return []

        nums = [i for i in range(1, n + 1)]

        def getTree(nums):
            if 0 == len(nums):
                return [None]
            if 1 == len(nums):
                return [TreeNode(nums[0])]
            if 2 == len(nums):
                n1 = TreeNode(nums[0])
                n1.right = TreeNode(nums[1])
                n2 = TreeNode(nums[1])
                n2.left = TreeNode(nums[0])
                return [n1, n2]
            res = []
            for i, n in enumerate(nums):
                lefts, rights = getTree(nums[:i]), getTree(nums[i + 1:])
                for l in lefts:
                    for r in rights:
                        node = TreeNode(n)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res

        return getTree(nums)


s = Solution()
for root in s.generateTrees(3):
    print(root)
