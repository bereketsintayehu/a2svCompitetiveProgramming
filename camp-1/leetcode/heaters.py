class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        n, n2 = len(houses), len(heaters)

        def helper(rad):
            nonlocal n, n2
            i = j = 0
            
            while i < n and j < n2:
                neg = heaters[j] - rad
                pos = heaters[j] + rad

                if neg <= houses[i] <= pos:
                    i += 1

                elif houses[i] < neg:
                    return False
                
                else:
                    j += 1

            return i == n

        l, r = -1, max(heaters + houses)
        while l + 1 < r:
            mid = (l + r) // 2
            print(mid, helper(mid))
            if helper(mid):
                r = mid
            else:
                l = mid
        
        return r