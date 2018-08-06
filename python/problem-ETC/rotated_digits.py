#   https://leetcode.com/problems/rotated-digits


class Solution:
    d = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}

    #   25.26%
    def rotatedDigits(self, N):

        def rotate(n):
            s = str(n)
            res = []
            for c in s:
                if c not in Solution.d:
                    return None
                res.append(Solution.d[c])
            return int(''.join(res))

        cnt = 0
        for i in range(N + 1):
            rotated = rotate(i)
            if rotated and rotated != i:
                cnt += 1
        return cnt


s = Solution()
data = [(10, 4),
        ]
for N, expected in data:
    real = s.rotatedDigits(N)
    print('{}, expected {}, real {}, result {}'.format(N, expected, real, expected == real))
