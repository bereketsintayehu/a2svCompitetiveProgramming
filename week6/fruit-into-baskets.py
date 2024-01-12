class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = l = 0
        freq = Counter()

        for r in range(len(fruits)):
            freq[fruits[r]] += 1

            while len(freq) > 2:
                fruit = fruits[l]
                freq[fruit] -= 1

                if freq[fruit] == 0:
                    del freq[fruit]
                
                l += 1

            ans = max(ans, sum(freq.values()))

        return ans