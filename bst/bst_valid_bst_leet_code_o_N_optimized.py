# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MIN_VAL = pow(-2, 31)
    MAX_VAL = pow(2, 31)-1
    
    def helper(self, root, minVal, maxVal):
        if root == None:
            return True
        
        if minVal > root.val or maxVal < root.val:
            return False
        
        if self.helper(root.left, minVal, root.val-1):
            if self.helper(root.right, root.val+1, maxVal):
                return True
        return False
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if self.helper(root, self.MIN_VAL, self.MAX_VAL):
            return True
        return False
            
            