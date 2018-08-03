#   https://leetcode.com/problems/design-linked-list


from ListNode import ListNode


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if self.head is None or index < 0:
            return -1
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
            if cur is None and 0 == index:
                return -1
        return cur

    def addAtHead(self, val):
        if self.head is None:
            self.head = ListNode(val)

    def addAtTail(self, val):
        if self.head is None:
            self.addAtHead(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)

    def addAtIndex(self, index, val):
        if self.head is None:
            if 0 == index:
                self.addAtHead(val)
        else:
            index -= 1
            cur = self.head
            _next = cur.next
            while cur and index:
                _next = _next.next
                cur = _next
                index -= 1
            if cur:
                cur.next = ListNode(val)
                cur.next.next = _next

    def deleteAtIndex(self, index):
        if self.head is None or index < 0:
            return
        if 0 == index:
            self.head = self.head.next
        else:
            index -= 1
            prev = self.head
            cur = prev.next
            while prev and index:
                prev = cur
                cur = prev.next
                index -= 1
            if cur.next:
                prev.next = cur.next
            else:
                prev.next = None



linkedList = MyLinkedList()
linkedList.addAtHead(1)
print(linkedList.head)
linkedList.addAtTail(3)
print(linkedList.head)
linkedList.addAtIndex(1, 2)
print(linkedList.head)
print(2 == linkedList.get(1).val)
linkedList.deleteAtIndex(1)
print(linkedList.head)
print(3 == linkedList.get(1).val)
print(-1 == linkedList.get(2))
linkedList.deleteAtIndex(1)
print(linkedList.head)
