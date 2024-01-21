class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        pre = [0] * n
        post = [0] * n

        pre[0] = nums[0]
        post[-1] = nums[-1]

        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]
            post[-i - 1] = post[-i] + nums[-i - 1]


        return [(num * i) - pre[i] + post[i] - (num * (n - i - 1)) for i, num in enumerate(nums)]