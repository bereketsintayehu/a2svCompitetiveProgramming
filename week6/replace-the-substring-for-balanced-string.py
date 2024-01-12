class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        map = defaultdict(int)
        v = set()

        for ch, count in Counter(s).items():
            if count > n:
                map[ch] = count - n
                v.add(ch)

        if len(map) == 0:
            return 0

        start = end = 0
        ans = len(s)

        for end in range(len(s)):
            if s[end] in v:
                map[s[end]] -= 1
                if map[s[end]] == 0:
                    del map[s[end]]

            while all(count <= 0 for count in map.values()):
                ans = min(ans, end - start + 1)
                if s[start] in v:
                    map[s[start]] += 1

                start += 1

        if len(map) == 0:
            ans = min(ans, end - start + 1)
        
        return ans