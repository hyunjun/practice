#   https://leetcode.com/problems/build-an-array-with-stack-operations


from typing import List


class Solution:
    #   runtime; 28ms, 100.00%
    #   memory; 13.8MB, 100.00%
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if target is None or not (1 <= len(target) <= 100) or not (1 <= n <= 100):
            return []
        res = []
        for i in range(1, n + 1):
            if 0 == len(target):
                break
            if target[0] == i:
                res.append("Push")
                target.pop(0)
            else:
                res.append("Push")
                res.append("Pop")
        return res


s = Solution()
data = [([1,3], 3, ["Push","Push","Pop","Push"]),
        ([1,2,3], 3, ["Push","Push","Push"]),
        ([1,2], 4, ["Push","Push"]),
        ([2,3,4], 4, ["Push","Pop","Push","Push","Push"]),
        ]
for target, n, expected in data:
    real = s.buildArray(target, n)
    print(f'{target} {n} expected {expected} real {real} result {expected == real}')
