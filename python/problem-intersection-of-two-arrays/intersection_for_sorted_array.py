#   intersection for sorted arrays

class Solution:

    #   O(n + m)
    def intersection(self, nums1, nums2):
        if nums1 is None or 0 == len(nums1) or nums2 is None or 0 == len(nums2):
            return []
        result, idx1, idx2 = [], 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
            #   To remove duplications
            prevIdx1 = idx1 - 1
            while 0 < idx1 < len(nums1) - 1 and nums1[prevIdx1] == nums1[idx1]:
                idx1 += 1
            prevIdx2 = idx2 - 1
            while 0 < idx2 < len(nums2) - 1 and nums2[prevIdx2] == nums2[idx2]:
                idx2 += 1
        return result

s = Solution()
data = [([], [2, 2], []),
        ([1, 3, 4, 7, 11, 19], [2, 3, 11, 17], [3, 11]),
        ([1, 3, 3, 4, 7, 11, 19], [2, 3, 11, 17], [3, 11])
        ]
for nums1, nums2, expected in data:
    real = s.intersection(nums1, nums2)
    print(f'{nums1}, {nums2}, expected {expected}, real {real}, result {expected == real}')
