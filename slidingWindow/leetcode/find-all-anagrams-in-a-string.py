class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target, ans, n1, n2 = Counter(p), [], len(p), len(s)
        curr = Counter(s[:n1])

        for i in range(n1, n2):
            if curr == target:
                ans.append(i - n1)

            curr[s[i]] += 1
            curr[s[i - n1]] -= 1

            if curr[s[i - n1]] == 0:
                del curr[s[i - n1]]

        if curr == target:
                ans.append(n2 - n1)
        return ans