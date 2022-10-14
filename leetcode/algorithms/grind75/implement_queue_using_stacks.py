class MyQueue:
    """
    push(): push to stack 1, update front if front is null
    pop(): keep popping stack 1 and push to stack 2 until it's empty, then pop all stack 2 and push to stack 1. The first one out of
    stack 2 is the new front.
    peek(): return front
    empty(): true if stack 1 is empty
    
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = [] 
        self.front = None
        
    def push(self, x: int) -> None:
        self.stack_1.append(x)
        if self.front is None:
            self.front = x

    def pop(self) -> int:

        while len(self.stack_1) > 1:
            popped = self.stack_1.pop()
            self.stack_2.append(popped)
        cur_front = self.stack_1.pop()

        self.front = None
        while len(self.stack_2) > 0:
            popped_2 = self.stack_2.pop()
            if self.front is None:
                self.front = popped_2
            self.stack_1.append(popped_2)

        return cur_front

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.stack_1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()