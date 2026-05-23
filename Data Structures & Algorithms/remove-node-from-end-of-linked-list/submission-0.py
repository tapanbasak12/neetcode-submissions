# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #A new node is created with value 0
        #Its .next points to the same node that head points to
        left=dummy
        right=head

        while n>0 and right:
            right= right.next
            n-=1
        
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next
