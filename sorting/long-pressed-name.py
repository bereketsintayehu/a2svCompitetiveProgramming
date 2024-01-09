class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        l = len(name)
        n = len(typed)

        while i < l:
            if j >= n:
                return False
            if name[i] != typed[j]:
                return False
            
            j += 1
            while j < n and name[i] == typed[j] and (i == l - 1 or name[i] != name[i+1]):
                j += 1
            
            i += 1
        
        
        return j >= n