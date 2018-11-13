#   https://leetcode.com/problems/intersection-of-two-arrays


class Solution:
    #   O(n^2)

    #   set이나 기타 자료구조 이용
    #   26.03%
    def intersection0(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    #   1. sort & merge sort처럼 비교 O(nlogn + mlogm + n + m)
    #   55.76%
    def intersection(self, nums1, nums2):
        sortedNums1, sortedNums2 = sorted(nums1), sorted(nums2)
        print(sortedNums1, sortedNums2)
        i, j, res = 0, 0, set()
        while i < len(nums1) and j < len(nums2):
            if sortedNums1[i] == sortedNums2[j]:
                res.add(sortedNums1[i])
                i += 1
                j += 1
            elif sortedNums1[i] < sortedNums2[j]:
                i += 1
            else:
                j += 1
        return list(res)

    #   2. 한 쪽은 sort & 다른 쪽 순회하면서 binary search O(nlogn + mlogn) = O((n + m)logn)
    #   긴 쪽과 짧은 쪽 중 어느 쪽을 정렬해야 하는가?
    #   그냥 생각하면 긴 쪽을 정렬한다고 생각하기 쉽지만, 수식으로 비교해보면 바로 알 수 있음
    #   (n + m)logn vs. (n + m)logm이므로 결국 logn vs. logm이므로 짧은 쪽을 정렬해야 함

    #   만약 정렬을 할 필요가 없다면 1과 2중에 어느 쪽이 더 좋은가?
    #   n + m vs. mlogn -> n, m의 길이에 따라 다르므로 비교를 해야 함


s = Solution()
data = [([1, 2, 2, 1], [2, 2], [2]),
        ([], [2, 2], []),
        ([1], [1, 2], [1]),
        ([3, 1, 2], [1, 3], [3, 1])
        ]
for nums1, nums2, expected in data:
    real = s.intersection(nums1, nums2)
    print('{}, {}, expected {}, real {}, result {}'.format(nums1, nums2, expected, real, expected == real))
