class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        term = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != term:
                return False
        
        return True
            
        