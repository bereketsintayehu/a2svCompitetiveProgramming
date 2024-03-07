class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if sum(ceil(num / mid) for num in nums) <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        
        return r + 1