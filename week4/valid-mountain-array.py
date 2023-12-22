class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        flag = False
        flag2 = False

        for i in range(1, n):
            if arr[i] == arr[i-1]:
                return False

            if flag:
                if arr[i] > arr[i-1]:
                    return False
                
            else:
                if arr[i] > arr[i-1]:
                    flag2 = True

                if arr[i-1] > arr[i]:
                    if flag2:
                        flag = True
                    else:
                        return False

        return flag
