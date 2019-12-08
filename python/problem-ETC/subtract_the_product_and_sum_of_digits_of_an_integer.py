#   https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

#   https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/discuss/446393/Python3-two-line-solution


from functools import reduce


class Solution:
    #   runtime; 24ms, 100.00%
    #   memory; 12.7MB, 100.00%
    def subtractProductAndSum(self, n: int) -> int:
        if not (1 <= n <= 10 ** 5):
            return -float('inf')
        nums = [int(c) for c in str(n)]
        return reduce(lambda x, y: x * y, nums) -  reduce(lambda x, y: x + y, nums)


s = Solution()
data = [(234, 15),
        (4421, 21),
        ]
for n, expected in data:
    real = s.subtractProductAndSum(n)
    print(f'{n}, expected {expected}, real {real}, result {expected == real}')
