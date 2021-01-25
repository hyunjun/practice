#   https://leetcode.com/problems/kth-largest-element-in-an-array


from typing import List


class Solution:
    heap_arr = ['x']
    size = 0

    def heapifyUp(self, nums):
        Solution.heap_arr = ['x']
        Solution.size = 0
        for n in nums:
            Solution.heap_arr.append(n)
            Solution.size += 1
            idx = Solution.size
            while 0 < idx:
                if 0 < idx // 2 and Solution.heap_arr[idx // 2] < Solution.heap_arr[idx]:
                    #print('before', Solution.heap_arr)
                    Solution.heap_arr[idx // 2], Solution.heap_arr[idx] = Solution.heap_arr[idx], Solution.heap_arr[idx // 2]
                    idx //= 2
                    #print('after', Solution.heap_arr)
                else:
                    break

    def peek(self):
        ret = Solution.heap_arr[1]
        Solution.size -= 1
        idx = 1
        Solution.heap_arr[1] = Solution.heap_arr[Solution.size + 1]
        Solution.heap_arr.pop()
        #print('before peeking', Solution.heap_arr, Solution.size)
        while idx < Solution.size:
            if idx * 2 + 1 <= Solution.size:
                if Solution.heap_arr[idx * 2] < Solution.heap_arr[idx * 2 + 1]:
                    bigger_child_idx = idx * 2 + 1
                else:
                    bigger_child_idx = idx * 2
            elif idx * 2 <= Solution.size:
                bigger_child_idx = idx * 2
            else:
                break
            if Solution.heap_arr[idx] < Solution.heap_arr[bigger_child_idx]:
                Solution.heap_arr[idx], Solution.heap_arr[bigger_child_idx] = Solution.heap_arr[bigger_child_idx], Solution.heap_arr[idx]
            idx = bigger_child_idx
        #print('after peeking', Solution.heap_arr, Solution.size)
        #print('peek', ret)
        return ret

    #   32.37%
    def findKthLargest0(self, nums, k):
        if nums is None or 0 == len(nums):
            return 0

        self.heapifyUp(nums)
        #print('after heapify', Solution.heap_arr)

        for i in range(k - 1):
            self.peek()

        return self.peek()

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3606
    #   runtime; 56ms, 96.14%
    #   memory; 14.9MB, 93.46%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


s = Solution()
data = [([3, 2, 1, 5, 6, 4], 2, 5),
        ([99, 99], 1, 99),
        ([2, 1], 2, 1),
        ([-1, 2, 0], 2, 0),
        ]
for nums, k, expect in data:
    real = s.findKthLargest(nums, k)
    print(f'{nums} {k} expect {expect} real {real} result {expect == real}')
