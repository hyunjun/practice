#   소문자로 구성된 문자열이 주어졌을 때 각 문자를 앞에서 나온 빈도만큼 회전하기
#   aaa -> abc
#   abc -> abc


class Solution:
    def rotate(self, c, cnt):
        target_num = ord(c) + cnt
        if 122 < target_num:
            target_num -= (ord('z') - ord('a') + 1)
        return chr(target_num)

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


s = Solution()
data = [('abc', 'abc'), ('aaa', 'abc'), ('apapap', 'apbqcr'), ('zzz', 'zab')]
for inp, expected in data:
    real = s.rotation(inp)
    print('inp {}, expected {}, real {}, result {}'.format(inp, expected, real, expected == real))
