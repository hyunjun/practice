#   https://leetcode.com/problems/letter-tile-possibilities


from collections import Counter


class Solution:
    #   runtime; 148ms, 27.29%
    #   memory; 13MB, 100.00%
    def numTilePossibilities(self, tiles: str) -> int:
        if tiles is None or 0 == len(tiles):
            return 0

        self.res = 0
        def traverse(d):
            self.res += 1
            if all([v == 0 for v in d.values()]):
                return
            for c, cnt in d.items():
                if 0 < cnt:
                    d[c] -= 1
                    traverse(d)
                    d[c] += 1

        traverse(Counter(tiles))

        return self.res - 1


s = Solution()
data = [('AAB', 8),
        ('AAABBC', 188),
        ]
for tiles, expected in data:
    real = s.numTilePossibilities(tiles)
    print(f'{tiles}, expected {expected}, real {real}, result {expected == real}')
