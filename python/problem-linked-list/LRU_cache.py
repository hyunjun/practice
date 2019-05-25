#   https://leetcode.com/problems/lru-cache


class DoublyLinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

    def __repr__(self):
        return '({}:{})<->{}'.format(self.key, self.value, self.next)


#   runtime; 124ms, 70.28%
#   memory; 22MB, 27.65%
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            return node.value
        return -1

    def put(self, key, value):
        if key in self.d:
            node = self.d[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
        else:
            if self.capacity <= len(self.d):
                removed = self.tail.prev
                p = removed.prev
                p.next = self.tail
                self.tail.prev = p
                del self.d[removed.key]
                del removed
            node = DoublyLinkedList(key, value)
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.d[key] = node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(1 == cache.get(1))
cache.put(3, 3)
print(-1 == cache.get(2))
cache.put(4, 4)
print(-1 == cache.get(1))
print(3 == cache.get(3))
print(4 == cache.get(4))
