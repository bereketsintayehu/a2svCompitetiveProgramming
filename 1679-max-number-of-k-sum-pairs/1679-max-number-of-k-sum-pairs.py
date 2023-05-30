class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        numCount = {}
        
        for num in nums:
            if num in numCount:
                numCount[num] += 1
            else:
                numCount[num] = 1
        
        for num in nums:
            comp = k - num
            
            if numCount.get(num) and numCount.get(comp):
                if num == comp:
                    if numCount[num] >= 2:
                        count += 1
                        numCount[num] -= 2
                else:
                    count += 1
                    numCount[num] -= 1
                    numCount[comp] -= 1
        
        return count
                