# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        number = 0
        dummy = head
        while dummy:
            number += 1
            dummy = dummy.next

        curr = head
        removeIndex = number - n
        if removeIndex == 0:
            return head.next

        for i in range(number - 1):
            if (i + 1) == removeIndex:
                curr.next = curr.next.next
                continue
            curr = curr.next
        
        return head
