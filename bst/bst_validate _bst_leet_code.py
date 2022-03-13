# Complexity: Time: O(N*2), space complexity: O(N)
# idea: https://afteracademy.com/blog/check-if-a-binary-tree-is-BST-or-not


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_min(self, root):
        if root == None:
            return root
        temp = root
        while temp.left != None:
            temp = temp.left
        return temp.val
    
    def get_max(self, root):
        if root == None:
            return root
        temp = root
        while temp.right != None:
            temp = temp.right
        return temp.val
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        max_left = self.get_max(root.left)
        min_right = self.get_min(root.right)
        
        if max_left and max_left >= root.val:
            return False
        if min_right and min_right <= root.val:
            return False
        
        if self.isValidBST(root.left)  and self.isValidBST(root.right):
            return True
        
        return False
            
            