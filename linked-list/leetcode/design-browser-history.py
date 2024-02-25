class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.tab.next = ListNode(url, self.tab)
        self.tab = self.tab.next

    def back(self, steps: int) -> str:
        while self.tab.prev and steps:
            self.tab = self.tab.prev
            steps -= 1
        
        return self.tab.val

    def forward(self, steps: int) -> str:
        while self.tab.next and steps:
            self.tab = self.tab.next
            steps -= 1

        return self.tab.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)