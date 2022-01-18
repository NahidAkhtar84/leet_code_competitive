# Definition for singly-linked list.
#! This is hash map approach, time complexity O(N), space complexity O(N)-> for storing in hash map/set

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        else:
            while head:
                if head.val == -1:
                    return True
                else:
                    head.val=-1
                    head = head.next
            return False
