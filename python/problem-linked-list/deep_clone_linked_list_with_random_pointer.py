#   https://codebasil.com/problems/deep-clone-linked-list-with-random-pointer


"""
class Node {
	val: int
	next: Node
	random: Node
}
"""

def deepCloneListWithRandomPointer(root):
    """
    Args:
        {Node} root Root of the list to be copied.
    Returns:
        {Node} Root of the newly copied list.
    """
    if root is None:
        return None
    n, idx, nodeDict, idxDict = root, 0, {}, {}
    while n:
        nodeDict[n] = idx
        idxDict[idx] = n
        n = n.next
        idx += 1
    n, nodes = root, [None] * idx
    while n:
        nodes[nodeDict[n]] = Node(n.val)
        n = n.next
    for i, n in enumerate(nodes):
        if i + 1 < idx:
            n.next = nodes[i + 1]
        n.random = nodes[nodeDict[idxDict[i].random]]
    return nodes[0]
