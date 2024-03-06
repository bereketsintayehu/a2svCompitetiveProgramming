class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] >= target:
                h = mid - 1
            else:
                l = mid + 1

        return h + 1