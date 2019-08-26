#   https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character


from typing import List


class Solution:
    #   runtime; 96ms, 78.28%
    #   memory; 14.3MB, 100.00%
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        if queries is None or 0 == len(queries) or words is None or 0 == len(queries):
            return []

        def getCount(word):
            minChar = min(word)
            return len([c for c in word if c == minChar])

        qCounts, wCounts = [getCount(query) for query in queries], sorted([getCount(word) for word in words])
        print(qCounts, wCounts)

        def binarySearch(arr, num):
            if len(arr) == 1:
                return 1 if num < arr[0] else 0
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if (0 <= m - 1 and arr[m - 1] <= num < arr[m]):
                    return len(arr) - m
                if arr[m] <= num:
                    l = m + 1
                else:
                    r = m - 1
            return 0
        '''
        0 1 2 3
        1 2 3 4 num = 4
        l m   r not (arr[m - 1] <= num < arr[m]) and arr[m] <= num: l = m + 1
            l
            m   not (arr[m - 1] <= num < arr[m]) and arr[m] <= num: l = m + 1
              l
              m not (arr[m - 1] <= num < arr[m]) and arr[m] <= num: l = m + 1
                l

        0 1 2 3
        1 2 3 4 num = 3
        l m   r arr[m] < num: l = m + 1
            l r
            m   arr[m] == num: l = m + 1
              l
              m arr[m  - 1] <= num < arr[m]: return len(arr) - m

        0 1 2 3
        1 2 3 4 num = 2
        l m   r arr[m] == num: l = m + 1
            l r
            m   arr[m  - 1] <= num < arr[m]: return len(arr) - m

        0 1 2 3
        1 2 3 4 num = 1
        l m   r arr[m - 1] <= num < arr[m]: return len(arr) - m

        0 1 2 3
        1 2 3 4 num = 0
        l m   r not (arr[m - 1] <= num < arr[m]): r = m - 1
        r
        m       num < arr[m]:   return len(arr) - m
        '''

        return [binarySearch(wCounts, qCount) for qCount in qCounts]


s = Solution()
data = [(['cbd'], ['zaaaz'], [1]),
        (['bbb', 'cc'], ['a', 'aa', 'aaa', 'aaaa'], [1, 2]),
        (['a', 'aa', 'aaa', 'aaaa'], ['a', 'aa', 'aaa', 'aaaa'], [3, 2, 1, 0]),
        ]
for queries, words, expected in data:
    real = s.numSmallerByFrequency(queries, words)
    print(f'{queries}, {words}, expected {expected}, real {real}, result {expected == real}')
