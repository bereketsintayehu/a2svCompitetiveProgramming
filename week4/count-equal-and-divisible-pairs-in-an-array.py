class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        ans = 0

        for i, num in enumerate(nums):
            if num in d:
                for j in d[num]:
                    if (i * j) % k == 0:
                        ans += 1

            d[num].append(i)
        
        return ans