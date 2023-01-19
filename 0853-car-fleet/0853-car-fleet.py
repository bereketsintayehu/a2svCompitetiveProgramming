from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()
        cars = {position[i] : speed[i] for i in range(len(position))}
        sortedCars = sorted(cars)
        timeLeft = [(target - sortedCars[i])/cars[sortedCars[i]] for i in range(len(speed))]

        
        for i in range(len(speed)-1, -1, -1):
            stack.append(timeLeft[i])
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
        