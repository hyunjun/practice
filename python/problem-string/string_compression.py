#   https://leetcode.com/problems/string-compression
#   37.52%

#   https://leetcode.com/problems/string-compression/solution


class Solution:
    def compress(self, chars):
        if chars is None or 0 == len(chars):
            return 0
        start, cnt = 0, 1
        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                cnt += 1
            else:
                if 1 < cnt:
                    #   숫자를 char로 바꿔 하나씩 입력
                    strCnt = str(cnt)
                    for j in range(len(strCnt)):
                        chars[start + 1 + j] = strCnt[j]
                    #   더 이상 필요없는 chars는 None으로 변경
                    blankStart = start + len(strCnt) + 1
                    for k in range(blankStart, blankStart + cnt - len(strCnt) - 1):
                        chars[k] = None
                start, cnt = i, 1
        if 1 < cnt:
            strCnt = str(cnt)
            for i in range(len(strCnt)):
                chars[start + 1 + i] = strCnt[i]
            blankStart = start + len(strCnt) + 1
            for j in range(blankStart, blankStart + cnt - len(strCnt) - 1):
                chars[j] = None
        #   None인 char들을 remove element 방법을 이용해 실제 문자로 할당
        #   https://github.com/hyunjun/practice/blob/master/python/problem-remove-element/remove_element.py
        i = 0
        for j in range(len(chars)):
            if chars[j] is not None:
                chars[i] = chars[j]
                i += 1
        return i


s = Solution()
data = [(['a', 'a', 'b', 'b', 'c', 'c', 'c'], ['a', '2', 'b', '2', 'c', '3']),
        (['a'], ['a']),
        (['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['a', 'b', '1', '2']),
        (['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c'], ['a', 'b', '1', '2', 'c']),
        (['a', 'a', 'b'], ['a', '2', 'b']),
        (['a', 'a', 'a', 'b', 'b', 'a', 'a'], ['a', '3', 'b', '2', 'a', '2']),
        ]
for chars, expected in data:
    real = s.compress(chars)
    print('{}, expected {}, real {}, result {}'.format(chars, expected, real, len(expected) == real))
