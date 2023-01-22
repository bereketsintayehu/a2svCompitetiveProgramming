from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqCount = Counter(tasks)
        
        freqTask = max(freqCount.values())
        freqTaskSlot = (freqTask - 1) * (n+1)
        numFreq = sum(freqCount[i] == freqTask for i in freqCount)
            
        return max(freqTaskSlot + numFreq, len(tasks))