#   https://leetcode.com/problems/course-schedule

#   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344


from collections import defaultdict
from typing import List


class Solution:
    #   Wrong Answer
    def canFinish0(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not (1 <= numCourses <= 10 ** 5):
            return False
        if prerequisites is None or 0 == len(prerequisites):
            return True
        edgeDict = defaultdict(list)
        for c, p in prerequisites:
            edgeDict[p].append(c)
        for s in range(numCourses):
            q, visited = [s], set()
            while q:
                p = q.pop(0)
                if p in visited:
                    return False
                visited.add(p)
                for n in edgeDict[p]:
                    q.append(n)
        return True

    #   Time Limit Exceeded
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not (1 <= numCourses <= 10 ** 5):
            return False
        if prerequisites is None or 0 == len(prerequisites):
            return True
        edgeDict = defaultdict(list)
        for c, p in prerequisites:
            edgeDict[p].append(c)

        visited = set()
        def hasCycle(acc, v):
            visited.add(v)
            if v in acc:
                return True
            if 0 == len(edgeDict[v]):
                return False
            for n in edgeDict[v]:
                if hasCycle(acc + [v], n):
                    return True
            return False

        for s, edges in sorted(edgeDict.items(), key=lambda t: -len(t[1])):
            if s in visited:
                continue
            if hasCycle([], s):
                return False
        return True

    #   Time Limit Exceeded
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not (1 <= numCourses <= 10 ** 5):
            return False
        if prerequisites is None or 0 == len(prerequisites):
            return True
        edgeDict = defaultdict(list)
        for c, p in prerequisites:
            edgeDict[p].append(c)

        visited = set()
        for s, edges in sorted(edgeDict.items(), key=lambda t: -len(t[1])):
            if s in visited:
                continue
            q = [([], s)]
            while q:
                paths, v = q.pop(0)
                if v in paths:
                    return False
                visited.add(v)
                for n in edgeDict[v]:
                    q.append((paths + [v], n))
        return True

    #   https://leetcode.com/problems/course-schedule/discuss/658643/python3-or-cycle-detector-using-bfs-or-only-15-lines-code
    #   runtime; 616ms, 16.30%
    #   memory; 15MB
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not (1 <= numCourses <= 10 ** 5):
            return False
        if prerequisites is None or 0 == len(prerequisites):
            return True
        edgeDict = defaultdict(list)
        for c, p in prerequisites:
            edgeDict[p].append(c)
        for s in range(numCourses):
            stack, visited = [s], set()
            while stack:
                v = stack.pop()
                if v not in visited:
                    for n in edgeDict[v]:
                        stack.append(n)
                elif v == s:
                    return False
                visited.add(v)
        return True


s = Solution()
data = [(2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [0, 2], [1, 2]], True),
        (4, [[2,0],[1,0],[3,1],[3,2],[1,3]], False),
        ]
for numCourses, prerequisites, expected in data:
    real = s.canFinish(numCourses, prerequisites)
    if 20 < len(prerequisites):
        print(f'{numCourses} {prerequisites[:20]}... expected {expected} real {real} result {expected == real}')
    else:
        print(f'{numCourses} {prerequisites} expected {expected} real {real} result {expected == real}')
'''
[2] -> [0, 1] -> [1] -> [0]
{2}    {2, 0}
2 -> 1 -> 0
|         ^
----------|

0 -> 2 ---|
|         \/
|--> 1 -> 3
     ^    |
     |----|
[0] -> [1, 2] -> [2, 3] -> [3]       -> [1]
       {0}       {0, 1}    {0, 1, 2}
'''
