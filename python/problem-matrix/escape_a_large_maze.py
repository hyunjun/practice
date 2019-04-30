#   https://leetcode.com/problems/escape-a-large-maze

#   https://leetcode.com/problems/escape-a-large-maze/discuss/282870/python-solution-with-picture-show-my-thoughts
#   내가 생각했던 case들을 똑같이 그림으로 그려놓은 링크


class Solution:
    #   RecursionError: maximum recursion depth exceeded in comparison
    def isEscapePossible0(self, blocked, source, target):
        if blocked is None or 0 == len(blocked):
            return True

        R, C, blockedSet = 10 ** 6, 10 ** 6, set([(r, c) for r, c in blocked])
        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c or (r, c) in blockedSet:
                return False
            return True

        visited = set()
        def fill(r, c):
            if r == target[0] and c == target[1]:
                return True
            if (r, c) in visited:
                return False
            visited.add((r, c))
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isValid(nr, nc):
                    if fill(nr, nc):
                        return True
            return False

        return fill(source[0], source[1])

    #   Time Limit Exceeded
    def isEscapePossible1(self, blocked, source, target):
        if blocked is None or 0 == len(blocked):
            return True

        R, C, blockedSet = 10 ** 6, 10 ** 6, set([(r, c) for r, c in blocked])
        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c or (r, c) in blockedSet:
                return False
            return True

        q, visited = [source], set()
        while q:
            r, c = q.pop(0)
            if r == target[0] and c == target[1]:
                return True
            visited.add((r, c))
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isValid(nr, nc):
                    q.append((nr, nc))
        return False

    #   runtime; 64ms, 98.05%
    #   memory; 16MB, 100.00%
    def isEscapePossible(self, blocked, source, target):
        if blocked is None or 0 == len(blocked):
            return True

        R, C, blockedSet = 10 ** 6, 10 ** 6, set([(r, c) for r, c in blocked])
        def isValidBlock(r, c):
            if r < 0 or R <= r or c < 0 or C <= c or (r, c) not in blockedSet:
                return False
            return True

        def isAllConnected():
            q, visited = [blocked[0]], set()
            while q:
                r, c = q.pop(0)
                visited.add((r, c))
                for nr, nc in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
                    if isValidBlock(nr, nc) and (nr, nc) not in visited:
                        q.append((nr, nc))
            return len(visited) == len(blocked)

        #   blocked가 모두 연결되어 있지 않다면 당연히 연결 가능하므로 True
        if not isAllConnected():
            return True

        hMin, hMax, vMin, vMax = blocked[0][1], blocked[0][1], blocked[0][0], blocked[0][0]
        for r, c in blocked:
            if c < hMin:
                hMin = c
            if hMax < c:
                hMax = c
            if r < vMin:
                vMin = r
            if vMax < r:
                vMax = r

        def isIncluded(point):
            x, y = point[0], point[1]
            if hMin <= x <= hMax and vMin <= y <= vMax:
                return True
            return False

        isSourceIncluded, isTargetIncluded = isIncluded(source), isIncluded(target)

        start = source
        if not isSourceIncluded and isTargetIncluded:
            start = target

        #   blocked의 개수가 제한이 있는 점을 이용해 상하좌우값만큼만 grid를 만듦
        grid = [[0] * (hMax - hMin + 1) for _ in range(vMax - vMin + 1)]
        R, C = len(grid), len(grid[0])
        def isValid(r, c):
            if r < 0 or R <= r or c < 0 or C <= c:
                return False
            return True

        def fill(r, c):
            if grid[r][c] != 0:
                return
            grid[r][c] = 1
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isValid(nr, nc):
                    fill(nr, nc)

        #   blocked인 구간은 -1로 채우고, start point부터 fill 함수를 재귀 호출해 1로 채움
        for r, c in blocked:
            grid[r - vMin][c - hMin] = -1
        fill(start[0] - vMin, start[1] - hMin)

        #   각 경계를 검사해 1인 경우면 연결 가능
        for r in range(R):
            if hMin != 0 and grid[r][0] == 1:
                return True
            if hMax != 10 ** 6 - 1 and grid[r][C - 1] == 1:
                return True
        for c in range(C):
            if vMin != 0 and grid[c][0] == 1:
                return True
            if vMax != 10 ** 6 - 1 and grid[c][R - 1] == 1:
                return True

        return False


s = Solution()
data = [([[0,1],[1,0]], [0,0], [0,2], False),
        ([[0,1],[1,0]], [0,0], [99999,99999], False),
        ([[0,2],[1,1],[2,0]], [0,0], [99999,99999], False),
        ([], [0,0], [999999,999999], True),
        ([[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]], [655988,180910], [267728,840949], True),
        ([[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]], [100079,100063], [999948,999967], False),
        ([[100025,100016],[100026,100017],[100027,100018],[100028,100019],[100029,100020],[100030,100021],[100031,100022],[100032,100023],[100033,100024],[100034,100025],[100035,100026],[100036,100027],[100037,100028],[100038,100029],[100039,100030],[100040,100031],[100041,100032],[100042,100033],[100043,100034],[100044,100035],[100045,100036],[100046,100037],[100047,100038],[100048,100039],[100049,100040],[100050,100041],[100051,100042],[100052,100043],[100053,100044],[100054,100045],[100055,100046],[100056,100045],[100057,100044],[100058,100043],[100059,100042],[100060,100041],[100061,100040],[100062,100039],[100063,100038],[100064,100037],[100065,100036],[100066,100035],[100067,100034],[100068,100033],[100069,100032],[100070,100031],[100071,100030],[100072,100029],[100073,100028],[100074,100027],[100075,100026],[100076,100025],[100077,100024],[100078,100023],[100079,100022],[100080,100021],[100081,100020],[100082,100019],[100083,100018],[100084,100017],[100085,100016],[100084,100015],[100083,100014],[100082,100013],[100081,100012],[100080,100011],[100079,100010],[100078,100009],[100077,100008],[100076,100007],[100075,100006],[100074,100005],[100073,100004],[100072,100003],[100071,100002],[100070,100001],[100069,100000],[100068,99999],[100067,99998],[100066,99997],[100065,99996],[100064,99995],[100063,99994],[100062,99993],[100061,99992],[100060,99991],[100059,99990],[100058,99989],[100057,99988],[100056,99987],[100055,99986],[100054,99987],[100053,99988],[100052,99989],[100051,99990],[100050,99991],[100049,99992],[100048,99993],[100047,99994],[100046,99995],[100045,99996],[100044,99997],[100043,99998],[100042,99999],[100041,100000],[100040,100001],[100039,100002],[100038,100003],[100037,100004],[100036,100005],[100035,100006],[100034,100007],[100033,100008],[100032,100009],[100031,100010],[100030,100011],[100029,100012],[100028,100013],[100027,100014],[100026,100015]], [100055,100016], [999974,999914], False),
        ]
for blocked, source, target, expected in data:
    real = s.isEscapePossible(blocked, source, target)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(blocked, source, target, expected, real, expected == real))
