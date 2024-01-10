class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        winB = sum(1 for b in blocks[:k] if b == 'B')
        maxB = winB
        
        for i in range(k, len(blocks)):
            if blocks[i] == 'B':
                winB += 1
            if blocks[i - k] == 'B':
                winB -= 1
            maxB = max(maxB, winB)

        return max(0, k - maxB)