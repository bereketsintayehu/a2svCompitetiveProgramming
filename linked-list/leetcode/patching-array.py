class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = curr = 0

        for num in nums:
            if curr > n:
                break

            while num - 1 > curr:
                if curr > n:
                    break
                curr += curr + 1
                ans += 1
            curr += num
        
        while curr + 1 < n:
            curr += (curr + 1)
            ans += 1 

        return ans