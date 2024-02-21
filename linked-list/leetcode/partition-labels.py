class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        prev = {char: index for index, char in enumerate(s)}
        
        ans = []
        start, end = 0, 0

        for i, char in enumerate(s):
            j = prev[char]  
            end = max(end, j)  
            
            if i == end:  
                ans.append(i - start + 1)
                start = i + 1  

        return ans