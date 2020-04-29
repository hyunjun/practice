#   https://leetcode.com/problems/validate-stack-sequences


from typing import List


class Solution:
    #   runtime; 76ms, 50.47%
    #   memory; 14MB, 20.00%
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed is None or popped is None:
            return False
        if 0 == len(pushed) == len(popped):
            return True
        if len(pushed) != len(popped) or not (1 <= len(pushed) <= 1000) or not (1 <= len(popped) <= 1000):
            return False

        stack = []

        def compareAndRemove():
            while 0 < len(stack) and 0 < len(popped) and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

        for p in pushed:
            compareAndRemove()
            stack.append(p)
        compareAndRemove()
        return 0 == len(stack) and 0 == len(popped)


s = Solution()
data = [([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ]
for pushed, popped, expected in data:
    real = s.validateStackSequences(pushed, popped)
    print(f'{pushed} {popped} expected {expected} real {real} result {expected == real}')
