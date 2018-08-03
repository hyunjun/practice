#   https://leetcode.com/problems/flood-fill

#   https://leetcode.com/problems/flood-fill/solution


class Solution:
    #   0.0%
    def floodFill(self, image, sr, sc, newColor):
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


s = Solution()
data = [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ]
for image, sr, sc, newColor, expected in data:
    print('{}, {}, {}, {}, expected {}'.format(image, sr, sc, newColor, expected))
    real = s.floodFill(image, sr, sc, newColor)
    print('real {}, result {}'.format(real, expected == real))
