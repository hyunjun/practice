#   https://leetcode.com/problems/h-index


class Solution:
    #   37.05%
    def hIndex0(self, citations):
        if citations is None or 0 == len(citations):
            return 0

        '''
        c = Counter(citations)
        sorted_c = sorted(c.items(), key=lambda t: t[0], reverse=True)
        cnts = [sorted_c[0][1]]
        for i in range(1, len(sorted_c)):
            cnts.append(cnts[i - 1] + sorted_c[i][1])
        print(sorted_c)
        print(cnts)
        for i in range(len(sorted_c)):
            print('{} <= {} ?'.format(len(sorted_c) - cnts[i], cnts[i]))
            if len(sorted_c) - cnts[i] <= cnts[i]:
                return sorted_c[i][0]
        return 0
        '''
        citations.sort()
        tot_cnt = len(citations)
        for i, citation in enumerate(citations):
            if citation >= tot_cnt - i:
                return tot_cnt - i
        return 0

    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3420
    #   runtime; 36ms, 76.92%
    #   memory; 14.2MB, 25.48%
    def hIndex(self, citations: List[int]) -> int:
        total = len(citations)
        citations.sort()
        for i, c in enumerate(citations):
            if total - i <= c:
                return total - i
        return 0


cases = [([3, 0, 6, 1, 5], 3),
         ([0, 0, 0], 0),
         ([6, 6, 6], 3),
         ([1, 1], 1),
         ([100], 1),
         ]
s = Solution()
for citations, expect in cases:
    real = s.hIndex(citations)
    print(f'{citations} expect {expect} real {real} result {expect == real}')
