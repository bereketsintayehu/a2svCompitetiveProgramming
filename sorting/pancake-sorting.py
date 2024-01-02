class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(arr), 0, -1):
            j = 0
            currMax = float('-inf')
            
            for k in range(i):
                if arr[k] > currMax:
                    currMax = arr[k]
                    j = k 

            if j == i - 1:
                continue

            if i != 0:
                ans.append(j + 1)
                arr = arr[:j + 1][::-1] + arr[j + 1:]

            ans.append(i)
            arr = arr[:i][::-1] + arr[i:]

        return ans