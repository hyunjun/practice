#   https://www.geeksforgeeks.org/number-of-special-nodes-in-an-n-ary-tree


class NTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def get_number_of_special_nodes(root):

    result = set()

    def dfs(prev, node):
        prev.append(node)
        if 0 == len(node.children):
            if len([p.val for p in prev]) == len(set([p.val for p in prev])):
                [result.add(p) for p in prev]
        else:
            for c in node.children:
                dfs(prev[:], c)

    dfs([], root)

    return len(result)


root1 = NTreeNode(1)
root1.children.append(NTreeNode(2))
root1.children.append(NTreeNode(3))
root1.children[0].children.append(NTreeNode(4))
root1.children[0].children.append(NTreeNode(5))
root1.children[1].children.append(NTreeNode(7))
root1.children[0].children[1].children.append(NTreeNode(2))
root1.children[0].children[1].children.append(NTreeNode(3))

root2 = NTreeNode(2)
root2.children.append(NTreeNode(1))
root2.children.append(NTreeNode(4))
root2.children[0].children.append(NTreeNode(3))
root2.children[0].children.append(NTreeNode(4))
root2.children[0].children.append(NTreeNode(8))
root2.children[1].children.append(NTreeNode(10))
root2.children[0].children[1].children.append(NTreeNode(2))
root2.children[0].children[1].children.append(NTreeNode(5))
root2.children[0].children[1].children.append(NTreeNode(1))

data = [(root1, 7),
        (root2, 8),
        ]
for root, expected in data:
    real = get_number_of_special_nodes(root)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
