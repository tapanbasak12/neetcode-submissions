# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next: #You need to check if currect node is not empty and the next node is not empty
        #Otherwise you are checking what comes after  nothing
            fast= fast.next.next
            slow = slow.next
            if (fast == slow):
                return True
        
        return False