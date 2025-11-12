# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            duplicate = False
            while (
                curr.next is not None
                and curr.next.val == curr.val
            ):
                curr = curr.next
                duplicate = True

            if duplicate:
                curr = curr.next
                prev.next = curr
            
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next
