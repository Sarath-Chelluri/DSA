class Deque:
    def __init__(self):
        # self.deque
        self.first = self.last = Node()

    def isEmpty(self):
        if self.last.val and self.first.val:
            return False

    def size(self):
        curr = self.first
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return size

    def addFirst(self, val):
        if self.first.val == None:
            self.first.val = val
            return
        cur = Node(val=val, next=self.first)
        self.first = cur

    def addLast(self, val):
        cur = Node(val=val)
        self.last.next = cur
        self.last = cur

    def removeFirst(self):
        self.first = self.first.next

    def removeLast(self):
        cur = self.first
        while cur.next != self.last:
            cur = cur.next
        cur.next = None
        self.last = cur

    def traverse(self):
        cur = self.first
        while cur:
            print(cur.val)
            cur = cur.next


class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


deq = Deque()
deq.addFirst(1)
deq.addFirst(2)
deq.addFirst(3)
deq.addLast(1)
deq.addLast(2)
deq.addLast(3)
deq.removeFirst()
deq.removeLast()
deq.traverse()
print(deq.size())
