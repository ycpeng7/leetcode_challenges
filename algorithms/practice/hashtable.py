#-------------------------------------------------------------------------------
#    Implementation of hash table using separate chaining with linkedlist
#-------------------------------------------------------------------------------


class Node:
    def __init__(self, key: str, val: int):
        self.key = key
        self.val = val
        self.next = None

    def equals(self, other):
        return self.key == other.key

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.load_factor = 0.6
        self.size = 0

    def _hash(self, key: str):
        return hash(key) % self.capacity
    
    def _resizeTable(self):
        self.capacity *= 2
        newTable = [None] * self.capacity
        for node in self.table:
            if node:
                newTable[self._hash(node.key)] = node

    def _insert(self, index: int, node) -> None:
        if self.table[index] is None:
            self.table[index] = node
        else:
            trav = self.table[index]
            while trav.next is not None:
                if node.equals(trav):
                    trav.val = node.val
                    return
                trav = trav.next
            trav.next = node
        self.size += 1
        if self.size > self.capacity * self.load_factor:
            self._resizeTable()


    def insert(self, key: str, val: int) -> None:
        if key is None:
            raise ValueError("Illegal key")
        else:
            newNode = Node(key, val)
            index = self._hash(key)
            self._insert(index, newNode)

    