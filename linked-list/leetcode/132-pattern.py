class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, t = [], -inf

        for num in reversed(nums):
            if num < t:
                return 1
            while stack and stack[-1] < num:
                t = stack.pop()
            stack.append(num)

        return 0