class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p1 = []
        count = 0
        p3 = []

        for num in nums:
            if num < pivot:
                p1.append(num)
            elif num > pivot:
                p3.append(num)
            else:
                count += 1
        
        return p1 + [pivot] * count + p3
