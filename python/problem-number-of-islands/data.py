# https://leetcode.com/problems/number-of-islands


grid0 = [ ['0'] ]
grid1 = [ ['1', '1', '1', '1', '0'],
          ['1', '1', '0', '1', '0'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '0', '0', '0'] ]
grid2 = [ ['1', '1', '0', '0', '0'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '0', '1', '1'] ]
grid3 = [ ['1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
          ['1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
          ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
          ['0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1'] ]
grid4 = [ ['1', '1', '0', '0', '0'],
          ['1', '1', '0', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '0', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['1', '1', '1', '1', '1'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '1', '0', '0'],
          ['0', '0', '0', '1', '1'] ]
grid5 = [ ['1', '0', '1', '1', '1'],
          ['1', '0', '1', '0', '1'],
          ['1', '1', '1', '0', '1'] ]
grid6 = [ ['1', '0', '1', '0', '0'],
          ['1', '0', '1', '0', '0'],
          ['1', '1', '1', '0', '1'],
          ['0', '0', '0', '1', '1'],
          ['0', '0', '1', '1', '1'] ]
grid7 = [ ['1', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0'],
          ['0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1'],
          ['1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0'],
          ['0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '1'],
          ['1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1'],
          ['0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0'],
          ['1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '1', '0'],
          ['0', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1'],
          ['0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0'],
          ['0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0'],
          ['1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
          ['0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1'],
          ['1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
          ['0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0'],
          ['0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1'],
          ['0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '0', '1'],
          ['0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
          ['0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1'],
          ['0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0'] ]
grid8 = [ ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1'],
          ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0'],
          ['1', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1'],
          ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
          ['1', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
          ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ]

data = [(grid0, 0),
        (grid1, 1),
        (grid2, 3),
        (grid3, 4),
        (grid4, 4),
        (grid5, 1),
        (grid6, 2),
        (grid7, 23),
        (grid8, 1),
        ]
