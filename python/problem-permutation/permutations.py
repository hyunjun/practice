#   https://leetcode.com/problems/permutations
#   54.10%


class Solution:
    cache = {1: [[0]], 2: [[0, 1], [1, 0]]}

    def factorial(self, num):
        res = 1
        for i in range(1, num + 1):
            res *= i
        return res

    def allIndices(self, num):
        if num in Solution.cache:
            return Solution.cache[num]

        indices, res = self.allIndices(num - 1), []
        index_len, additional_num = len(indices[0]) + 1, num - 1
        for ind, index in enumerate(indices):
            for i in range(index_len):
                tmp = index[:]
                tmp.insert(i, additional_num)
                res.append(tmp)
        Solution.cache[num] = res
        return res

    def permute(self, nums):
        if nums is None or 0 == len(nums):
            return []

        res = []
        indices = self.allIndices(len(nums))

        for index in indices:
            res.append([nums[i] for i in index])

        return res


s = Solution()
print(s.permute([1, 2, 3]))
