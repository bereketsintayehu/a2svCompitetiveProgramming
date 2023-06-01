class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        
        target = sorted(arr)
        
        for target in range(len(target), 0, -1):
            index = arr.index(target)

            if index == target - 1:
                continue

            if index != 0:
                ans.append(index + 1)
                arr = arr[:index + 1][::-1] + arr[index + 1:]

            ans.append(target)
            arr = arr[:target][::-1] + arr[target:]

        return ans