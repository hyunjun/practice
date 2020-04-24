#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3309


class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

    def __repr__(self):
        return '({}:{})<->{}'.format(self.key, self.val, self.next)


#   runtime; 204ms, 67.09%
#   memory; 23.4MB
class LRUCache:
    def __init__(self, capacity):
        self.hash = {}
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.capacity = capacity
        self.head.prev = self.tail.next = None
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            p, n = node.prev, node.next
            p.next, n.prev = n, p
            node.prev, node.next = self.head, self.head.next
            self.head.next.prev = node
            self.head.next = node
            #print(self.hash, self.head)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].val = value
            node = self.hash[key]
            p, n = node.prev, node.next
            p.next, n.prev = n, p
        else:
            if len(self.hash) == self.capacity:
                p = self.tail.prev.prev
                n = self.hash.pop(p.next.key, None)
                n = None
                p.next = self.tail
                self.tail.prev = p
                #print('\t', self.hash, self.head)
            node = DoublyLinkedListNode(key, value)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.hash[key] = node
        #print(self.hash, self.head)

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

print()
cache = LRUCache(1)
cache.put(2, 1)
print(1 == cache.get(2))
cache.put(3, 2)
print(-1 == cache.get(2))
print(2 == cache.get(3))

print()
cache = LRUCache(2)
print(-1 == cache.get(2))
cache.put(2, 6)
print(-1 == cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(2 == cache.get(1))
print(6 == cache.get(2))

print()
cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(-1 == cache.get(1))
print(3 == cache.get(2))
