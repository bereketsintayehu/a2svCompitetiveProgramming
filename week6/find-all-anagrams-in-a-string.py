class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = sum([hash(c) for c in p])
        ans, n1, n2 = [], len(p), len(s)
        curr = sum([hash(c) for c in s[:n1]])

        for i in range(n1, n2):
            if curr == target:
                ans.append(i - n1)

            curr += hash(s[i]) - hash(s[i - n1])

        if curr == target:
                ans.append(n2 - n1)

        return ans