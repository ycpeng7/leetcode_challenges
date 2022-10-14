#-------------------------------------------------------------------------------
#    Implementation of queue using list with pointers
#-------------------------------------------------------------------------------

class Queue:
    def __init__(self):
        self.q = [None] * 100
        self.front  = 0 # The position of the first element in q. If there's no element, it's same as end.
        self.end = 0 # The position of where the next element will be added

    def push(self, val):
        self.q[self.end] = val
        self.end += 1

    def isEmpty(self):
        return self.front == self.end
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            val = self.q[self.front]
            self.q[self.front] = None
            self.front += 1
        return val
    
    def peek(self):
        return self.q[self.front]


if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    assert queue.pop() == 2
    queue.push(3)
    assert queue.pop() == 3
    assert queue.pop() == None