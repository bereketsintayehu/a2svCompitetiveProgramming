class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 1
        ans = [0] * len(nums)

        for num in nums:
            if num < 0:
                ans[n] = num
                n += 2
            else:
                ans[p] = num
                p += 2
        
        return ans