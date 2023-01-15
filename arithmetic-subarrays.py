class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        areArthimetic = [True] * len(l)
        for i in range(len(l)):
            tempNums = nums[l[i]:r[i]+1]
            tempNums.sort()
            d = tempNums[1] - tempNums[0]
            
            for j in range(1, len(tempNums)):
                if tempNums[j] - tempNums[j-1] != d:
                    areArthimetic[i] = False
                    break
                    
        return areArthimetic
                    
