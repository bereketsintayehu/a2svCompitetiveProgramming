class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for l in range(n):
            p = nums[l] > 0

            if l == (l + nums[l]) % n:
                continue

            visited = set()
            while (nums[l] > 0) == p:
                if l in visited:
                    return True

                visited.add(l)
                l = (l + nums[l]) % n

                if l == (l + nums[l]) % n:
                    break
        
        return False