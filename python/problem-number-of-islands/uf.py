# https://leetcode.com/problems/number-of-islands
# 21.08%

class Solution(object):
  parent_dict = {}
  rank_dict = {}

  def findSet(self, x):
    if Solution.parent_dict[x] == x:
      return x
    Solution.parent_dict[x] = self.findSet(Solution.parent_dict[x])
    return Solution.parent_dict[x]

  def unionSet(self, x, y):
    xset = self.findSet(x)
    yset = self.findSet(y)
    if xset == yset:
      return xset

    if Solution.rank_dict[xset] < Solution.rank_dict[yset]:
      Solution.parent_dict[xset] = yset
      return yset

    Solution.parent_dict[yset] = xset
    if Solution.rank_dict[xset] == Solution.rank_dict[yset]:
      Solution.rank_dict[xset] += 1
    return xset

  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if grid is None or 0 == len(grid) or 0 == len(grid[0]):
      return 0

    H = len(grid)
    W = len(grid[0])
    #for i in range(H):
    #  print(grid[i])
    #print()
    for i in range(H):
      for j in range(W):
        Solution.parent_dict[i * W + j] = i * W + j
        Solution.rank_dict[i * W + j] = 0
    #for i in range(H):
    #  print(' '.join([str(Solution.parent_dict[i * W + j]) for j in range(W)]))
    #for i in range(H):
    #  print(' '.join([str(Solution.rank_dict[i * W + j]) for j in range(W)]))
    #print()

    for i in range(H):
      for j in range(W):
        if grid[i][j] == '0':
          continue
        if 0 < j and grid[i][j - 1] == '1':
          self.unionSet(i * W + j - 1, i * W + j)
        if 0 < i and grid[i - 1][j] == '1':
          self.unionSet((i - 1) * W + j, i * W + j)
    #for i in range(H):
    #  print(' '.join([str(Solution.parent_dict[i * W + j]) for j in range(W)]))
    #for i in range(H):
    #  print(' '.join([str(Solution.rank_dict[i * W + j]) for j in range(W)]))
    ans = 0
    for i in range(H):
      for j in range(W):
        if grid[i][j] == '0':
          continue
        n = i * W + j
        if Solution.parent_dict[n] == n:
          #print(n)
          ans += 1
    return ans


s = Solution()
from data import data
for i, (grid, expected) in enumerate(data):
    real = s.numIslands(grid)
    print('[{}], expected {}, real {}, result {}'.format(i, expected, real, expected == real))
