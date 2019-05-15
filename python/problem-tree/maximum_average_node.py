#   https://aonecode.com/amazon-online-assessment-questions -> Q4


from TreeNode import TreeNode


def get_max_average_node(root):
    if root is None:
        return None

    def get_max_avg_node(n):
        if n is None:
            return (None, 0, 0, 0)
        lNode, lAvg, lCnt, lVal = get_max_avg_node(n.left)
        rNode, rAvg, rCnt, rVal = get_max_avg_node(n.right)
        cnt = 1 + lCnt + rCnt
        val = n.val + lVal + rVal
        avg = val / cnt
        max_avg, max_avg_node = avg, n
        if lNode and max_avg < lAvg:
            max_avg, max_avg_node = lAvg, lNode
        if rNode and max_avg < rAvg:
            max_avg, max_avg_node = rAvg, rNode
        return (max_avg_node, max_avg, cnt, val)

    return get_max_avg_node(root)[0]


root = TreeNode(2)
root.left = TreeNode(-2)
root.right = TreeNode(14)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
root.right.right = TreeNode(-1)
print(get_max_average_node(root))
