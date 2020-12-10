#-------------------------------------------------------------------------------
#    Implementation of queue using list with pointers
#-------------------------------------------------------------------------------

class Queue:
    def __init__(self):
        self.queue = [None] * 100
        self.end = -1
        self.front = 0
    
    def push(self, val):
        self.end += 1
        self.queue[self.end] = val

    def isEmpty(self):
        return self.front > self.end
    
    def pop(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        else:
            val = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return val
    
    def peek(self):
        if self.isEmpty:
            print("Empty Queue")
        else:
            print(self.queue[self.front])
    

if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    print(queue.pop())
    print(queue.pop())
    queue.push(3)
    print(queue.pop())
    print(queue.pop())