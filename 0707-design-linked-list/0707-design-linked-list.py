class MyLinkedList:

    def __init__(self):
        self.lList = []

    def get(self, index: int) -> int:
        if index < len(self.lList):
            return self.lList[index]
        return -1
        

    def addAtHead(self, val: int) -> None:
        self.lList.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.lList.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.lList):   
            self.lList.insert(index, val)
        elif index == len(self.lList):
            self.lList.append(val)
    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.lList):
            self.lList.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)