#   https://leetcode.com/problems/array-nesting

#   https://leetcode.com/problems/array-nesting/solution


class Solution:
    #   15.68%
    def arrayNesting(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        maxCnt, memo = 0, {}
        for i in range(len(nums)):
            j, cnt, tmp = nums[i], 1, [i]
            if j in memo:
                print('memo [{}] {}'.format(i, memo[i]))
                continue
            while j != i:
                tmp.append(j)
                j = nums[j]
                cnt += 1
            print(tmp, cnt)
            for t in tmp:
                memo[t] = cnt
            maxCnt = max(maxCnt, cnt)
            print('[{}] {}'.format(i, cnt))
        return maxCnt


s = Solution()
data = [([5, 4, 0, 3, 1, 6, 2], 4),
        ]
for nums, expected in data:
    real = s.arrayNesting(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
'''
0 1 2 3 4 5 6
5 4 0 3 1 6 2

0 -> 5 -> 6 -> 2 -> 0
1 -> 4 -> 1
2 -> 0 -> 5 -> 6 -> 2
3 -> 3
4 -> 1 -> 4
5 -> 6 -> 2 -> 0 -> 5
6 -> 2 -> 0 -> 5 -> 6
'''
