class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return []
        indexList, indexPos = [], 0
        while True:
            try:
                indexPos = nums.index(target, indexPos)
                indexList.append(indexPos)
                indexPos += 1
            except ValueError as e:
                break

        return indexList