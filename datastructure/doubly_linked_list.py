#-------------------------------------------------------------------------------
#    Implementation of Doubly Linked List
#-------------------------------------------------------------------------------

class DoublyLinkedList:
    class Node:
        def __init__(self, val: int=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def clear(self):
        trav = self.head
        while trav is not None:
            temp = trav.next
            del trav
            trav = temp
        self.length = 0

    def size(self):
        return self.length

    def add(self, val):
        self.addLast(val)
    
    def isEmpty(self):
        return self.length == 0

    def addFirst(self, val):
        if self.isEmpty():
            self.head = self.tail = self.Node(val)
        else:
            self.head.prev = self.Node(val, None, self.head)
            self.head = self.head.prev
        self.length += 1
    
    def addLast(self, val):
        if self.isEmpty():
            self.head = self.tail = self.Node(val)
        else:
            self.tail.next = self.Node(val, self.tail, None)
            self.tail = self.tail.next
        self.length += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise "Empty List"
        else:
            temp = self.head.next
            self.head = temp
            if temp is None:
                self.tail = None
            else:
                temp.prev = None
            self.length -= 1
    
    def removeLast(self):
        if self.isEmpty():
            raise "Empty List"
        else:
            temp = self.tail.prev
            self.tail = temp
            if temp is None:
                self.head = None
            else:
                temp.next = None
            self.length -= 1     

    def _remove(self, node):
        if node == self.head:
            self.removeFirst()
            return
        if node == self.tail:
            self.removeLast()
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        del node
        self.length -= 1
    
    def removeAt(self, index):
        if index < 0 or index >= self.length:
            raise "Invalid index"
        if index < self.length / 2:
            trav = self.head
            for _ in range(index):
                trav = trav.next
        else:
            trav = self.tail
            for _ in range(self.length - index):
                trav = trav.prev
        self._remove(trav)

    def removeVal(self, val):
        trav = self.head
        while trav is not None:
            temp = trav.next
            if trav.val == val:
                self._remove(trav)
            trav = temp

