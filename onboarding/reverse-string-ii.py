class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        flag = 1

        for i in range(0, len(s), k):
            if flag:
                ans.append(s[i : i + k][::-1])
            else:
                ans.append(s[i:i+k])
            flag = not flag

        return ''.join(ans)
        