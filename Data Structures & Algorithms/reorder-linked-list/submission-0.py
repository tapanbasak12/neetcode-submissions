# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast.next and fast.next.next: #returns 1st middle in Even lists, for first middle use fast and fast.next
            fast= fast.next.next
            slow=slow.next
        
        #slow is the end of the first list now
        second = slow.next # Inititaling head of second part of the list
        prev = None
        slow.next=None  #Nulling the first list, Now we have two lists


        while second:
            #prev is already None and inititated
            #let's save the link to next node 
            tmp = second.next
            second.next = prev #reversing pointer
            #moving both nodes to next
            prev=second 
            second = tmp 
        
        second = prev
        while second:
            tmp1=head.next
            tmp2=second.next
            head.next=second
            second.next=tmp1
            head=tmp1
            second=tmp2


        


            
            