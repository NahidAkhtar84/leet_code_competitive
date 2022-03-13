
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.arr = []
        
        def check(node):
            if node:
                check(node.left)
                self.arr.append(node)
                check(node.right)
        check(root)
        self.minNode = TreeNode(self.arr[0].val-1, left=None, right=root)
        self.current_index = -1
            

    def next(self) -> int:
        self.current_index += 1
        return self.arr[self.current_index].val

    def hasNext(self) -> bool:
        if self.current_index+1 < len(self.arr):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
param_1 = obj.next()
param_2 = obj.hasNext()
