class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0

        for a in answers:
            if cnt[a] % (a + 1) == 0:
                ans += a + 1
            cnt[a] += 1

        return ans