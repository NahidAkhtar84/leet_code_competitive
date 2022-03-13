class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

class BST:   
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if root.val == key:
            return root

        if root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        return root

    def in_order_traverse(self, root):
        if root:
            self.in_order_traverse(root.left)
            print(root.val)
            self.in_order_traverse(root.right)

b = BST()
r = Node(50)
r = b.insert(r, 30)
r = b.insert(r, 20)
r = b.insert(r, 40)
r = b.insert(r, 70)
r = b.insert(r, 60)
r = b.insert(r, 80)
b.in_order_traverse(r)
