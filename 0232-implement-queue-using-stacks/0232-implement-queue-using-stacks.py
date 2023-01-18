from collections import deque
class MyQueue:
    def __init__(self):
        self.stack = deque()
        self.tempStack = deque()

    def push(self, x: int) -> None:
        while len(self.stack) > 0:
            self.tempStack.append(self.stack.pop())
        self.stack.append(x)
        while len(self.tempStack) > 0:
            self.stack.append(self.tempStack.pop())
                
    def pop(self) -> int:
        return self.stack.pop()
        
    def peek(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        return not bool(len(self.stack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()