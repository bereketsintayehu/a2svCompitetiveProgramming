class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = {'T': 0, 'F': 0}
        curr = 0
        ans = start = 0

        for end in range(len(answerKey)):
            freq[answerKey[end]] += 1
            curr = max(curr, freq[answerKey[end]])

            while (end - start + 1 - curr) > k:
                freq[answerKey[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)

        return ans