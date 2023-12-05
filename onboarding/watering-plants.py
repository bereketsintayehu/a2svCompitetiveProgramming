class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity 
        steps = 0

        for i, plant in enumerate(plants):
            if plant > curr:
                steps += 2 * i + 1
                curr = capacity - plant
            else:
                curr -= plant
                steps += 1
        
        return steps

        