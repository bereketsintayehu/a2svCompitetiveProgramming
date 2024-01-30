class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p

        if target == 0:
            return 0

        ans = n
        map = {}
        map[0] = -1
        curr = 0

        for i in range(n):
            curr = (curr + nums[i]) % p
            
            if ((curr - target) % p) in map:
                ans = min(ans, i - map[(curr - target) % p])

            map[curr] = i
 
        return ans if ans < n else -1