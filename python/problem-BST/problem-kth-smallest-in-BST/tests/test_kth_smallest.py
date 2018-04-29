from kth_smallest import *

def test_kth_smallest():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(16)
    root.left.left = Node(3)
    root.left.right = Node(7)
    assert 7 == kth_smallest(root, 3)
