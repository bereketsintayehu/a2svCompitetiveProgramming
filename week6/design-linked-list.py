class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
    
class MyLinkedList:
    # def __str__:
    #     curr = self.head
    #     while curr:
    #         print()
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
            
        return -1

    def addAtHead(self, val: int) -> None:
        self.size += 1

        dummy = Node(val)
        dummy.next = self.head
        self.head = dummy

    def addAtTail(self, val: int) -> None:
        self.size += 1
        curr = self.head

        if not self.head:
            self.addAtHead(val)
            return 

        while curr and curr.next:
            curr = curr.next

        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        self.size += 1
        if not self.head or index == 0:
            self.addAtHead(val)
            return 

        curr = self.head

        while index > 1:
            index -= 1
            curr = curr.next

        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if not index < self.size:
            return

        self.size -= 1

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        while index > 1:
            index -= 1
            curr = curr.next
        
        if not curr.next:
            curr = None
        else:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)