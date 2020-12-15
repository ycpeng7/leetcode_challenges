#-------------------------------------------------------------------------------
#    LRU Cache
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/lru-cache/
# Completed 12/14/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Use a doubly linked list, always insert at head
2. hashmap to map key to the node which stores value

get()
1. If key doesn't exist in hashmap, return -1
2. Else, more the node corresponding to the key to head, and return value
Time: O(1)

put()
1. If key exists in hashmap, update value in node
2. Move node to head
3. Else, add node to head
4. If over capacity, remove the tail node

Time: O(1)

Space: O(N)
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Node:
    def __init__(self, val: int, key: int, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.numofNodes = 0
        self.head = None
        self.tail = None

    def _addToHashmap(self, key, node) -> None:
        self.hashmap[key] = node
    
    def _add(self, key, val) -> None:
        node = Node(val, key, self.head)
        if self.head is not None:
            self.head.next = node
        else:
            self.tail = node
        self.head = node
        self._addToHashmap(key, self.head)        
        self.numofNodes += 1

    def _movefront(self, node) -> None:
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.next
        self.head.next = node
        node.prev = self.head
        self.head = node

    def _removelast(self) -> None:
        new_tail = self.tail.next
        self.tail.next = None
        if new_tail is not None:
            new_tail.prev = None
        del self.hashmap[self.tail.key]
        self.tail = new_tail
        if self.numofNodes == 1:
            self.head = None
        self.numofNodes -= 1
        
    def get(self, key: int) -> int:
        if self.hashmap.get(key) is None:
            return -1
        else:
            node = self.hashmap.get(key)
            if node != self.head:
                self._movefront(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        # If key exists, update value
        if self.hashmap.get(key) is not None:
            node = self.hashmap.get(key)
            node.val = value
            if node != self.head:
                self._movefront(node)            
        else:
            self._add(key, value)
            if self.numofNodes > self.capacity:
                self._removelast()
 

if __name__ == '__main__':
    unittest.main()