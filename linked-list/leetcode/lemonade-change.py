class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ch = { 5 : 0, 10 : 0, 20 : 0}

        for b in bills: 
            ch[b] +=1
            
            if b == 10:
                if ch[5]:
                    ch[5] -= 1
                else:
                    return False
                
            if b == 20:
                if ch[5] and ch[10]:
                    ch[5] -= 1
                    ch[10] -= 1
                    
                elif ch[5] > 2:
                    ch[5] -= 3
                    
                else:
                    return False
                
        return True