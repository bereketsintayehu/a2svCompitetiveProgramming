class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = -1, len(nums)
        
        while l + 1 < h:
            mid = (l + h) // 2
            if nums[mid] >= target:
                h = mid 
            else:
                l = mid
        
        if h >= len(nums) or nums[h] != target:
            return [-1, -1]

        ans = [h]

        l, h = h, len(nums)

        while l + 1 < h:
            mid = (l + h) // 2
            if nums[mid] > target:
                h = mid 
            else:
                l = mid

        ans.append(l)
        return ans