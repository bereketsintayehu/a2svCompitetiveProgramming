class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:   
        n = len(weights)
        arr = [0] * (n - 1)
        
        for i in range(n - 1):
            arr[i] = weights[i] + weights[i + 1]
            
        arr.sort()
        ans = 0
        
        for i in range(k - 1):
            ans += arr[n - 2 - i] - arr[i]

        return ans