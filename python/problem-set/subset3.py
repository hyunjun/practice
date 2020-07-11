# https://leetcode.com/problems/subsets


from typing import List
import math


class Solution(object):
    # 34.60% recursive가 time limit에 걸려 다시 이 방식 사용
    def subsets0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or 0 == len(nums):
            return [[]]
        result = []
        for i in range(int(math.pow(2, len(nums)))):
            #print(i)
            idx, b = 0, i
            temp = []
            while 0 < b:
                if b & 0x1:
                    #print('[{}] 1'.format(idx))
                    temp.append(nums[idx])
                #else:
                #        print('[{}] 0'.format(idx))
                b >>= 1
                idx += 1
            result.append(temp)

        return result

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387
    #   runtime; 48ms, 20.82%
    #   memory; 14MB, 63.81%
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            res.append([nums[j] for j, n in enumerate(bin(i)[2:][::-1]) if n == '1'])
        return res


s = Solution()
print(s.subsets([]))
print(s.subsets([1]))
print(s.subsets([1, 2]))
print(s.subsets([1, 2, 3]))
print(s.subsets([1,2,3,4,5,6,7,8,10,0]))
