from collections import defaultdict
from typing import List


class Solution:
    #   Wrong Answer
    def findItinerary0(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for departure, arrival in tickets:
            d[departure].append(arrival)

        self.res = []
        def chaining(acc, visited, airport):
            if len(visited) == len(tickets) or airport is None:
                if airport is not None:
                    acc.append(airport)
                self.res.append(acc)
            else:
                hasNextCity = False
                if airport in d:
                    acc.append(airport)
                    for nextCity in d[airport]:
                        visit = (airport, nextCity)
                        if visit in visited:
                            continue
                        hasNextCity = True
                        visited.add(visit)
                        chaining(acc[:], visited, nextCity)
                        visited.remove(visit)
                if hasNextCity == False:
                    chaining(acc, visited, airport)
        chaining([], set(), "JFK")
        return sorted(self.res, key=lambda t: ''.join(t))[0]

    #   Time Limit Exceeded
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        cities = set()
        for departure, arrival in tickets:
            cities.add(departure)
            cities.add(arrival)
        cities.remove("JFK")
        cities = sorted(list(cities))
        cities.insert(0, "JFK")
        citiDict = {city: i for i, city in enumerate(cities)}
        board = [[0] * len(cities) for _ in range(len(cities))]
        for departure, arrival in tickets:
            board[citiDict[departure]][citiDict[arrival]] += 1
        #for b in board:
        #    print(b)

        self.res = []
        def visit(visited, acc, num):
            #print(acc, num)
            #for v in visited:
            #    print(v)
            hasNext = False
            acc.append(cities[num])
            for i, n in enumerate(visited[num]):
                if 0 < n:
                    hasNext = True
                    visited[num][i] -= 1
                    visit(visited, acc[:], i)
                    visited[num][i] += 1
            if hasNext == False:
                #print('res', acc)
                self.res.append(acc)

        for i, n in enumerate(board[0]):
            if 0 < n:
                board[0][i] -= 1
                visit(board, [cities[0]], i)
                board[0][i] += 1

        return sorted(self.res, key=lambda t: (-len(t), ''.join(t)))[0]

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3374
    #   https://leetcode.com/problems/reconstruct-itinerary/discuss/709877/Python3-DFS-Solution
    #   runtime; 72ms, 97.95%
    #   memory; 14MB, 81.24%
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        tickets.sort(key=lambda x: x[1])

        for u, v in tickets:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

        itinerary, stack = [], [("JFK")]

        while stack:
            cur = stack[-1]

            if cur in graph and len(graph[cur]) > 0:
                stack.append(graph[cur].pop(0))
            else:
                itinerary.append(stack.pop())
        return itinerary[::-1]


s = Solution()
data = [([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]),
        ([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]], ["JFK","NRT","JFK","KUL"]),
        ([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]], ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]),
        ([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]], ['JFK', 'ADL', 'ANU', 'ADL', 'ANU', 'AUA', 'ADL', 'AUA', 'ADL', 'AUA', 'ANU', 'AXA', 'ADL', 'AUA', 'ANU', 'AXA', 'ADL', 'AXA', 'ADL', 'AXA', 'ANU', 'AXA', 'ANU', 'AXA', 'EZE', 'ADL', 'AXA', 'EZE', 'ADL', 'AXA', 'EZE', 'ADL', 'EZE', 'ADL', 'EZE', 'ADL', 'EZE', 'ANU', 'EZE', 'ANU', 'EZE', 'AUA', 'AXA', 'EZE', 'AUA', 'AXA', 'EZE', 'AUA', 'AXA', 'JFK', 'ADL', 'EZE', 'AUA', 'EZE', 'AXA', 'JFK', 'ADL', 'JFK', 'ADL', 'JFK', 'ADL', 'JFK', 'ADL', 'TIA', 'ADL', 'TIA', 'AUA', 'JFK', 'ANU', 'TIA', 'AUA', 'JFK', 'AUA', 'JFK', 'AUA', 'TIA', 'AUA', 'TIA', 'AXA', 'TIA', 'EZE', 'AXA', 'TIA', 'EZE', 'JFK', 'AXA', 'TIA', 'EZE', 'JFK', 'AXA', 'TIA', 'JFK', 'EZE', 'TIA', 'JFK', 'EZE', 'TIA', 'JFK', 'TIA', 'JFK', 'AUA', 'SYD']),
        ]
for tickets, expect in data:
    real = s.findItinerary(tickets)
    print(f'{tickets}\n\texpect {expect}\n\treal {real}\n\tresult {expect == real}')
