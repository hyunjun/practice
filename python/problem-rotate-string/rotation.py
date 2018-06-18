#   소문자로 구성된 문자열이 주어졌을 때 각 문자를 앞에서 나온 빈도만큼 회전하기
#   aaa -> abc
#   abc -> abc


class Solution:
    def rotate(self, c, cnt):
        targetNum = ord(c) + cnt
        return chr(((targetNum - ord('a')) % 26) + ord('a'))

    def rotation(self, inp):
        if inp is None or 0 == len(inp):
            return ''

        count_dict, result = {}, []
        for c in inp:
            if c not in count_dict:
                result.append(c)
                count_dict[c] = 1
            else:
                cnt = count_dict[c]
                result.append(self.rotate(c, cnt))
                count_dict[c] = cnt + 1

        return ''.join(result)

    def rotation1(self, inp):
        count = [0] * (ord('z') - ord('a') + 1)

        res = []
        for i in range(len(inp)):
            targetNum = ord(inp[i]) + count[ord(inp[i]) - ord('a')]
            res.append(((targetNum - ord('a')) % 26) + ord('a'))
            count[ord(inp[i]) - ord('a')] += 1
        return ''.join([chr(r) for r in res])


s = Solution()
data = [('abc', 'abc'), ('aaa', 'abc'), ('apapap', 'apbqcr'), ('zzz', 'zab'),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst'),
        ]
for inp, expected in data:
    real = s.rotation(inp)
    real1 = s.rotation1(inp)
    if len(inp) < 20:
        print('inp {}, expected {}, real {}, real1 {}, result {}'.format(inp, expected, real, real1, expected == real == real1))
    else:
        print('inp      {}\nexpected {}\nreal     {}\nreal 1   {}\nresult {}'.format(inp, expected, real, real1, expected == real == real1))
