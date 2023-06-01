class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occ = defaultdict(int)
        
        for num in arr:
            occ[num] += 1
        
        sr = sorted(occ, key=occ.get, reverse=True)
        sz = len(arr)//2
        temp = 0
        ans = 0
        
        for s in sr:
            if temp >= sz:
                break
            temp += occ[s]
            ans += 1
            
        return ans