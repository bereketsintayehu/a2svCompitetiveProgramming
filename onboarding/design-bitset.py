class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset =  [0] * size
        self.oneCount = 0
        self.zeroCount = size
        self.bitrev = [1] * size
        
    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.oneCount += 1
            self.zeroCount -= 1
        self.bitset[idx] = 1
        self.bitrev[idx] = 0
        

    def unfix(self, idx: int) -> None:
        if self.bitset[idx]:
            self.oneCount -= 1
            self.zeroCount += 1
        self.bitset[idx] = 0
        self.bitrev[idx] = 1
        

    def flip(self) -> None:
        self.oneCount, self.zeroCount = self.zeroCount, self.oneCount
        self.bitset, self.bitrev = self.bitrev, self.bitset

    def all(self) -> bool:
        return self.oneCount == self.size

    def one(self) -> bool:
        return self.oneCount

    def count(self) -> int:
        return self.oneCount

    def toString(self) -> str:
        return ''.join('1' if self.bitset[i] else '0' for i in range(self.size))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()