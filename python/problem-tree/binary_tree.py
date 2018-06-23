
class Node:
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    def add_left(self, target, new):
        node = self.find(target)
        if node.l is None:
            node.l = Node(new)
    def add_right(self, target, new):
        node = self.find(target)
        if node.r is None:
            node.r = Node(new)
    def find(self, target):
        def find_r(node, target):
            if node is None:    return    None
            if node.d == target:    return    node
            l_result = find_r(node.l, target)
            r_result = find_r(node.r, target)
            if l_result is not None:    return    l_result
            if r_result is not None:    return    r_result
            return    None
        return    find_r(self.root, target)
    def print_inorder(self):
        def print_inorder_r(node):
            if node.l is not None:
                print_inorder_r(node.l)
            print(node.d)
            if node.r is not None:
                print_inorder_r(node.r)
        print_inorder_r(self.root)
        print()
    def mirror(self):
        def swap(node):
            if node is None:    return
            tmp = node.l
            node.l = node.r
            node.r = tmp
            swap(node.l)
            swap(node.r)
        swap(self.root)
    def isSymmetrical(self):
        def isSymmetrical(n1, n2):
            if n1 is None and n2 is None:    return    True
            if n1 is None or n2 is None or n1.d != n2.d:    return    False
            return    isSymmetrical(n1.l, n2.r) and isSymmetrical(n1.r, n2.l)
        return    isSymmetrical(self.root.l, self.root.r)
    def print_sum_path(self, val):
        def sum_path(node, val, acc):
            if node is None:    return
            if sum(acc) + node.d == val:
                print(acc, node.d)
                return
            elif sum(acc) + node.d < val:
                l_acc = list(acc)
                l_acc.append(node.d)
                sum_path(node.l, val, l_acc)
                r_acc = list(acc)
                r_acc.append(node.d)
                sum_path(node.r, val, r_acc)
            return
        sum_path(self.root, val, [])
    def common_parents(self, d1, d2):
        def get_node(node, d1, d2):
            result = (None, False, False)
            if node is None:    return    result
            print('node %d to find(%d, %d)' % (node.d, d1, d2))
            if node.d == d1:
                result = (node, True, False)
            if node.d == d2:
                result = (node, False, True)
            l_result = get_node(node.l, d1, d2)
            r_result = get_node(node.r, d1, d2)
            print(result, l_result, r_result)
            if l_result[1] and l_result[2]:
                return    l_result
            if r_result[1] and r_result[2]:
                return    r_result
            return    (node, result[1] | l_result[1] | r_result[1], result[2] | l_result[2] | r_result[2])
        return    get_node(self.root, d1, d2)

def isSubtree(btree1, btree2):
    #    1. get size of trees, then decide which is smaller
    #    2. get the data of root of smaller tree
    #    3. check wheter the data exists in taller tree
    node = btree1.find(btree2.root.d)
    if node is None:
        return    False
    #    4. compare all the nodes
    def sameNode(n1, n2):
        if n1 is None and n2 is None:    return    True
        if n1 is None or n2 is None or n1.d != n2.d:    return    False
        l_result = r_result = True
        if n1.l is not None and n2.l is not None:
            l_result = sameNode(n1.l, n2.l)
        if n1.r is not None and n2.r is not None:
            r_result = sameNode(n1.r, n2.r)
        print(n1.d, n2.d, l_result, r_result)
        return    l_result and r_result
    return    sameNode(node, btree2.root)


if __name__ == '__main__':
    btree1 = BinaryTree(6)
    btree1.add_left(6, 8)
    btree1.add_right(6, 7)
    btree1.add_left(8, 9)
    btree1.add_right(8, 2)
    btree1.add_left(2, 4)
    btree1.add_right(2, 7)
    btree1.print_inorder()

    btree2 = BinaryTree(8)
    btree2.add_left(8, 9)
    btree2.add_right(8, 2)
    btree2.print_inorder()

    print(isSubtree(btree1, btree2))

    btree1.print_inorder()
    btree1.mirror()
    btree1.print_inorder()
    print(btree1.isSymmetrical())

    btree3 = BinaryTree(6)
    btree3.add_left(6, 9)
    btree3.add_right(6, 9)
    print(btree3.isSymmetrical())

    btree4 = BinaryTree(10)
    btree4.add_left(10, 5)
    btree4.add_right(10, 12)
    btree4.add_left(5, 4)
    btree4.add_right(5, 7)
    btree4.print_sum_path(22)
    print("4, 7's common parents = %d" % btree4.common_parents(4, 7)[0].d)
    print("5, 4's common parents = %d" % btree4.common_parents(5, 4)[0].d)
    print("10, 4's common parents = %d" % btree4.common_parents(10, 4)[0].d)
    print("12, 4's common parents = %d" % btree4.common_parents(12, 4)[0].d)
