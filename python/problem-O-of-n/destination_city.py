#   https://leetcode.com/problems/destination-city


from typing import List


class Solution:
    #   runtime; 52ms, 87.07%
    #   memory; 13.9MB, 100.00%
    def destCity(self, paths: List[List[str]]) -> str:
        if paths is None or not (1 <= len(paths) <= 100):
            return ''
        departures, arrivals = set(), set()
        for d, a in paths:
            departures.add(d)
            arrivals.add(a)
        return list(arrivals - departures)[0]


s = Solution()
data = [([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo"),
        ([["B","C"],["D","B"],["C","A"]], "A"),
        ([["A","Z"]], "Z"),
        ]
for paths, expected in data:
    real = s.destCity(paths)
    print(f'{paths} expected {expected} real {real} result {expected == real}')
