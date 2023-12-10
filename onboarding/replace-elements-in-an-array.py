class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        opp = {}

        for old, new in reversed(operations):
                opp[old] = opp.get(new, new)

        return [opp[num] if num in opp else num for num in nums]