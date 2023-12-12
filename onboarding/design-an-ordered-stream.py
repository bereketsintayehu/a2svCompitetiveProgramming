class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [0] * (n+1)
        self.p = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        buffer = []

        while self.p <= self.n and self.arr[self.p] != 0:
            buffer.append(self.arr[self.p])
            self.p += 1

        return buffer
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)