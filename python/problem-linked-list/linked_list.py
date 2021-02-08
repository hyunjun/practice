
class Node:
    def __init__(self, d):
        self.d = d
        self.n = None

class SLL:    #    singly linked list
    def __init__(self):
        self.h = Node(-1)
    def printNodes(self):
        cur = self.h
        while cur.n is not None:
            cur = cur.n
            print(cur.d)
        print
    def last(self):
        l = self.h
        while l.n is not None:
            l = l.n
        return l
    def add(self, d):
        l = self.last()
        l.n = Node(d)
    def reverse(self):
        p = None
        c = self.h.n
        if c is None:
            return
        n = c.n
        while n is not None:
            c.n = p
            p = c
            c = n
            n = c.n
        c.n = p
        self.h.n = c

def reverse_every_k(sll, k):
    hList = []
    c = sll.h
    n = c.n
    while n is not None:
        cnt = 0
        hList.append(c)
        while cnt < k and n is not None:
            c = c.n
            n = c.n
            cnt += 1
        c.n = None
        c = Node(-1)
        c.n = n

    rHList = []
    for head in hList:
        rHList.append(reverse(head))
    for i in range(len(rHList) - 1):
        last(rHList[i]).n = rHList[i+1].n
    sll.h = rHList[0]
    return sll

def last(h):
    l = h
    while l.n is not None:
        l = l.n
    return l

def reverse(h):
    p = None
    c = h.n
    if c is None:
        return
    n = c.n
    while n is not None:
        c.n = p
        p = c
        c = n
        n = c.n
    c.n = p
    h.n = c
    return h

if __name__ == '__main__':
    sll = SLL()
    sll.add(1)
    sll.add(2)
    sll.add(3)
    sll.printNodes()
    sll.add(4)
    sll.printNodes()
    sll.reverse()
    sll.printNodes()
    sll.reverse()
    sll.printNodes()
    sll.add(5)
    sll.add(6)
    sll.add(7)
    sll.add(8)
    sll = reverse_every_k(sll, 3)
    sll.printNodes()
