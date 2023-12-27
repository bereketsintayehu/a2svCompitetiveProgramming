class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = { num : index for index, num in enumerate(arr2) }
        n = len(arr2)
        
        return sorted(arr1, key=lambda x : order[x] if x in order else n + x)