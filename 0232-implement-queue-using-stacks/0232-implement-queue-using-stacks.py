from collections import deque
class MyQueue:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.reverse()
        self.stack.append(x)
        self.stack.reverse()
        

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