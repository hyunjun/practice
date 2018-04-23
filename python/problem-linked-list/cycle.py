#   https://www.interviewcake.com/question/python/linked-list-cycles


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def contains_cycle(node):
    if node is None:
        return False

    step1 = node
    step2 = node.next
    if step2 is None:
        return False

    while step1 is not None and step2 is not None:
        if step1.value == step2.value:
            return True

        step1 = step1.next
        step2 = step2.next.next
    return False
