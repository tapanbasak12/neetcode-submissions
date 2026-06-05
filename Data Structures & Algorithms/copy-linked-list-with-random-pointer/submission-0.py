"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict_={}
        def func(node):
            if not node:
                return
            if node in dict_:
                return dict_[node]
            
            copy_node = Node(node.val)
            dict_[node]= copy_node

            copy_node.next= func(node.next)
            copy_node.random=func(node.random)
            return copy_node
        
        return func(head)
        