#   https://leetcode.com/problems/keys-and-rooms

#   https://leetcode.com/problems/keys-and-rooms/solution


class Solution:
    #   runtime; 56ms, 31.05%
    #   memory; 13.4MB, 19.35%
    def canVisitAllRooms(self, rooms):
        if rooms is None or 0 == len(rooms):
            return False
        roomSet, keysDict = set(), {}
        for i, keys in enumerate(rooms):
            roomSet.add(i)
            keysDict[i] = keys
        roomSet.remove(0)
        visited, q = set([0]), [keysDict[0]]
        while q:
            keys = q.pop(0)
            for key in keys:
                if key in visited:
                    continue
                if key in roomSet:
                    visited.add(key)
                    roomSet.remove(key)
                q.append(keysDict[key])
        return len(roomSet) == 0


s = Solution()
data = [([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
        ]
for rooms, expected in data:
    real = s.canVisitAllRooms(rooms)
    print('{}, expected {}, real {}, result {}'.format(rooms, expected, real, expected == real))
'''
rooms     0x    1x       2   3x
keysDict  [1 3] [3 0 1] [2]  [0]
visited   0     1            3
q         [1 3] [3 0 1] [0] -> [3 0 1] [0] -> [0]
keys      [1 3]                [3 0 1]        0
key       1 3                  3 0 1

rooms     0x   1x   2x   3x
keysDict  [1]  [2]  [3]  []
visited   0    1    2    3
q         [1]  [2]  [3]  []
keys      [1]  [2]  [3]
key       1    2    3
'''
