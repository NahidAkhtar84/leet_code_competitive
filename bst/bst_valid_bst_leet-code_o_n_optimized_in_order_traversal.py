# Complexity: Time: O(N), space complexity: O(N)
# idea: https://afteracademy.com/blog/check-if-a-binary-tree-is-BST-or-not


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MIN_VAL = pow(-2, 31)
    MAX_VAL = pow(2, 31)-1
    
    def in_order_traversal(self, root, arr):
        if root:
            self.in_order_traversal(root.left, arr)
            arr.append(root.val)
            self.in_order_traversal(root.right, arr)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.in_order_traversal(root, arr)
        for i in range(0, len(arr)-1):
            if arr[i+1] <= arr[i]:
                return False
        return True
            
            