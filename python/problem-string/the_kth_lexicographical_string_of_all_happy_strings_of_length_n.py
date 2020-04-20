#   https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n


class Solution:
    #   RecursionError
    def getHappyString0(self, n: int, k: int) -> str:
        if not (1 <= n <= 10) or not (1 <= k <= 100):
            return ''

        def isHappyString(s):
            if len(s) == 1:
                return True
            for i, c in enumerate(s):
                if 0 == i or len(s) - 1 == i:
                    continue
                if s[i - 1] == c or c == s[i + 1]:
                    return False
            return s[i - 1] != c

        def getNext(last, num):
            if isHappyString(last):
                num += 1
            if num == k:
                return last
            if all(c == 'c' for c in last):
                return ''

            for i in range(n - 1, -1, -1):
                if last[i] == 'a':
                    last[i] = 'b'
                    break
                if last[i] == 'b':
                    last[i] = 'c'
                    break
                if last[i] == 'c':
                    last[i] = 'a'
            return getNext(last, num)

        return ''.join(getNext(['a'] * n, 0))

    #   runtime; 892ms, 7.96%
    #   memory; 14MB, 100.00%
    def getHappyString(self, n: int, k: int) -> str:
        if not (1 <= n <= 10) or not (1 <= k <= 100):
            return ''

        def isHappyString(s):
            if len(s) == 1:
                return True
            for i, c in enumerate(s):
                if 0 == i or len(s) - 1 == i:
                    continue
                if s[i - 1] == c or c == s[i + 1]:
                    return False
            return s[i - 1] != c

        last, num = ['a'] * n, 0
        while True:
            if isHappyString(last):
                num += 1
            if num == k:
                break
            if all(c == 'c' for c in last):
                last = []
                break

            for i in range(n - 1, -1, -1):
                if last[i] == 'a':
                    last[i] = 'b'
                    break
                if last[i] == 'b':
                    last[i] = 'c'
                    break
                if last[i] == 'c':
                    last[i] = 'a'

        return ''.join(last)


s = Solution()
data = [(1, 3, 'c'),
        (1, 4, ''),
        (3, 9, 'cab'),
        (2, 7, ''),
        (10, 100, 'abacbabacb'),
        ]
for n, k, expected in data:
    real = s.getHappyString(n, k)
    print(f'{n} {k} expected {expected} real {real} result {expected == real}')
