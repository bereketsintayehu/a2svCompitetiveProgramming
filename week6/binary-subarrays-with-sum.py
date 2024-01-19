class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum = defaultdict(int)
        psum[0] = 1
        ans = 0
        curr = 0

        for num in nums:
            curr += num
            ans += psum[curr - goal]
            psum[curr] += 1
        
        return ans