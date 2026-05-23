# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right =root.right, root.left

        self.invertTree(root.left) #Call the invertTree method on this same Solution object, passing root.left as the argument.
        self.invertTree(root.right)

        return root