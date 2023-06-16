class Solution:
    def numOfWays(self, nums):
        self.comb = self.generate(len(nums) + 1)
        return self.ways(nums) - 1

    def ways(self, nums):
        if len(nums) <= 2:
            return 1

        left = []
        right = []

        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                left.append(nums[i])
            else:
                right.append(nums[i])

        ans = self.comb[len(nums) - 1][len(left)]
        ans = (ans * self.ways(left)) % self.kMod
        ans = (ans * self.ways(right)) % self.kMod
        return ans

    def generate(self, numRows):
        comb = []

        for i in range(numRows):
            comb.append([1] * (i + 1))

        for i in range(2, numRows):
            for j in range(1, len(comb[i]) - 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % self.kMod

        return comb

    kMod = 10 ** 9 + 7
