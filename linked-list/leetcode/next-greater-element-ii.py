class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        stack = []
        for i in range(2 * n):
            while stack and stack[-1][1] < nums[i % n]:
                ans[stack.pop()[0]] = nums[i % n]

            stack.append([i % n, nums[i % n]])

        return ans