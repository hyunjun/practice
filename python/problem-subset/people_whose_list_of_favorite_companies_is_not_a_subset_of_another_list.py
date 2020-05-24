#   https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list


from collections import defaultdict
from typing import List


class Solution:
    #   runtime; 376ms, 84.99%
    #   memory; 28.4MB, 100.00%
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        if favoriteCompanies is None or not (1 <= len(favoriteCompanies) <= 100):
            return []
        d = defaultdict(list)
        for i, favoriteCompany in enumerate(favoriteCompanies):
            d[len(favoriteCompany)].append((i, set(favoriteCompany)))
        res, maxL = [], max(d.keys()) + 1
        for l, idxCompaniesList in sorted(d.items(), key=lambda t: t[0]):
            for idx, companySet in idxCompaniesList:
                isIncluded = False
                for targetLength in range(l, maxL):
                    for tIdx, tCompanySet in d[targetLength]:
                        if idx == tIdx:
                            continue
                        if companySet.issubset(tCompanySet):
                            isIncluded = True
                            break
                    if isIncluded:
                        break
                if not isIncluded:
                    res.append(idx)
        return sorted(res)


s = Solution()
data = [([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]], [0,1,4]),
        ([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]], [0,1]),
        ([["leetcode"],["google"],["facebook"],["amazon"]], [0,1,2,3]),
        ]
for favoriteCompanies, expect in data:
    real = s.peopleIndexes(favoriteCompanies)
    print(f'{favoriteCompanies} expect {expect} real {real} result {expect == real}')
