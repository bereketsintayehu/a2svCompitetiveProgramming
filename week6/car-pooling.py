class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001

        for n, f, t in trips:
            arr[f] += n
            arr[t] -= n

        curr = 0

        for p in arr:
            curr += p
            
            if curr > capacity:
                return False
        
        return True
        