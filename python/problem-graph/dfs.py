from collections import defaultdict

edge_list = [(5, 6), (5, 4), (6, 4), (6, 1), (4, 2), (1, 4), (2, 1), (2, 3)]

adjacency_list_dict = defaultdict(lambda: [])
for src, dst in edge_list:
    adjacency_list_dict[src].append(dst)

visiting_list, visited_list = [], []
visiting_list.append(5)
while 0 < len(visiting_list):
    cur = visiting_list.pop()
    for adj in adjacency_list_dict[cur]:
        if adj not in visiting_list and adj not in visited_list:
            visiting_list.append(adj)
    visited_list.append(cur)
print(visited_list)
