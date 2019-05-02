#   https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

#   https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91050/Python-6-lines-bit-by-bit
#   https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/264958/Python-iterative-trie-with-comments
#   https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/130522/python-trie-solution-O(n)


from collections import defaultdict


class Solution:
    #   runtime; 356ms, 50.95%
    #   memory; 102.1MB, 27.27%
    def findMaximumXOR(self, nums):
        if nums is None or 0 == len(nums):
            return 0

        TRIE = lambda: defaultdict(TRIE)
        trie = TRIE()

        def insert(numStr, val):
            t = trie
            for n in numStr:
                t = t[n]
            t['val'] = val

        maxBitLen = len(bin(max(nums))[2:])
        for n in nums:
            bitNum = bin(n)[2:]
            bitNum = '0' * (maxBitLen - len(bitNum)) + bitNum
            insert(bitNum, n)

        maxNum = 0
        for n in nums:
            if 2 ** (maxBitLen - 1) & n == 0:
                continue
            revNode = trie
            for b in bin(n)[2:]:
                if b == '1':
                    if '0' in revNode:
                        revNode = revNode['0']
                    else:
                        revNode = revNode['1']
                elif b == '0':
                    if '1' in revNode:
                        revNode = revNode['1']
                    else:
                        revNode = revNode['0']
            maxNum = max(maxNum, n ^ revNode['val'])
        return maxNum


s = Solution()
data = [([3, 10, 5, 25, 2, 8], 28),
        ([8, 10, 2], 10),
        ([32,18,33,42,29,20,26,36,15,46], 62),
        ]
for nums, expected in data:
    real = s.findMaximumXOR(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
