# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s, t):
        if not t: return True  #if subTree (t) is null, return true    
        if not s and t: return False #if the actual tree is null, and subtree is not null
            
        if self.sameTree(t, s):
            return True
        
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)) #if any of the right 
        #or left is a substree then return true


    def sameTree(self, s, t):
        if not s and not t: return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        return False

