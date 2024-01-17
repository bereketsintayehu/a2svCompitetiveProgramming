class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        psum = defaultdict(int)
        psum[0] = 1

        for num in nums:
          curr += num % 2
          ans += psum[curr - k]
          psum[curr] += 1

        return ans
        
