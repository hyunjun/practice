#   https://leetcode.com/problems/clone-graph


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from copy import deepcopy


class Solution:
    #   runtime; 28ms, 98.79%
    #   memory; 14.5MB, 99.99%
    def cloneGraph0(self, node: 'Node') -> 'Node':
        return deepcopy(node)

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3501
    #   runtime; 32ms, 94.08%
    #   memory; 14.2MB
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited, q, nodes = set(), [node], {}
        while q:
            n = q.pop(0)
            if n in visited:
                continue
            visited.add(n)
            nodes[n] = Node(n.val)
            for neighbor in n.neighbors:
                if neighbor in visited:
                    continue
                q.append(neighbor)
        for org, cloned in nodes.items():
            #print(id(org), org.val, id(cloned), cloned.val)
            for neighbor in org.neighbors:
                cloned.neighbors.append(nodes[neighbor])
        return nodes[node]


s = Solution()
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]
nn1 = s.cloneGraph(n1)
print(id(n1), id(nn1))
