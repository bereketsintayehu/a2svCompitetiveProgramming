from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        i = 0
        n = len(popped)
        for elem in pushed:
            stack.append(elem)
            while stack and i<n and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not bool(stack)
                
        