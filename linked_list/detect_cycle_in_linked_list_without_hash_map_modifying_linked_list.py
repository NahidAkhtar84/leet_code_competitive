# Definition for singly-linked list.
#! This is linked list structure change approache, using a flag with each node
#! Time complexity O(N), space complexity O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.flag = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.flag == True:
                return True
            head.flag = True
            head = head.next
            
        return False