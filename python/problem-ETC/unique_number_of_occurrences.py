#   https://leetcode.com/problems/unique-number-of-occurrences


from collections import Counter


class Solution(object):
    #   runtime; 20ms, 85.87%
    #   memory; 11.9MB, 100.00%
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s, c = set(arr), Counter(arr)
        return len(s) == len(set(c.values()))


s = Solution()
data = [([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
        ]
for arr, expected in data:
    real = s.uniqueOccurrences(arr)
    print(f'{arr}, expected {expected}, real {real}, result {expected == real}')
