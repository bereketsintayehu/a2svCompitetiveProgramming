class ATM:

    def __init__(self):
        self.notes = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = amount
        used = [0] * 5

        if temp >= 500:
            n = temp // 500
            if n > self.notes[4]:
                temp -= self.notes[4] * 500
                used[4] = self.notes[4]
            else:
                temp -= n * 500
                used[4] += n
        if temp >= 200:
            n = temp // 200
            if n > self.notes[3]:
                temp -= self.notes[3] * 200
                used[3] = self.notes[3]

            else:
                temp -= n * 200
                used[3] += n

        if temp >= 100:
            n = temp // 100
            if n > self.notes[2]:
                temp -= self.notes[2] * 100
                used[2] = self.notes[2]

            else:
                temp -= n * 100
                used[2] += n
        if temp >= 50:
            n = temp // 50
            if n > self.notes[1]:
                temp -= self.notes[1] * 50
                used[1] = self.notes[1]

            else:
                temp -= n * 50
                used[1] += n
        if temp >= 20:
            n = temp // 20
            if n > self.notes[0]:
                temp -= self.notes[0] * 20
                used[0] = self.notes[0]

            else:
                temp -= n * 20
                used[0] += n
        if temp:
            return [-1]
        
        for i in range(5):
            self.notes[i] -= used[i]
        
        return used

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)