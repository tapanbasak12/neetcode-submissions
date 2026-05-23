# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #creating a dummy node with value zero, next none
        current=dummy
        #note that this is a connecting arrows problem, no extra space required
        while list1 and list2:
            if list1.val < list2.val: 
                current.next=list1
                list1=list1.next #move to next node
            else:
                current.next=list2
                list2=list2.next #move to next node

            current = current.next 
        
        #one of them has been read completely
        if list1:
            current.next=list1
        elif list2:
            current.next=list2

        return dummy.next #first value of dummy is useless
