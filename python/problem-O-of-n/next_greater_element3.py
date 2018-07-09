#   https://leetcode.com/problems/next-greater-element-iii
#   85.47%


class Solution:
    def nextGreaterElement(self, n):
        if n <= 10:
            return -1

        digits, maxVal = list(str(n)), 2 ** 31 - 1
        for i in range(len(digits) - 2, -1, -1):
            for j in range(len(digits) - 1, i, -1):
                if digits[i] < digits[j]:
                    tmp = sorted(digits[i:])
                    for k, t in enumerate(tmp):
                        if digits[i] < t:
                            idx = k
                            break
                    cand = int(''.join([str(d) for d in digits[:i] + tmp[k:k + 1] + tmp[:k] + tmp[k + 1:]]))
                    if maxVal <= cand:
                        return -1
                    return cand
        return -1


s = Solution()
data = [(12, 21),
        (21, -1),
        (210241, 210412),
        (1999999999, -1),
        (2147483647, -1),
        ]
for n, expected in data:
    real = s.nextGreaterElement(n)
    print('{}, expected {}, real {}, result {}'.format(n, expected, real, expected == real))
