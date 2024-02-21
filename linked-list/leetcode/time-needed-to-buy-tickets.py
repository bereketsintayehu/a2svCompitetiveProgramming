class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[k] == 0:
                    break

                if tickets[i] > 0:
                    ans += 1
                    tickets[i] -= 1

        return ans