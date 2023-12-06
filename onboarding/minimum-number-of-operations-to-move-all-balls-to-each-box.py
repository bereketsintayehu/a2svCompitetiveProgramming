class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        for i, b in enumerate(boxes):
            if b == '1':
                for j in range(n):
                    ans[j] += abs(i-j)
                
        return ans