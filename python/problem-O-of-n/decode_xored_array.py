#   https://leetcode.com/problems/decode-xored-array


from typing import List


class Solution:
    #   runtime; 220ms, 100.00%
    #   memory; 15.9MB, 100.00%
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for e in encoded:
            ret.append(ret[-1] ^ e)
        return ret


s = Solution()
data = [([1,2,3], 1, [1,0,2,1]),
        ([6,2,7,3], 4, [4,2,0,7,4]),
        ]
for encoded, first, expect in data:
    real = s.decode(encoded, first)
    print(f'{encoded} {first} expect {expect} real {real} result {expect == real}')
