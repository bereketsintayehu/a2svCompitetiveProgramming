class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = len(nums) // 3
        ans = []
        for i in range(len(nums) - s):
            if nums[i] == nums[i + s]:
                ans.append(nums[i])
        return list(set(ans))