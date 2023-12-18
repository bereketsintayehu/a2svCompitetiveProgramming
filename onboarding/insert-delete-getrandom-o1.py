class RandomizedSet:

    def __init__(self):
        self.randSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randSet:
            return False
        self.randSet.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.randSet:
            return False
        self.randSet.remove(val)
        return True

    def getRandom(self) -> int:
        return random.sample(self.randSet, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()