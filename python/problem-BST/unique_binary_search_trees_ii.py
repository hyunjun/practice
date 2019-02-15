#   https://leetcode.com/problems/unique-binary-search-trees-ii

#   https://en.wikipedia.org/wiki/Catalan_number
#   결과의 갯수가 catalan number


from TreeNode import TreeNode

class Solution:

    #   runtime; 48ms, 79.19%
    #   memory; 14.9MB, 100.00%
    def generateTrees(self, n):
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


s = Solution()
for root in s.generateTrees(3):
    print(root)
'''
f([1, 2, 3])
[1] - f([2, 3])
f([2]) - [1] - f([3])
[1, 2] - f([3])
'''
