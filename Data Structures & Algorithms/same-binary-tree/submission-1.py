# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #both are null
            return True 
        if not p or not q: #one of them is not null which means false
            return False
        if p.val != q.val: #The values are different
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        #all of the recursion calls i.e. calls to t subtrees must all be equal, 
        #so only return true is that's the case