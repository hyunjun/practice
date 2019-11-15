#   https://leetcode.com/problems/distance-between-bus-stops


class Solution(object):
    #   runtime; 36ms, 36.36%
    #   memory; 12.4MB, 100.00%
    def distanceBetweenBusStops(self, distance, start, destination):
        s, e = min(start, destination), max(start, destination)
        return min(sum(distance[s:e]), sum(distance[:s]) + sum(distance[e:]))


s = Solution()
data = [([1, 2, 3, 4], 0, 1, 1),
        ([1, 2, 3, 4], 0, 2, 3),
        ([1, 2, 3, 4], 0, 3, 4),
        ([7, 10, 1, 12, 11, 14, 5, 0], 7, 2, 17),
        ]
for distance, start, destination, expected in data:
    real = s.distanceBetweenBusStops(distance, start, destination)
    print(f'{distance}, {start}, {destination}, expected {expected}, real {real}, result {expected == real}')
