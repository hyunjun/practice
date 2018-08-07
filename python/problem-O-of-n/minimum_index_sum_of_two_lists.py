#   https://leetcode.com/problems/minimum-index-sum-of-two-lists

#   https://leetcode.com/problems/minimum-index-sum-of-two-lists/solution


class Solution:
    #   64.06%
    def findRestaurant(self, list1, list2):
        d1, d2 = {}, {}
        for i, r in enumerate(list1):
            d1[r] = i
        for i, r in enumerate(list2):
            d2[r] = i
        minVal, res = None, []
        for r, idx in d1.items():
            if r not in d2:
                continue
            if minVal is None or idx + d2[r] < minVal:
                minVal = idx + d2[r]
                res = [r]
            elif idx + d2[r] == minVal:
                res.append(r)
        return res


s = Solution()
data = [(['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun'], ['Shogun']),
        (['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], ['KFC', 'Shogun', 'Burger King'], ['Shogun']),
        ]
for l1, l2, expected in data:
    real = s.findRestaurant(l1, l2)
    print('{}, {}, expected {}, real {}, result {}'.format(l1, l2, expected, real, sorted(expected) == sorted(real)))
