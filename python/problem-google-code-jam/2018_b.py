#   https://blog.naver.com/ndb796/221247631646


class Solution:
    def troubleSort(self, inp):
        if inp is None or 0 == len(inp):
            return []
        idx = len(inp) - 1
        while 0 < idx:
            tmpIdx = idx
            while 1 < tmpIdx and inp[tmpIdx - 2] > inp[tmpIdx]:
                inp[tmpIdx - 2], inp[tmpIdx] = inp[tmpIdx], inp[tmpIdx - 2]
                tmpIdx -= 2
            idx -= 1
        idx = 0
        while idx < len(inp) - 1:
            if inp[idx] > inp[idx + 1]:
                return idx
            idx += 1
        return 'OK'


s = Solution()
data = [([5, 6, 8, 4, 3], 'OK'), ([8, 9, 7], 1)]
for inp, expected in data:
    real = s.troubleSort(inp)
    print('inp {}, expected {}, real {}, result {}'.format(inp, expected, real, expected == real))
