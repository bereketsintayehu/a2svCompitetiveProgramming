class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sortKey(e):
            return int(e)
        nums.sort(reverse=True, key=sortKey)
        return nums[k-1]
        
