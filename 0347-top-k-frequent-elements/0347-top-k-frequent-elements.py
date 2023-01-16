class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        elements = list(set(nums))

        def sortKey(e):
            return nums.count(e)

        elements.sort(key=sortKey, reverse=True)

        return elements[:k]