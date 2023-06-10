# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lList = []
        ans = 0
        
        while head:
            lList.append(head.val)
            head = head.next
            
        n = len(lList) 
        
        for i in range(n//2):
            ans = max(ans, lList[i] + lList[n - 1 - i])
            
        return ans