# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self._merge(left, right)

    def _merge(self, a, b):
        dummy = ListNode(0)
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        return dummy.next
    
    

