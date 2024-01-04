class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        n = len(nums)

        nums.sort()

        for i in range(n-2):
            l, r = i + 1, n - 1

            while l < r:
                curr = (nums[i] + nums[l] + nums[r]) - target
                
                if curr == 0:
                    return target

                if abs(ans) > abs(curr):
                    ans = curr
                
                if curr > 0:
                    r -= 1
                else:
                    l += 1

        return ans + target

        