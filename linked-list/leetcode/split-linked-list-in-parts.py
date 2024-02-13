# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        ans = []
        j = size % k
        curr = head

        for i in range(k):
            dum = ListNode()
            res = dum
            t = size // k

            while t and curr:
                res.next = ListNode(curr.val)
                curr = curr.next
                res = res.next
                t -= 1

            if i < j and curr:
                res.next = ListNode(curr.val)
                curr = curr.next

            ans.append(dum.next)
        return ans
