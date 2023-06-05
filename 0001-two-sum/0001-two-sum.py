class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = defaultdict(list)
        for i, num in enumerate(nums):
            numIndex[num].append(i)
        l, r = 0, len(nums) - 1

        nums.sort()
        
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                if nums[l] == nums[r]:
                    return [numIndex[nums[r]][0], numIndex[nums[r]][1]]
            
                return [numIndex[nums[l]][0], numIndex[nums[r]][0]]
            elif s > target:
                r -= 1
            else: 
                l += 1