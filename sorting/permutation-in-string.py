class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = Counter(s1), Counter()
        l = 0
        k = len(s1)

        for r in range(len(s2)):
            s2_map[s2[r]] += 1

            if r >= k - 1:
                if s2_map == s1_map:
                    return True
                s2_map[s2[l]] -= 1
                l += 1

        return False