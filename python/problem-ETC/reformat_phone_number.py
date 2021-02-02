#   https://leetcode.com/problems/reformat-phone-number


class Solution:
    #   runtime; 36ms, 32.20%
    #   memory; 14.2MB, 55.89%
    def reformatNumber(self, number: str) -> str:
        if number is None or 0 == len(number):
            return ''
        res, cnt, nums = [], 0, list(number)
        while nums:
            n = nums.pop(0)
            if '0' <= n <= '9':
                res.append(n)
                cnt += 1
                if cnt == 3:
                    res.append('-')
                    cnt = 0
        if res[-1] == '-':
            res.pop()
        if res[-2] == '-':
            res[-3], res[-2] = res[-2], res[-3]
        return ''.join(res)


s = Solution()
data = [("1-23-45 6", "123-456"),
        ("123 4-567", "123-45-67"),
        ("123 4-5678", "123-456-78"),
        ("12", "12"),
        ("--17-5 229 35-39475 ", "175-229-353-94-75"),
        ]
for number, expect in data:
    real = s.reformatNumber(number)
    print(f'{number} expect {expect} real {real} result {expect == real}')
