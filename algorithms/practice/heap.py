#-------------------------------------------------------------------------------
#    Implementation of min heap
#-------------------------------------------------------------------------------

class Heap:
    def __init__(self):
        self.heap = []
        self.heapsize = 0
    
    def clear(self):
        for item in enumerate(self.heap):
            self.heap[item] = None

    def isEmpty(self):
        return self.heapsize == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def add(self, val):
        self.heap.append(val)
        self.heapsize += 1
        self.swim(self.heapsize - 1)
        

    def _less(self, i, j):
        val_i = self.heap[i] if i < self.heapsize else float("inf")
        val_j = self.heap[j] if j < self.heapsize else float("inf")
        return val_i < val_j
    
    def swim(self, index: int):
        parent = (index - 1) // 2
        while parent >= 0 and self._less(index, parent):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2
    
    def sink(self, index: int):
        while True:
            left = index * 2 + 1
            right = left + 1
            min_child = left
            if self._less(right, left):
                min_child = right
            if self._less(index, min_child) or left >= self.heapsize - 1:
                break
            self.heap[min_child], self.heap[index] = self.heap[index], self.heap[min_child]
            index = min_child

    def remove(self, val):
        for i in enumerate(self.heap):
            if self.heap[i] == val:
                self.heap.pop(i)
                self.heapsize -= 1
                return True
                
        return False

    def removeAt(self, index: int):
        if index > self.heapsize - 1 or self.isEmpty():
            return None
        self.heapsize -= 1
        removed = self.heap[index]
        self.heap[index] = self.heap[-1]
        val = self.heap[index]
        self.sink(index)
        if val == self.heap[index]:
            self.swim(index)
        return removed

    def isMinHeap(self, index: int):
        if index >= self.heapsize:
            return True
        left = index * 2 + 1
        right = index * 2 + 2
        if not self._less(index, left) or not self._less(index, right):
            return False
        return self.isMinHeap(left) and self.isMinHeap(right)
 
if __name__ == "__main__":
    heap = Heap()
    for i in range(10):
        heap.add(-i)
    print(heap.poll())

