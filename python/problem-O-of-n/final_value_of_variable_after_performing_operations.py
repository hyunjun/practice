#   https://leetcode.com/problems/final-value-of-variable-after-performing-operations


from typing import List


class Solution:
    #   runtime; 44ms, 97.43%
    #   memory; 14.3MB, 16.05%
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
        return sum(d[o] for o in operations)


s = Solution()
data = [(["--X","X++","X++"], 1),
        (["++X","++X","X++"], 3),
        (["X++","++X","--X","X--"], 0),
        ]
for operations, expect in data:
    real = s.finalValueAfterOperations(operations)
    print(f'{operations} expect {expect} real {real} result {expect == real}')
