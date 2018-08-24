#   https://leetcode.com/problems/predict-the-winner

#   https://leetcode.com/problems/predict-the-winner/solution
#   https://www.youtube.com/watch?v=6ELUvkSkCts


class Solution:
    #   Time Limit Exceeded
    def predictTheWinner0(self, nums):
        if nums is None or 0 == len(nums):
            return False
        if len(nums) < 3:
            return True
        def turnByTurnSum(s1, s2, isP1Turn, l, r):
            if r - l == 1:
                bigger, smaller = max(nums[l], nums[r]), min(nums[l], nums[r])
                if isP1Turn:
                    return s1 + bigger, s2 + smaller
                return s1 + smaller, s2 + bigger
            if isP1Turn:
                ls1, ls2 = turnByTurnSum(s1 + nums[l], s2, not isP1Turn, l + 1, r)
                rs1, rs2 = turnByTurnSum(s1 + nums[r], s2, not isP1Turn, l, r - 1)
                if ls1 > rs1:
                    return ls1, ls2
                return rs1, rs2
            ls1, ls2 = turnByTurnSum(s1, s2 + nums[l], not isP1Turn, l + 1, r)
            rs1, rs2 = turnByTurnSum(s1, s2 + nums[r], not isP1Turn, l, r - 1)
            if ls1 < rs1:
                return ls1, ls2
            return rs1, rs2
        s1, s2 = turnByTurnSum(0, 0, True, 0, len(nums) - 1)
        return s1 >= s2

    #   0.0%
    def predictTheWinner(self, nums):
        if nums is None or 0 == len(nums):
            return False
        if len(nums) < 3:
            return True
        def turnByTurnSum(s1, s2, isP1Turn, l, r):
            #print(s1, s2, isP1Turn, l, r)
            if r - l == 2:
                bigger, smaller = max(nums[l], nums[r]), min(nums[l], nums[r])
                if isP1Turn:
                    return s1 + bigger + min(smaller, nums[l + 1]), s2 + max(smaller, nums[l + 1])
                return s1 + max(smaller, nums[l + 1]), s2 + bigger + min(smaller, nums[l + 1])
            elif r - l == 3:
                lSum, rSum = nums[l] + nums[l + 2], nums[l + 1] + nums[r]
                if isP1Turn:
                    if s1 + lSum > s2 + rSum:
                        return s1 + lSum, s2 + rSum
                    return s1 + rSum, s2 + lSum
                if s1 + lSum < s2 + rSum:
                    return s1 + lSum, s2 + rSum
                return s1 + rSum, s2 + lSum
            if isP1Turn:
                ls1, ls2 = turnByTurnSum(s1 + nums[l], s2, not isP1Turn, l + 1, r)
                rs1, rs2 = turnByTurnSum(s1 + nums[r], s2, not isP1Turn, l, r - 1)
                #print(isP1Turn, ls1, ls2, 'vs', rs1, rs2)
                if ls1 > rs1:
                    return ls1, ls2
                return rs1, rs2
            ls1, ls2 = turnByTurnSum(s1, s2 + nums[l], not isP1Turn, l + 1, r)
            rs1, rs2 = turnByTurnSum(s1, s2 + nums[r], not isP1Turn, l, r - 1)
            #print(isP1Turn, ls1, ls2, 'vs', rs1, rs2)
            if ls1 < rs1:
                return ls1, ls2
            return rs1, rs2
        s1, s2 = turnByTurnSum(0, 0, True, 0, len(nums) - 1)
        return s1 >= s2


s = Solution()
data = [([1, 5, 2], False),
        ([1, 5, 233, 7], True),
        ([1, 5, 233, 7, 9], False),
        ([1, 5, 233, 7, 9, 2], True),
        ([1, 5, 233, 7, 9, 232, 2], True),
        ([0, 1, 5, 233, 7, 9, 232, 2], True),
        ([1163573,4225123,1034109,6416120,4401957,408968,8769389,7498770,6003151,2054050,2621821,8204739,2586055,6520977,2014732,4750306,4172182,6965656,1861876,9549339], True),
        ([1398871,3911315,3298661,725450,9541448,915835,3155005,58239,1541250,6094565,7622099,1953520,5565179,5923565,1842903,7679819,7288290,8409862,1747401,1662260], True),
        ([1000,999,999,1000,555,400], True),
        ]
for nums, expected in data:
    real = s.predictTheWinner(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
