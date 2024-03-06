class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = -1, len(letters)

        while l + 1 < h:
            mid = (l + h) // 2
            if letters[mid] > target:
                h = mid
            else:
                l = mid
        
        return letters[h] if h < len(letters) else letters[0]