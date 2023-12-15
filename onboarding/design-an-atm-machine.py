class ATM:

    def __init__(self):
        self.notes = [0] * 5
        self.noteValue = {
            4: 500,
            3: 200,
            2: 100,
            1: 50,
            0: 20
        }

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = amount
        used = [0] * 5

        for i in range(4, -1, -1):
            n = temp // self.noteValue[i]
            if n > self.notes[i]:
                temp -= self.notes[i] * self.noteValue[i]
                used[i] = self.notes[i]
            else:
                temp -= n * self.noteValue[i]
                used[i] += n
        
        if temp:
            return [-1]
        
        for i in range(5):
            self.notes[i] -= used[i]
        
        return used

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)