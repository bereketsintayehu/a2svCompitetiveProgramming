class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        psum = defaultdict(int)
        psum[0] = 1

        for num in nums:
          curr += num
          ans += psum[curr % k]
          psum[curr % k] += 1

        return ans
    