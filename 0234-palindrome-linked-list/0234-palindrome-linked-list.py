# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            if not node or not node.next:
                return node
            
            new_head = reverse(node.next)
            node.next.next = node
            node.next = None
            return new_head

        def compare(list1, list2):
            while list1 and list2:
                if list1.val != list2.val:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True
        
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reversed_second_half = reverse(slow)
        
        return compare(head, reversed_second_half)
