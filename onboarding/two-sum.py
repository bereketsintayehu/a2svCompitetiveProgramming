class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        
        for i, num in enumerate(nums):
            compl = target - num
            if compl in numIndex:
                return [i, numIndex[compl]]
            numIndex[num] = i