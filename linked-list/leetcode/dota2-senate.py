class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        direQ = deque()
        radQ = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == 'D':
                direQ.append(i)
            else:
                radQ.append(i)
        
        while direQ and radQ:
            if direQ[0] < radQ[0]:
                radQ.popleft()
                direQ.append(direQ.popleft() + n)
            else:
                direQ.popleft()
                radQ.append(radQ.popleft() + n)

        return 'Radiant' if radQ else 'Dire'