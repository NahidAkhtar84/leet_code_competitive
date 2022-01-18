# Marking visited nodes without modifying the linked list data
"""
Approach:
In this method, a temporary node is created. 
The next pointer of each node that is traversed is made to point to this temporary node. 
This way we are using the next pointer of a node as a flag 
to indicate whether the node has been traversed or not. 
Every node is checked to see if the next is pointing to a temporary node or not. 
In the case of the first node of the loop, 
the second time we traverse it this condition will be true, hence we find that loop exists. 
If we come across a node that points to null then the loop doesn’t exist.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = ""
        while head:
            if head.next == None:
                return False
            if head.next == temp:
                return True
            nxt = head.next
            head.next = temp
            head = nxt