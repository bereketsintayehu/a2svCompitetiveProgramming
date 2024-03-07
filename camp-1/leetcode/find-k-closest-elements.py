class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        l, r = max(0, idx - k), min(len(arr) - 1, idx + k)

        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
            
        return arr[l:r + 1]
