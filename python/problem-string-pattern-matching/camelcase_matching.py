#   https://leetcode.com/problems/camelcase-matching


class Solution:
    #   Wrong Answer
    def camelMatch0(self, queries, pattern):

        patternLen = len(pattern)
        def hasPattern(query):
            grid, matched = [[0] * (patternLen + 1) for _ in range(len(query) + 1)], 0
            for i, q in enumerate(query):
                for j, p in enumerate(pattern):
                    if q == p:
                        grid[i + 1][j + 1] = grid[i][j] + 1
                        if grid[i + 1][j + 1] == patternLen:
                            matched = i
                    else:
                        grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j])
            if grid[len(query)][patternLen] == patternLen:
                for i in range(matched + 1, len(query)):
                    if 'A' <= query[i] <= 'Z':
                        return False
                return True
            return False

        return [hasPattern(query) for query in queries]

    #   runtime; 40ms, 53.12%
    #   memory; 13.1MB, 100.00%
    def camelMatch(self, queries, pattern):
        def hasPattern(query, pattern):
            if query == pattern:
                return True
            if 0 == len(query):
                return False
            if 0 == len(pattern):
                for q in query:
                    if 'A' <= q <= 'Z':
                        return False
                return True
            if query[0] == pattern[0]:
                return hasPattern(query[1:], pattern[1:])
            if 'A' <= query[0] <= 'Z':
                return False
            return hasPattern(query[1:], pattern)

        return [hasPattern(query, pattern) for query in queries]


s = Solution()
data = [(['FooBar','FooBarTest','FootBall','FrameBuffer','ForceFeedBack'], 'FB', [True,False,True,True,False]),
	(['FooBar','FooBarTest','FootBall','FrameBuffer','ForceFeedBack'], 'FoBa', [True,False,True,False,False]),
	(['FooBar','FooBarTest','FootBall','FrameBuffer','ForceFeedBack'], 'FoBaT', [False,True,False,False,False]),
	]
for queries, pattern, expected in data:
    real = s.camelMatch(queries, pattern)
    print('{}, {}, expected {}, real {}, result {}'.format(queries, pattern, expected, real, expected == real))
