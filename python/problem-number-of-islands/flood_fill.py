#   https://leetcode.com/problems/flood-fill

#   https://leetcode.com/problems/flood-fill/solution


from typing import List


class Solution:
    #   0.0%
    def floodFill0(self, image, sr, sc, newColor):
        if image is None or 0 == len(image) or image[0] is None or 0 == len(image[0]):
            return image
        row, column = len(image), len(image[0])
        visited = set()
        def fill(r, c, curColor):
            if (r, c) in visited or r < 0 or c < 0 or row <= r or column <= c or image[r][c] != curColor:
                return
            visited.add((r, c))
            image[r][c] = newColor
            points = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for x, y in points:
                fill(x, y, curColor)
        fill(sr, sc, image[sr][sc])
        return image

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326
    #   runtime; 72ms, 93.84%
    #   memory; 13.9MB
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image is None or not (1 <= len(image) <= 50) or not (1 <= len(image[0]) <= 50) or not (0 <= sr < len(image)) or not (0 <= sc < len(image[0])):
            return [[]]
        R, C, COLOR, visited = len(image), len(image[0]), image[sr][sc], set()

        def fill(r, c):
            if not (0 <= r < R) or not (0 <= c < C) or (r, c) in visited or image[r][c] != COLOR:
                return
            visited.add((r, c))
            image[r][c] = newColor
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                fill(nr, nc)

        fill(sr, sc)

        return image


s = Solution()
data = [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ]
for image, sr, sc, newColor, expected in data:
    print('{}, {}, {}, {}, expected {}'.format(image, sr, sc, newColor, expected))
    real = s.floodFill(image, sr, sc, newColor)
    print('real {}, result {}'.format(real, expected == real))
