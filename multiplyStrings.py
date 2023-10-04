class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        inum1, inum2 = 0, 0

        for i in range(len(num1)):
            inum1 *= 10 
            inum1 += ord(num1[i]) - 48


        for i in range(len(num2)):
            inum2 *= 10 
            inum2 += ord(num2[i]) - 48
        
        return str(inum1 * inum2)
