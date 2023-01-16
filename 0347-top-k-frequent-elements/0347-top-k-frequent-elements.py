class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        elemCount = {}
        
        for i in nums:
            if i in elemCount:
                elemCount[i] += 1
            else:
                elemCount[i] = 1

        elemCount = sorted(elemCount, key=elemCount.get, reverse=True)

        return elemCount[:k]
        