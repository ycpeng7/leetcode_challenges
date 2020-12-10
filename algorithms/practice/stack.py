#-------------------------------------------------------------------------------
#    Implementation of stack using list with pointers
#-------------------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.stack = [None] * 100
        self.top = -1
    
    def push(self, val):
        self.top += 1
        self.stack[self.top] = val

    def isEmpty(self):
        return self.top == -1
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            val = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return val
    
    def peek(self):
        if self.isEmpty:
            print("Empty stack")
        else:
            print(self.stack[self.top])
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())
    stack.push(3)
    print(stack.pop())
    print(stack.pop())