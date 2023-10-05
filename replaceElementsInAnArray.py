class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        operands = {num: index for index, num in enumerate(nums)}

        for operand, operation in operations:
            i = operands[operand]
            del operands[operand]

            nums[i] = operation
            operands[nums[i]] = i

        return nums

        
