#   https://leetcode.com/problems/occurrences-after-bigram


from typing import List


class Solution:
    #   runtime; 36ms, 50.41%
    #   memory; 13.1MB, 100.00%
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        i, splits, res = 0, text.split(' '), []
        while i < len(splits):
            if i + 2 < len(splits) and splits[i] == first and splits[i + 1] == second:
                res.append(splits[i + 2])
                i += 2
            else:
                i += 1
        return res


s = Solution()
data = [('alice is a good girl she is a good student', 'a', 'good', ['girl','student']),
        ('we will we will rock you', 'we', 'will', ['we','rock']),
        ]
for text, first, second, expected in data:
    real = s.findOcurrences(text, first, second)
    print(f'{text}, {first}, {second}, expected {expected}, real {real}, result {expected == real}')
