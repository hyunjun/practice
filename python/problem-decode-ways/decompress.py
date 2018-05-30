

class Solution:
    def decompress(self, compressed):
        if compressed is None or 0 == len(compressed):
            return compressed
        s, compressedLen, stack = -1, len(compressed), []
        for e in range(compressedLen):
            if '[' == compressed[e] or ']' == compressed[e]:
                if s + 1 < e:
                    stack.append(compressed[s + 1:e])
                s = e
        if -1 == s:
            return compressed
        #print(stack)
        result = []
        while stack:
            cur = stack.pop()
            if '0' <= cur[0] <= '9':
                cnt = int(cur)
                result.append(result.pop() * cnt)
            elif 'a' <= cur[-1] <= 'z':
                result.append(cur)
            else:
                for i in range(len(cur)):
                    if '0' <= cur[i] <= '9':
                        break
                #print(cur[:i], cur[i:])
                cnt = int(cur[i:])
                result.append(cur[:i] + result.pop() * cnt)
        #print(result)
        return ''.join(result[::-1])


s = Solution()
data = [('2[ab]', 'abab'),
        ('ab3[xy]de2[zy]', 'abxyxyxydezyzy'),
        ('a2[b3[dk]]', 'abdkdkdkbdkdkdk'),
        ]
for compressed, expected in data:
    real = s.decompress(compressed)
    print('{}, expected {}, real {}, result {}'.format(compressed, expected, real, expected == real))
