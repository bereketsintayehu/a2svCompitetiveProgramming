class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        currSum = 0
        prefixSum = {0: 1}

        for num in nums:
          currSum += num
          output += prefixSum.get(currSum - k, 0)
          prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return output