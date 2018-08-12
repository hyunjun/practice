#   https://leetcode.com/problems/candy

#   https://leetcode.com/problems/candy/solution


class Solution:
    #   Wrong Answer
    def candy(self, ratings):
        cnt = len(ratings)
        for i, r in enumerate(ratings):
            if 0 == i:
                if i + 1 < len(ratings) and r > ratings[i + 1]:
                    cnt += 1
            elif len(ratings) - 1 == i:
                if 0 <= i - 1 and ratings[i - 1] < r:
                    cnt += 1
            else:
                if ratings[i - 1] < r >= ratings[i + 1] or ratings[i - 1] <= r > ratings[i + 1]:
                    cnt += 1
        return cnt

    #   92.98%
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1
        #print(candies)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        #print(candies)
        return sum(candies)


s = Solution()
data = [([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 0, 3, 9, 3, 3, 1, 2, 2], 15),
        ([1, 0, 3, 9, 3, 3, 1, 2, 2, 29, 3, 3, 1, 4, 0], 24),
        ]
for ratings, expected in data:
    real = s.candy(ratings)
    print('{}, expected {}, real {}, result {}'.format(ratings, expected, real, expected == real))
