class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[0] - x[1]))
        ans = 0
        A = B = len(costs) // 2
        
        for a, b in costs:
            if B == 0 or (A and a < b):
                ans += a
                A -=1
            else:
                ans += b
                B -= 1
        
        return ans